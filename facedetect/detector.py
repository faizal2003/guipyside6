import argparse
import pickle
from collections import Counter
from pathlib import Path
import os
from datetime import datetime
import xml.etree.ElementTree as ET
from PySide6.QtWidgets import QMessageBox


import face_recognition
from PIL import Image, ImageDraw

DEFAULT_ENCODINGS_PATH = Path("facedetect/output/encodings.pkl")
BOUNDING_BOX_COLOR = "blue"
TEXT_COLOR = "white"

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

def recognize_faces(
    image_location: str,
    model: str = "hog",
    encodings_location: Path = DEFAULT_ENCODINGS_PATH,
) -> None:
    """
    Given an unknown image, get the locations and encodings of any faces and
    compares them against the known encodings to find potential matches.
    """
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
        _display_face(draw, bounding_box, name)

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
        else:
            print("wajah dikenali, membuka brankas")
            # QMessageBox.information("Gagal", "wajah tidak dikenali, brankas tetap tertutup")
            act = "berhasil"
            #todo: open safe when face is recognized
        _display_face(draw, bounding_box, name)
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

    pillow_image.save(save_path)
    print(f"Saved image to {save_path}")
    log_to_xml(
        name=base_name,
        waktu=timestamplog,
        aktivitas=act)
    
    act = ""
    

def _recognize_face(unknown_encoding, loaded_encodings):
    """
    Given an unknown encoding and all known encodings, find the known
    encoding with the most matches.
    """
    boolean_matches = face_recognition.compare_faces(
        loaded_encodings["encodings"], unknown_encoding
    )
    votes = Counter(
        name
        for match, name in zip(boolean_matches, loaded_encodings["names"])
        if match
    )
    if votes:
        return votes.most_common(1)[0][0]


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