import argparse
import pickle
import os
import cv2
import time
from collections import Counter
from pathlib import Path

import face_recognition
from PIL import Image, ImageDraw

DEFAULT_ENCODINGS_PATH = Path("output/encodings.pkl")
BOUNDING_BOX_COLOR = "blue"
TEXT_COLOR = "white"

# Create directories if they don't already exist
Path("training").mkdir(exist_ok=True)
Path("output").mkdir(exist_ok=True)
Path("validation").mkdir(exist_ok=True)

# parser = argparse.ArgumentParser(description="Recognize faces in an image")
# parser.add_argument("--train", action="store_true", help="Train on input data")
# parser.add_argument(
#     "--validate", action="store_true", help="Validate trained model"
# )
# parser.add_argument(
#     "--test", action="store_true", help="Test the model with an unknown image"
# )
# parser.add_argument(
#     "-m",
#     action="store",
#     default="hog",
#     choices=["hog", "cnn"],
#     help="Which model to use for training: hog (CPU), cnn (GPU)",
# )
# parser.add_argument(
#     "-f", action="store", help="Path to an image with an unknown face"
# )
# args = parser.parse_args()

def capture_for_val():
    # Create the folder if it doesn't exist
    folder_name = "check"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    
    # Open the camera
    cap = cv2.VideoCapture(0)  # 0 is the default camera
    
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return
    
    # Capture a single frame
    ret, frame = cap.read()
    
    if ret:
        image_path = os.path.join(folder_name, "captured_image.jpg")
        cv2.imwrite(image_path, frame)
        print(f"Image saved at {image_path}")
    else:
        print("Error: Could not capture image.")
    
    # Release the camera and close windows
    cap.release()
    cv2.destroyAllWindows()

# Run the function
# capture_and_save_image()


def capture_and_save_images():
    # Create the folder if it doesn't exist
    folder_name = "training"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    
    # Open the camera
    cap = cv2.VideoCapture(0)  # 0 is the default camera
    
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return
    
    for i in range(5):
        # Capture a single frame
        ret, frame = cap.read()
        
        if ret:
            image_path = os.path.join(folder_name, f"captured_image_{i+1}.jpg")
            cv2.imwrite(image_path, frame)
            print(f"Image {i+1} saved at {image_path}")
        else:
            print(f"Error: Could not capture image {i+1}.")
            
        # Wait for 5 seconds before capturing the next image
        time.sleep(5)
    
    # Release the camera and close windows
    cap.release()
    cv2.destroyAllWindows()

# Run the function
# capture_and_save_images()




def encode_known_faces(
    model: str = "hog", encodings_location: Path = DEFAULT_ENCODINGS_PATH
) -> None:
    """
    Loads images in the training directory and builds a dictionary of their
    names and encodings.
    """
    names = []
    encodings = []

    for filepath in Path("training").glob("*/*"):
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
        _display_face(draw, bounding_box, name)

    del draw
    pillow_image.show()


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


