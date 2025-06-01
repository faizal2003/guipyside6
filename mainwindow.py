# This Python file uses the following encoding: utf-8
import cv2
import os
from datetime import datetime
import sys
import ui_src
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
# from facedetect import detector


# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow
from ui_mainmenu import Ui_MainMenu
from ui_tambahdata import Ui_TambahData
from ui_password import Ui_Password
from ui_log import Ui_Log

# Add the facedetect folder to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'facedetect'))

# Now you can import detector
import detector


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.pressed.connect(self.teststart)
        self.ui.pushButton_2.pressed.connect(self.testshutdown)
        self.ui.pushButton_3.pressed.connect(self.testimg)

    def teststart(self):
        print("button start pressed")
        widget.setCurrentIndex(widget.currentIndex() + 1)
    def testshutdown(self):
        print("button shut down pressed")
        sys.exit(app.exec())
    def testimg(self):
        print("button img pressed")
        
        # Create facedetect/targetface folder if it doesn't exist
        folder_name = os.path.join("facedetect", "targetface")
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
            print(f"Created folder: {folder_name}")
        
        # Initialize camera
        cap = cv2.VideoCapture(0)  # 0 for default camera
        
        if not cap.isOpened():
            print("Error: Could not open camera")
            QMessageBox.warning(self, "Camera Error", "Could not access camera!")
            return
        
        try:
            # Capture frame
            ret, frame = cap.read()
            
            if ret:
                # Fixed filename that will be overwritten each time
                filename = "target_image.jpg"
                filepath = os.path.join(folder_name, filename)
                
                # Save the image
                success = cv2.imwrite(filepath, frame)
                
                if success:
                    print(f"Image saved successfully: {filepath}")
                    # QMessageBox.information(self, "Success", f"Image saved to {filepath}")
                else:
                    print("Error: Failed to save image")
                    QMessageBox.warning(self, "Save Error", "Failed to save image!")
            else:
                print("Error: Failed to capture image")
                QMessageBox.warning(self, "Capture Error", "Failed to capture image from camera!")
                
        except Exception as e:
            print(f"Error during image capture: {str(e)}")
            QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")
            
        finally:
            # Always release the camera
            cap.release()
            print("Camera released")
            
        detector.recognize_faces(image_location=filepath)
        print("Face recognition completed")

class SecondWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainMenu()
        self.ui.setupUi(self)
        self.ui.pushButton_5.pressed.connect(self.back_action)
        self.ui.pushButton_2.pressed.connect(self.tambahdata_action)
        self.ui.pushButton.pressed.connect(self.logbutton_action)

    def logbutton_action(self):
        print("button log pressed")
        widget.setCurrentIndex(widget.currentIndex() + 3 )
    def back_action(self):
        # print("button start pressed")
        widget.setCurrentIndex(widget.currentIndex() - 1)

    def tambahdata_action(self):
        print("button shut down pressed")
        widget.setCurrentIndex(widget.currentIndex() + 1)


class TambahData(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_TambahData()
        self.ui.setupUi(self)
        
        # Connect buttons
        self.ui.pushButton.pressed.connect(self.back_action)
        self.ui.pushButton_2.pressed.connect(self.capture_photo)  # CAPTURE button
        self.ui.pushButton_3.pressed.connect(self.save_photo)     # SELESAI button
        self.ui.pushButton_4.pressed.connect(self.reset_camera)   # RESET button
        
        # Camera setup
        self.camera = None
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)
        self.captured_frame = None
        self.is_capturing = False
        self.camera_initialized = False
        
        # Find the camera display area (assuming it's a QLabel in your UI)
        # You may need to adjust this based on your actual UI structure
        self.camera_label = None
        self.setup_camera_display()
    
    def showEvent(self, event):
        """Handle when window is shown - restart camera"""
        super().showEvent(event)
        if not self.camera_initialized or not self.camera or not self.camera.isOpened():
            print("Window shown - initializing camera")
            self.init_camera()
    
    def hideEvent(self, event):
        """Handle when window is hidden - stop camera"""
        super().hideEvent(event)
        print("Window hidden - stopping camera")
        self.cleanup_camera()
    
    def setup_camera_display(self):
        """Setup the camera display area"""
        # If you have a specific QLabel for camera in your UI, use it
        # Otherwise, we'll look for a suitable widget or create one
        
        # Try to find existing label for camera display
        # Adjust this based on your UI structure
        if hasattr(self.ui, 'label_camera'):
            self.camera_label = self.ui.label_camera
        else:
            # Create a new label for camera display if not exists
            # You might need to adjust the parent and positioning
            self.camera_label = QLabel(self)
            self.camera_label.setGeometry(332, 190, 650, 400)  # Adjust based on your red area
            self.camera_label.setStyleSheet("border: 2px solid red; background-color: black;")
        
        self.camera_label.setAlignment(Qt.AlignCenter)
        self.camera_label.setScaledContents(True)
        self.camera_label.setText("Camera Loading...")
    
    def init_camera(self):
        """Initialize the camera"""
        try:
            # Clean up existing camera first
            if self.camera and self.camera.isOpened():
                self.camera.release()
            
            # Add small delay to ensure camera is released
            import time
            time.sleep(0.1)
            
            self.camera = cv2.VideoCapture(0)  # Use default camera
            if not self.camera.isOpened():
                raise Exception("Could not open camera")
            
            # Set camera resolution
            self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
            self.camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
            
            # Start camera feed
            self.timer.start(30)  # Update every 30ms
            self.is_capturing = True
            self.camera_initialized = True
            
            print("Camera initialized successfully")
            
        except Exception as e:
            print(f"Camera initialization error: {e}")
            self.camera_label.setText(f"Camera Error: {str(e)}")
            self.camera_initialized = False
            # QMessageBox.warning(self, "Camera Error", f"Failed to initialize camera: {str(e)}")
    
    def update_frame(self):
        """Update camera frame"""
        if self.camera and self.camera.isOpened() and self.is_capturing:
            ret, frame = self.camera.read()
            if ret:
                # Convert frame to QImage and display
                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                h, w, ch = rgb_frame.shape
                bytes_per_line = ch * w
                qt_image = QImage(rgb_frame.data, w, h, bytes_per_line, QImage.Format_RGB888)
                
                # Scale image to fit label
                pixmap = QPixmap.fromImage(qt_image)
                scaled_pixmap = pixmap.scaled(self.camera_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
                self.camera_label.setPixmap(scaled_pixmap)
    
    def capture_photo(self):
        """Capture current frame"""
        print("Capture button pressed")
        if self.camera and self.camera.isOpened():
            ret, frame = self.camera.read()
            if ret:
                self.captured_frame = frame.copy()
                self.is_capturing = False  # Stop live feed
                
                # Display captured image
                rgb_frame = cv2.cvtColor(self.captured_frame, cv2.COLOR_BGR2RGB)
                h, w, ch = rgb_frame.shape
                bytes_per_line = ch * w
                qt_image = QImage(rgb_frame.data, w, h, bytes_per_line, QImage.Format_RGB888)
                
                pixmap = QPixmap.fromImage(qt_image)
                scaled_pixmap = pixmap.scaled(self.camera_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
                self.camera_label.setPixmap(scaled_pixmap)
                
                print("Photo captured successfully")
            else:
                QMessageBox.warning(self, "Capture Error", "Failed to capture photo")
        else:
            QMessageBox.warning(self, "Camera Error", "Camera not available")
    
    def save_photo(self):
        """Save captured photo in folder named from textEdit"""
        print("Selesai button pressed")
        if self.captured_frame is None:
            QMessageBox.warning(self, "Save Error", "No photo captured. Please capture a photo first.")
            return
        
        # Get name from textEdit
        name = self.ui.textEdit.toPlainText().strip()
        if not name:
            QMessageBox.warning(self, "Save Error", "Please enter a name before saving.")
            return
        
        try:
            # Create folder with the name from textEdit
            folder_path = os.path.join("photos", name)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            
            # Generate filename with timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"{name}_{timestamp}.jpg"
            filepath = os.path.join(folder_path, filename)
            
            # Save the photo
            success = cv2.imwrite(filepath, self.captured_frame)
            
            if success:
                QMessageBox.information(self, "Save Success", f"Photo saved in folder '{name}' as: {filename}")
                print(f"Photo saved: {filepath}")
                
                # Optionally clear the form after saving
                # self.ui.textEdit.clear()
                self.reset_camera()
            else:
                QMessageBox.critical(self, "Save Error", "Failed to save photo")
                
        except Exception as e:
            print(f"Save error: {e}")
            QMessageBox.critical(self, "Save Error", f"Error saving photo: {str(e)}")
    
    def reset_camera(self):
        """Reset camera to live feed"""
        print("Reset button pressed")
        self.captured_frame = None
        
        # Clear name field
        # self.ui.textEdit.clear()
        
        # Always cleanup and reinitialize for reset
        self.cleanup_camera()
        
        # Add delay before reinitializing
        import time
        time.sleep(0.2)
        
        # Reinitialize camera
        self.init_camera()
        
        print("Camera reset completed")
    
    def back_action(self):
        """Handle back button"""
        print("Back button pressed")
        # Stop camera when leaving the window
        self.cleanup_camera()
        widget.setCurrentIndex(widget.currentIndex() - 1)
    
    def cleanup_camera(self):
        """Clean up camera resources"""
        print("Cleaning up camera resources")
        
        # Stop timer first
        if self.timer.isActive():
            self.timer.stop()
        
        # Set flags to stop capturing
        self.is_capturing = False
        
        # Release camera with proper cleanup
        if self.camera and self.camera.isOpened():
            self.camera.release()
            print("Camera released")
        
        # Set camera to None to ensure clean state
        self.camera = None
        self.camera_initialized = False
        
        # Clear the display
        if self.camera_label:
            self.camera_label.clear()
            self.camera_label.setText("Camera Stopped")
        
        # Force garbage collection to ensure cleanup
        import gc
        gc.collect()
    
    def closeEvent(self, event):
        """Handle window close event"""
        self.cleanup_camera()
        super().closeEvent(event)
    
    def testshutdown(self):
        print("button shut down pressed")

class Password(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Password()
        self.ui.setupUi(self)
        self.ui.pushButton.pressed.connect(self.back_action)
        self.ui.lineEdit.setEchoMode(QLineEdit.Password)
        self.ui.lineEdit.setPlaceholderText("Enter Password")
        self.ui.pushButton_2.pressed.connect(self.checkpassword)

    def checkpassword(self):
        if self.ui.lineEdit.text() == "admin":
            print("Password is correct")
            self.ui.lineEdit.clear()
            widget.setCurrentIndex(widget.currentIndex() + 1)
        else:
            print("Password is incorrect")
    
    def back_action(self):
        print("button start pressed")
        widget.setCurrentIndex(widget.currentIndex() - 1)

    def testshutdown(self):
        print("button shut down pressed")
        
class LogWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Log()
        self.ui.setupUi(self)
        
        table_model = MyTableModel(self, data_list, header)
        self.ui.tableView.setModel(table_model)
        font = QFont("Courier New", 20, QFont.Bold)
        self.ui.pushButton.pressed.connect(self.back_action)
        self.ui.tableView.setFont(font)
        self.ui.tableView.setFixedSize(700, 450)
        self.ui.tableView.resizeColumnsToContents()
        # self.ui.tableView.setSortingEnabled(True)
        
    def back_action(self):
        print("button start pressed")
        widget.setCurrentIndex(widget.currentIndex() - 3)
    
class MyTableModel(QAbstractTableModel):
    def __init__(self, parent, mylist, header, *args):
        QAbstractTableModel.__init__(self, parent, *args)
        self.mylist = mylist
        self.header = header

    def rowCount(self, parent):
        return len(self.mylist)

    def columnCount(self, parent):
        return len(self.mylist[0])

    def data(self, index, role):
        if not index.isValid():
            return None
        elif role != Qt.DisplayRole:
            return None
        return self.mylist[index.row()][index.column()]

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.header[col]
        return None

    def sort(self, col, order):
        """sort table by given column number col"""
        self.emit(SIGNAL("layoutAboutToBeChanged()"))
        self.mylist = sorted(self.mylist,
            key=operator.itemgetter(col))
        if order == Qt.DescendingOrder:
            self.mylist.reverse()
        self.emit(SIGNAL("layoutChanged()"))

# the solvent data ...
header = ['No','Nama', ' Tanggal/Waktu', ' Aktivitas']
# use numbers for numeric data to sort properly
data_list = [
(1, "yanto", "12 januari 25/ 11:11:11", "login"),
(2, "agus sedunia", "25 januari 25/12:12:12", "login"),
(2, "agus sedunia", "25 januari 25/12:12:12", "login"),
]


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget=QStackedWidget()
    mainwindow=MainWindow()
    mainmenu=SecondWindow()
    tambahdata=TambahData()
    password=Password()
    log=LogWindow()
    widget.addWidget(mainwindow)
    widget.addWidget(mainmenu)
    widget.addWidget(password)
    widget.addWidget(tambahdata)
    widget.addWidget(log)
    # widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
