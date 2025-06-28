import argparse
import pickle
from collections import Counter
from pathlib import Path
import RPi.GPIO as GPIO
import threading
import time
import signal
import sys
import os
from datetime import datetime
import xml.etree.ElementTree as ET
from PySide6.QtWidgets import QMessageBox
import numpy as np


import face_recognition
from PIL import Image, ImageDraw

DEFAULT_ENCODINGS_PATH = Path("facedetect/output/encodings.pkl")
BOUNDING_BOX_COLOR = "blue"
TEXT_COLOR = "white"
aksi = "tidak ada aksi"

# Create directories if they don't already exist
Path("training").mkdir(exist_ok=True)
Path("output").mkdir(exist_ok=True)
Path("validation").mkdir(exist_ok=True)

parser = argparse.ArgumentParser(description="Recognize faces in an image")
parser.add_argument("--train", action="store_true", help="Train on input data")
parser.add_argument(
    "--validate", action="store_true", help="Validate trained model"
)
parser.add_argument(
    "--test", action="store_true", help="Test the model with an unknown image"
)
parser.add_argument(
    "-m",
    action="store",
    default="hog",
    choices=["hog", "cnn"],
    help="Which model to use for training: hog (CPU), cnn (GPU)",
)
parser.add_argument(
    "-f", action="store", help="Path to an image with an unknown face"
)
args = parser.parse_args()


def encode_known_faces(
    model: str = "hog", encodings_location: Path = DEFAULT_ENCODINGS_PATH
) -> None:
    """
    Loads images in the training directory and builds a dictionary of their
    names and encodings.
    """
    names = []
    encodings = []

    print("start encoding faces")
    for filepath in Path("facedetect/training").glob("*/*"):
        name = filepath.parent.name
        image = face_recognition.load_image_file(filepath)

        face_locations = face_recognition.face_locations(image, model=model)
        face_encodings = face_recognition.face_encodings(image, face_locations)

        for encoding in face_encodings:
            names.append(name)
            encodings.append(encoding)

    name_encodings = {"names": names, "encodings": encodings}
    with encodings_location.open(mode="wb") as f:
        pickle.dump(name_encodings, f)
    print("finished encoding faces")
    isComplete = True
    
RELAY_PINS = [17, 27]  # GPIO pins connected to relays
RELAY_ACTIVE_LOW = True  # Set to False if relays are active high

class DualRelayController:
    def __init__(self, pins, active_low=True):
        self.pins = pins
        self.active_low = active_low
        self.setup_gpio()
        
    def setup_gpio(self):
        """Initialize GPIO settings"""
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Enable pull-up resistor
        for pin in self.pins:
            GPIO.setup(pin, GPIO.OUT)
        # Initialize both relays to OFF state
        self.all_relays_off()
        
    def relay_on(self, relay_num):
        """Turn specific relay ON (1 or 2)"""
        if relay_num < 1 or relay_num > len(self.pins):
            print(f"Invalid relay number. Use 1-{len(self.pins)}")
            return
            
        pin = self.pins[relay_num - 1]
        if self.active_low:
            GPIO.output(pin, GPIO.LOW)
        else:
            GPIO.output(pin, GPIO.HIGH)
        print(f"Relay {relay_num} (GPIO {pin}) ON")
        
    def relay_off(self, relay_num):
        """Turn specific relay OFF (1 or 2)"""
        if relay_num < 1 or relay_num > len(self.pins):
            print(f"Invalid relay number. Use 1-{len(self.pins)}")
            return
            
        pin = self.pins[relay_num - 1]
        if self.active_low:
            GPIO.output(pin, GPIO.HIGH)
        else:
            GPIO.output(pin, GPIO.LOW)
        print(f"Relay {relay_num} (GPIO {pin}) OFF")
        
    def relay_toggle(self, relay_num):
        """Toggle specific relay state"""
        if relay_num < 1 or relay_num > len(self.pins):
            print(f"Invalid relay number. Use 1-{len(self.pins)}")
            return
            
        pin = self.pins[relay_num - 1]
        current_state = GPIO.input(pin)
        if (self.active_low and current_state == GPIO.LOW) or \
           (not self.active_low and current_state == GPIO.HIGH):
            self.relay_off(relay_num)
        else:
            self.relay_on(relay_num)
            
    def all_relays_on(self):
        """Turn all relays ON"""
        for i in range(len(self.pins)):
            self.relay_on(i + 1)
            
    def all_relays_off(self):
        """Turn all relays OFF"""
        for i in range(len(self.pins)):
            self.relay_off(i + 1)
            
    def cleanup(self):
        """Clean up GPIO resources"""
        self.all_relays_off()
        GPIO.cleanup()
        print("GPIO cleanup completed")

def signal_handler(sig, frame):
    """Handle Ctrl+C gracefully"""
    print("\nShutting down...")
    relay.cleanup()
    sys.exit(0)

def check_door_open():
    """Check if door is open - replace with actual GPIO read"""
    # return GPIO.input(22) == GPIO.LOW
    return GPIO.input(22) == GPIO.HIGH
    # return True  # Placeholder - replace with actual sensor reading

def trigger_alarm():
    """Sound alarm"""
    print("🚨 ALARM: Door open too long!")
    GPIO.output(27, GPIO.LOW)  # Turn on alarm
    
def stop_alarm():
    """Stop alarm"""
    print("✅ Alarm stopped")
    GPIO.output(27, GPIO.HIGH)  # Turn off alarm

def monitor_door():
    """Monitor door for 30 seconds, trigger alarm if still open"""
    time.sleep(30)  # Wait 30 seconds
    
    if check_door_open():
        trigger_alarm()
        
        # Keep alarm on until door closes
        while check_door_open():
            time.sleep(1)
            
        stop_alarm()


def recognize_faces(
    image_location: str,
    model: str = "hog",
    encodings_location: Path = DEFAULT_ENCODINGS_PATH,
) -> None:
    """
    Given an unknown image, get the locations and encodings of any faces and
    compares them against the known encodings to find potential matches.
    """
    
    global relay
    
    # Set up signal handler for graceful shutdown
    signal.signal(signal.SIGINT, signal_handler)
    
    # Initialize dual relay controller
    relay = DualRelayController(RELAY_PINS, RELAY_ACTIVE_LOW)
    
    with encodings_location.open(mode="rb") as f:
        loaded_encodings = pickle.load(f)

    input_image = face_recognition.load_image_file(image_location)

    input_face_locations = face_recognition.face_locations(
        input_image, model=model
    )
    input_face_encodings = face_recognition.face_encodings(
        input_image, input_face_locations
    )

    pillow_image = Image.fromarray(input_image)
    draw = ImageDraw.Draw(pillow_image)

    for bounding_box, unknown_encoding in zip(
        input_face_locations, input_face_encodings
    ):
        name = _recognize_face(unknown_encoding, loaded_encodings)
        if not name:
            name = "Unknown"
            print("wajah tidak dikenali")
            act = "gagal"
            aksi = "gagal"
        # _display_face(draw, bounding_box, name)

    del draw
    # pillow_image.show()
    with encodings_location.open(mode="rb") as f:
        loaded_encodings = pickle.load(f)

    input_image = face_recognition.load_image_file(image_location)

    input_face_locations = face_recognition.face_locations(
        input_image, model=model
    )
    input_face_encodings = face_recognition.face_encodings(
        input_image, input_face_locations
    )

    pillow_image = Image.fromarray(input_image)
    draw = ImageDraw.Draw(pillow_image)

# Initialize a set to keep track of saved names in this image
    recognized_names = set()

    for bounding_box, unknown_encoding in zip(
        input_face_locations, input_face_encodings
    ):
        name = _recognize_face(unknown_encoding, loaded_encodings)
        if not name:
            name = "Unknown"
            print("wajah tidak dikenali")
            # QMessageBox.information("Gagal", "wajah tidak dikenali, brankas tetap tertutup")
            act = "gagal"
            aksi = "gagal"
            aksi = "gagal"
            relay.relay_on(2)
            time.sleep(2)
            relay.relay_off(2)
            time.sleep(2)
            relay.relay_on(2)
            time.sleep(2)
            relay.relay_off(2)
            time.sleep(2)
            relay.relay_on(2)
            time.sleep(2)
            relay.relay_off(2)
            time.sleep(2)
        else:
            if name == "Unknown":
                print("wajah tidak dikenali")
                # QMessageBox.information("Gagal", "wajah tidak dikenali, brankas tetap tertutup")
                act = "gagal"
                aksi = "gagal"
                aksi = "gagal"
                relay.relay_on(2)
                time.sleep(2)
                relay.relay_off(2)
                time.sleep(2)
                relay.relay_on(2)
                time.sleep(2)
                relay.relay_off(2)
                time.sleep(2)
                relay.relay_on(2)
                time.sleep(2)
                relay.relay_off(2)
            else:
                print("wajah dikenali, membuka brankas")
                # QMessageBox.information("Gagal", "wajah tidak dikenali, brankas tetap tertutup")
                act = "berhasil"
                aksi = "berhasil"
                relay.relay_on(1)
                time.sleep(5)
                relay.relay_off(1)
                #todo: open safe when face is recognized
                _display_face(draw, bounding_box, name)
                door_thread = threading.Thread(target=monitor_door)
                door_thread.daemon = True
                door_thread.start()
        recognized_names.add(name)

    del draw
    # pillow_image.show()
    # if recognized_names == "":
    #     print("Tidak ada wajah yang dikenali dalam gambar.")
    # print(sorted(recognized_names))
    # if len(sorted(recognized_names)) == 0:
    #     print("Tidak ada wajah yang dikenali dalam gambar.")
        
# Save image with name(s) and timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    timestamplog = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # If multiple names are detected, join them with underscores
    base_name = "_".join(sorted(recognized_names))
    # nama = sorted(recognized_names)
    # print(nama)
    # print(base_name)
    # Final filename
    save_dir = "facedetect/output_images"
    os.makedirs(save_dir, exist_ok=True)
    filename = f"{base_name}_{timestamp}.jpg"
    save_path = os.path.join(save_dir, filename)
    save_pre= os.path.join("img_preview", "preview.jpg")

    pillow_image.save(save_path)
    pillow_image.save(save_pre)
    print(f"Saved image to {save_path}")
    log_to_xml(
        name=base_name,
        waktu=timestamplog,
        aktivitas=act)
    
    act = ""
    return aksi, name


def open_safe():
    """
    Opens the safe by activating the relay for a specified duration.
    """
    relay.relay_on(1)  # Activate relay 1 to open the safe
    time.sleep(5)  # Keep it open for 5 seconds
    relay.relay_off(1)  # Deactivate relay 1 to close the safe
    print("Safe opened for 5 seconds")

def _recognize_face(unknown_encoding, loaded_encodings):
    face_distances = face_recognition.face_distance(
        loaded_encodings["encodings"], unknown_encoding
    )
    best_match_index = np.argmin(face_distances)
    distance_threshold = 0.45
    if face_distances[best_match_index] < distance_threshold:
        return loaded_encodings["names"][best_match_index]
    else:
        return "Unknown"


def _display_face(draw, bounding_box, name):
    """
    Draws bounding boxes around faces, a caption area, and text captions.
    """
    top, right, bottom, left = bounding_box
    draw.rectangle(((left, top), (right, bottom)), outline=BOUNDING_BOX_COLOR)
    text_left, text_top, text_right, text_bottom = draw.textbbox(
        (left, bottom), name
    )
    draw.rectangle(
        ((text_left, text_top), (text_right, text_bottom)),
        fill=BOUNDING_BOX_COLOR,
        outline=BOUNDING_BOX_COLOR,
    )
    draw.text(
        (text_left, text_top),
        name,
        fill=TEXT_COLOR,
    )


def validate(model: str = "hog"):
    """
    Runs recognize_faces on a set of images with known faces to validate
    known encodings.
    """
    for filepath in Path("validation").rglob("*"):
        if filepath.is_file():
            recognize_faces(
                image_location=str(filepath.absolute()), model=model
            )


def log_to_xml(name, waktu, aktivitas="login"):
        """Log face recognition data to XML file"""
        xml_file = "log_data.xml"
        
        # Check if XML file exists
        if os.path.exists(xml_file):
            # Load existing XML
            try:
                tree = ET.parse(xml_file)
                root = tree.getroot()
            except ET.ParseError:
                # If file is corrupted, create new root
                root = ET.Element("logs")
                tree = ET.ElementTree(root)
        else:
            # Create new XML structure
            root = ET.Element("logs")
            tree = ET.ElementTree(root)
        
        # Get the next record number
        existing_records = root.findall("record")
        next_no = len(existing_records) + 1
        
        # Create new record
        record = ET.SubElement(root, "record")
        
        # Add data elements
        no_elem = ET.SubElement(record, "no")
        no_elem.text = str(next_no)
        
        nama_elem = ET.SubElement(record, "nama")
        nama_elem.text = name if name != "Unknown" else "tidak_dikenal"
        
        tanggal_waktu_elem = ET.SubElement(record, "tanggal_waktu")
        tanggal_waktu_elem.text = waktu
        
        aktivitas_elem = ET.SubElement(record, "aktivitas")
        aktivitas_elem.text = aktivitas
        
        # Save XML file
        
        tree.write(xml_file, encoding='UTF-8', xml_declaration=True)
        print(f"Data logged to {xml_file}")
   
    
def indent_xml(self, elem, level=0):
    """Add indentation to XML for better readability"""
    i = "\n" + level * "  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for child in elem:
            self.indent_xml(child, level + 1)
        if not child.tail or not child.tail.strip():
            child.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
                elem.tail = i


if __name__ == "__main__":
    if args.train:
        encode_known_faces(model=args.m)
    if args.validate:
        validate(model=args.m)
    if args.test:
        recognize_faces(image_location=args.f, model=args.m)