# This Python file uses the following encoding: utf-8
import cv2
import os
from datetime import datetime
import sys
import ui_src
import time
import xml.etree.ElementTree as ET
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
# from PySide6.QtGui import QPixmap, QIcon
import operator
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
from ui_hapusdata import Ui_HapusData
from ui_deteksi import Ui_Deteksi
from ui_capture import Ui_CaptureWindow
from ui_preview import Ui_Preview

# Add the facedetect folder to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'facedetect'))

# Now you can import detector
import detector

name = None
aksi = None

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.pressed.connect(self.teststart)
        self.ui.pushButton_2.pressed.connect(self.testshutdown)
        self.ui.pushButton_3.pressed.connect(self.detek)

    def teststart(self):
        print("button start pressed")
        widget.setCurrentIndex(widget.currentIndex() + 1)
    def testshutdown(self):
        print("button shut down pressed")
        sys.exit(app.exec())
      
    def detek(self):
        print("button detek pressed")
        widget.setCurrentIndex(widget.currentIndex() + 6)
        print(widget.currentIndex())          
        
class SecondWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainMenu()
        self.ui.setupUi(self)
        self.ui.pushButton_5.pressed.connect(self.back_action)
        self.ui.pushButton_2.pressed.connect(self.tambahdata_action)
        self.ui.pushButton_3.pressed.connect(self.hapusdata_action)
        self.ui.pushButton_4.pressed.connect(self.capturewindow_action)
        self.ui.pushButton.pressed.connect(self.logbutton_action)
        print(widget.currentIndex())
    def capturewindow_action(self):
        print("button capture pressed")
        widget.setCurrentIndex(widget.currentIndex() + 6 )
        print(widget.currentIndex())
    def hapusdata_action(self):
        print("button delete pressed")
        widget.setCurrentIndex(widget.currentIndex() + 4 )
        print(widget.currentIndex())
    def logbutton_action(self):
        print("button log pressed")
        widget.setCurrentIndex(widget.currentIndex() + 3 )
        print(widget.currentIndex())
    def back_action(self):
        # print("button start pressed")
        widget.setCurrentIndex(widget.currentIndex() - 1)
        print(widget.currentIndex())
    def tambahdata_action(self):
        print("button shut down pressed")
        widget.setCurrentIndex(widget.currentIndex() + 1)
        print(widget.currentIndex())


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
            folder_path = os.path.join("facedetect/training", name)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            
            # Generate filename with timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"{timestamp}.jpg"
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
        detector.encode_known_faces()
        QMessageBox.information(self, "Menambahkan wajah", "menambahkan wajah ke database, silahkan tunggu...")
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

class Hapusdata(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_HapusData()
        self.ui.setupUi(self)
        self.ui.pushButton.pressed.connect(self.back_action)
        self.ui.pushButton_2.pressed.connect(self.delete_data)

    def delete_data(self):
        print("Delete button pressed")
        name = self.ui.textEdit.toPlainText().strip()
        if not name:
            QMessageBox.warning(self, "Delete Error", "Please enter a name to delete.")
            return
        
        folder_path = os.path.join("facedetect/training", name)
        if os.path.exists(folder_path):
            try:
                # Remove the folder and its contents
                import shutil
                shutil.rmtree(folder_path)
                QMessageBox.information(self, "Delete Success", f"Data for '{name}' deleted successfully.")
                print(f"Deleted folder: {folder_path}")
            except Exception as e:
                QMessageBox.critical(self, "Delete Error", f"Error deleting data: {str(e)}")
                print(f"Error deleting folder: {e}")
        else:
            QMessageBox.warning(self, "Delete Error", f"No data found for '{name}'.")

    def back_action(self):
        print("button start pressed")
        detector.encode_known_faces(model="hog")
        QMessageBox.information(self, "Menghapus wajah", "menghapus wajah dari database, silahkan tunggu...")
        widget.setCurrentIndex(widget.currentIndex() - 4)

class Deteksi(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Deteksi()
        self.ui.setupUi(self)
        
        # Connect buttons
        self.ui.pushButton_2.pressed.connect(self.back_action)
        self.ui.pushButton.pressed.connect(self.deteksi_action)  # Detection button
        
        # Camera setup
        self.camera = None
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)
        self.captured_frame = None
        self.is_capturing = False
        self.camera_initialized = False
        
        # Create target directory if it doesn't exist
        self.target_dir = "facedetect/targetface"
        os.makedirs(self.target_dir, exist_ok=True)
        
        # Setup camera display
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
        # Try to find existing label for camera display
        if hasattr(self.ui, 'label'):
            self.camera_label = self.ui.label
        elif hasattr(self.ui, 'label_camera'):
            self.camera_label = self.ui.label_camera
        else:
            # Create a new label for camera display if not exists
            self.camera_label = QLabel(self)
            self.camera_label.setGeometry(150, 100, 640, 480)  # Adjust based on your layout
            self.camera_label.setStyleSheet("border: 2px solid red; background-color: black;")
        
        self.camera_label.setAlignment(Qt.AlignCenter)
        self.camera_label.setScaledContents(True)
        self.camera_label.setText("Camera Loading...")
    
    def check_available_cameras(self):
        """Check which camera indices are available"""
        available_cameras = []
        for i in range(5):  # Check first 5 indices
            cap = cv2.VideoCapture(i)
            if cap.isOpened():
                ret, frame = cap.read()
                if ret and frame is not None:
                    available_cameras.append(i)
                    print(f"Camera {i}: Available ({frame.shape})")
                else:
                    print(f"Camera {i}: Opens but no frames")
                cap.release()
            else:
                print(f"Camera {i}: Not available")
        
        if not available_cameras:
            print("No cameras found!")
        return available_cameras
    
    def init_camera(self):
        """Initialize the camera"""
        try:
            # Clean up existing camera first
            if self.camera and self.camera.isOpened():
                self.camera.release()
            
            # Add small delay to ensure camera is released
            import time
            time.sleep(0.1)
            
            # Check for available cameras
            print("Checking available cameras...")
            available_cameras = self.check_available_cameras()
            
            if not available_cameras:
                raise Exception("No cameras detected")
            
            # Try to open the first available camera
            camera_index = available_cameras[0]
            self.camera = cv2.VideoCapture(camera_index)
            
            if not self.camera.isOpened():
                raise Exception(f"Could not open camera {camera_index}")
            
            # Set camera properties
            self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
            self.camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
            self.camera.set(cv2.CAP_PROP_BUFFERSIZE, 1)
            
            # Test camera by reading a frame
            ret, frame = self.camera.read()
            if not ret or frame is None:
                raise Exception("Camera opens but cannot read frames")
            
            # Start camera feed
            self.timer.start(30)  # Update every 30ms
            self.is_capturing = True
            self.camera_initialized = True
            
            print(f"Camera {camera_index} initialized successfully")
            
        except Exception as e:
            print(f"Camera initialization error: {e}")
            self.camera_label.setText(f"Camera Error: {str(e)}\n\nTroubleshooting:\n- Close other camera apps\n- Check camera connections\n- Try running as administrator")
            self.camera_initialized = False
            
            # Show detailed error message
            QMessageBox.warning(self, "Camera Error", 
                              f"Failed to initialize camera: {str(e)}\n\n"
                              "Troubleshooting tips:\n"
                              "1. Close other apps using the camera\n"
                              "2. Check camera connections\n"
                              "3. Try running as administrator\n"
                              "4. Check camera permissions")
    
    def update_frame(self):
        """Update camera frame"""
        if self.camera and self.camera.isOpened() and self.is_capturing:
            ret, frame = self.camera.read()
            if ret and frame is not None:
                # Store current frame for detection
                self.captured_frame = frame.copy()
                
                # Convert frame to QImage and display
                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                h, w, ch = rgb_frame.shape
                bytes_per_line = ch * w
                qt_image = QImage(rgb_frame.data, w, h, bytes_per_line, QImage.Format_RGB888)
                
                # Scale image to fit label
                pixmap = QPixmap.fromImage(qt_image)
                scaled_pixmap = pixmap.scaled(self.camera_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
                self.camera_label.setPixmap(scaled_pixmap)
            else:
                print("Failed to read frame from camera")
    
    def deteksi_action(self):
        """Save current frame when detection button is pressed"""
        
        global name, aksi
        print("Deteksi button pressed")
        
        if self.captured_frame is None:
            QMessageBox.warning(self, "Detection Error", "No camera feed available. Please ensure camera is working.")
            return
        
        try:
            # Save the current frame as target_image.jpg
            target_path = os.path.join(self.target_dir, "target_image.jpg")
            success = cv2.imwrite(target_path, self.captured_frame)
            
            if success:
                QMessageBox.information(self, "Success", f"Target image saved successfully!\nLocation: {target_path}")
                print(f"Image saved successfully to {target_path}")
                aksi, name = detector.recognize_faces(image_location=target_path)
                
                # Optional: Show captured image briefly
                self.is_capturing = False  # Stop live feed temporarily
                
                # Display captured image with border or indicator
                rgb_frame = cv2.cvtColor(self.captured_frame, cv2.COLOR_BGR2RGB)
                h, w, ch = rgb_frame.shape
                bytes_per_line = ch * w
                qt_image = QImage(rgb_frame.data, w, h, bytes_per_line, QImage.Format_RGB888)
                
                pixmap = QPixmap.fromImage(qt_image)
                scaled_pixmap = pixmap.scaled(self.camera_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
                self.camera_label.setPixmap(scaled_pixmap)
                
                widget.setCurrentIndex(widget.currentIndex() + 2 )
                # Resume live feed after 2 seconds
                # QTimer.singleShot(2000, self.resume_live_feed)
                
                widget.setCurrentIndex(widget.currentIndex() + 8)  # Move to Preview window
                
                
            else:
                QMessageBox.warning(self, "Error", "Failed to save target image!")
                print("Failed to save image")
                
        except Exception as e:
            print(f"Detection error: {e}")
            QMessageBox.critical(self, "Detection Error", f"Error saving target image: {str(e)}")
    
    def resume_live_feed(self):
        """Resume live camera feed"""
        self.is_capturing = True
        print("Resumed live camera feed")
    
    def back_action(self):
        """Handle back button press"""
        print("Back button pressed")
        # Stop camera when leaving the window
        self.cleanup_camera()
        widget.setCurrentIndex(widget.currentIndex() - 6)
    
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

class LogWindow(QMainWindow):
    def __init__(self, xml_file="log_data.xml", parent=None):
        super().__init__(parent)
        self.xml_file = xml_file
        self.ui = Ui_Log()
        self.ui.setupUi(self)
        
        # Load initial data from XML
        data_list = self.load_data_from_xml()
        
        self.table_model = MyTableModel(self, data_list, header)
        self.ui.tableView.setModel(self.table_model)
        font = QFont("Courier New", 20, QFont.Bold)
        self.ui.pushButton.pressed.connect(self.back_action)
        self.ui.pushButton_2.pressed.connect(self.refresh_data)
        self.ui.tableView.setFont(font)
        self.ui.tableView.setFixedSize(700, 450)
        self.ui.tableView.resizeColumnsToContents()
        
        # Add refresh button (optional)
        # self.add_refresh_button()
    
    def load_data_from_xml(self):
        """Load data from XML file and return as list of tuples"""
        try:
            tree = ET.parse(self.xml_file)
            root = tree.getroot()
            
            data_list = []
            for record in root.findall('record'):
                no = int(record.find('no').text) if record.find('no') is not None else 0
                nama = record.find('nama').text if record.find('nama') is not None else ""
                tanggal_waktu = record.find('tanggal_waktu').text if record.find('tanggal_waktu') is not None else ""
                aktivitas = record.find('aktivitas').text if record.find('aktivitas') is not None else ""
                
                data_list.append((no, nama, tanggal_waktu, aktivitas))
            
            return data_list
        except FileNotFoundError:
            print(f"XML file '{self.xml_file}' not found. Using default data.")
            return self.get_default_data()
        except ET.ParseError as e:
            print(f"Error parsing XML: {e}. Using default data.")
            return self.get_default_data()
        except Exception as e:
            print(f"Error loading XML: {e}. Using default data.")
            return self.get_default_data()
    
    def get_default_data(self):
        """Return default data if XML loading fails"""
        return [
            (1, "yanto", "12 januari 25/ 11:11:11", "login"),
            (2, "agus sedunia", "25 januari 25/12:12:12", "login"),
            (3, "agus sedunia", "25 januari 25/12:12:12", "login"),
        ]
    
    def refresh_data(self):
        """Reload data from XML and update the table"""
        new_data = self.load_data_from_xml()
        self.table_model.update_data(new_data)
        self.ui.tableView.resizeColumnsToContents()
        print("Data refreshed from XML")
    
    def save_data_to_xml(self, data_list):
        """Save current data to XML file"""
        try:
            root = ET.Element("logs")
            
            for record in data_list:
                record_elem = ET.SubElement(root, "record")
                
                no_elem = ET.SubElement(record_elem, "no")
                no_elem.text = str(record[0])
                
                nama_elem = ET.SubElement(record_elem, "nama")
                nama_elem.text = record[1]
                
                tanggal_elem = ET.SubElement(record_elem, "tanggal_waktu")
                tanggal_elem.text = record[2]
                
                aktivitas_elem = ET.SubElement(record_elem, "aktivitas")
                aktivitas_elem.text = record[3]
            
            tree = ET.ElementTree(root)
            tree.write(self.xml_file, encoding='utf-8', xml_declaration=True)
            print(f"Data saved to {self.xml_file}")
            
        except Exception as e:
            print(f"Error saving XML: {e}")
    
    def add_refresh_button(self):
        """Add a refresh button to manually reload XML data"""
        refresh_btn = QPushButton("Refresh Data")
        refresh_btn.clicked.connect(self.refresh_data)
        # You would need to add this to your UI layout
        
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
        return len(self.mylist[0]) if self.mylist else 0

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
    
    def update_data(self, new_data):
        """Update the model with new data"""
        self.beginResetModel()
        self.mylist = new_data
        self.endResetModel()
        
class ImageGallery(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_CaptureWindow()
        self.ui.setupUi(self)
        
        # Connect buttons
        self.ui.pushButton.pressed.connect(self.back_action)
        # self.ui.pushButton.pressed.connect(self.deteksi_action)  # Detection button
        
        # Setup the QListWidget for images
        self.setup_image_list()
        
        # Load images from folder
        self.load_images()
    
    def setup_image_list(self):
        """Configure the QListView for displaying images"""
        # Create a model for the QListView
        self.model = QStandardItemModel()
        self.ui.listView.setModel(self.model)
        
        # Set icon size (adjust as needed)
        self.ui.listView.setIconSize(QSize(200, 200))
        
        # Set grid size to accommodate icon and text
        self.ui.listView.setGridSize(QSize(240, 250))
        
        # Set flow and wrapping
        self.ui.listView.setFlow(QListView.Flow.LeftToRight)
        self.ui.listView.setWrapping(True)
        
        # Set view mode to icon mode
        self.ui.listView.setViewMode(QListView.ViewMode.IconMode)
        
        # Set resize mode
        self.ui.listView.setResizeMode(QListView.ResizeMode.Adjust)
        
        # Set spacing
        self.ui.listView.setSpacing(10)
        
        # Optional: Set selection mode
        self.ui.listView.setSelectionMode(QListView.SelectionMode.SingleSelection)
    
    def load_images(self):
        """Load images from facedetect/output_images folder - only Unknown_ prefixed images"""
        folder_path = "facedetect/output_images"
        
        # Check if folder exists
        if not os.path.exists(folder_path):
            print(f"Folder '{folder_path}' does not exist!")
            return
        
        # Clear existing items
        self.model.clear()
        
        # Supported image formats
        supported_formats = ('.png', '.jpg', '.jpeg', '.bmp', '.tiff', '.gif')
        
        # Get only image files with "Unknown_" prefix (case-insensitive)
        image_files = []
        for file in os.listdir(folder_path):
            if (file.lower().endswith(supported_formats) and 
                file.startswith("Unknown_")):
                image_files.append(file)
        
        # Sort files alphabetically
        image_files.sort(key=lambda x: x.lower())
        
        # Add images to the list widget
        for filename in image_files:
            file_path = os.path.join(folder_path, filename)
            self.add_image_item(file_path, filename)
        
        print(f"Loaded {len(image_files)} Unknown images from {folder_path}")
    
    def add_image_item(self, image_path, filename):
        """Add an image item to the QListView"""
        # Load and scale the image
        pixmap = QPixmap(image_path)
        if not pixmap.isNull():
            # Scale image to fit icon size while maintaining aspect ratio
            icon_size = self.ui.listView.iconSize()
            scaled_pixmap = pixmap.scaled(
                icon_size.width(), 
                icon_size.height(), 
                Qt.KeepAspectRatio, 
                Qt.SmoothTransformation
            )
            
            # Create QStandardItem
            item = QStandardItem()
            item.setIcon(QIcon(scaled_pixmap))
            item.setText(filename)
            
            # Store the full file path in the item data for later use
            item.setData(image_path, Qt.UserRole)
            
            # Make item non-editable
            item.setEditable(False)
            
            # Add item to model
            self.model.appendRow(item)
        else:
            print(f"Failed to load image: {image_path}")
    
    def refresh_images(self):
        """Refresh the image list (useful if images are added/removed)"""
        self.load_images()
    
    def get_selected_image_path(self):
        """Get the file path of the currently selected image"""
        current_index = self.ui.listView.currentIndex()
        if current_index.isValid():
            item = self.model.itemFromIndex(current_index)
            return item.data(Qt.UserRole)
        return None
    
    def on_image_selection_changed(self):
        """Handle image selection change (connect this to itemSelectionChanged signal if needed)"""
        selected_path = self.get_selected_image_path()
        if selected_path:
            print(f"Selected image: {selected_path}")
    
    def back_action(self):
        """Handle back button press"""
        print("Back button pressed")
        widget.setCurrentIndex(widget.currentIndex() - 6)
        
class Preview(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Preview()
        self.ui.setupUi(self)
        
        # Connect existing buttons
        # self.ui.pushButton.pressed.connect(self.teststart)
        # self.ui.pushButton_2.pressed.connect(self.testshutdown)
    
    def showEvent(self, event):
        """Override showEvent to refresh content when window is shown"""
        super().showEvent(event)
        self.refresh_preview()
    
    def refresh_preview(self):
        """Refresh all preview content"""
        self.setup_preview_image()
        self.setup_placeholders()
        # Add any other refresh logic here
        print("Preview refreshed!")  # Debug message
    
    def setup_preview_image(self):
        """Load and display the preview image"""
        image_path = "img_preview/preview.jpg"
        
        if os.path.exists(image_path):
            # Force reload the image from disk
            pixmap = QPixmap()
            pixmap.load(image_path)  # This reloads from file
            
            # Scale the image to fit the label while maintaining aspect ratio
            scaled_pixmap = pixmap.scaled(
                self.ui.preview.size(), 
                Qt.KeepAspectRatio, 
                Qt.SmoothTransformation
            )
            
            self.ui.preview.setPixmap(scaled_pixmap)
            self.ui.preview.setScaledContents(True)
        else:
            # Set placeholder text if image not found
            self.ui.preview.setText("Image not found")
            self.ui.preview.setStyleSheet("color: red; text-align: center;")
    
    def setup_placeholders(self):
        """Setup placeholder text for name and status labels"""
        # Get fresh data here - replace with your actual data source
        current_name = name #self.get_current_name()  # Your method to get current name
        current_status = aksi #self.get_current_status()  # Your method to get current status
        print(name)
        print(aksi)
        
        if hasattr(self.ui, 'Nama_dt'):
            if current_name:
                self.ui.Nama_dt.setText(current_name)
                self.ui.Nama_dt.setStyleSheet("color: white; font-style: normal;")
            else:
                self.ui.Nama_dt.setText("No name set")
                self.ui.Nama_dt.setStyleSheet("color: #888888; font-style: italic;")
        
        if hasattr(self.ui, 'Status_dt'):
            if current_status:
                if current_status.lower() == "berhasil":
                    self.ui.Status_dt.setText("Terdeteksi, membuka brankas")
                    self.ui.Status_dt.setStyleSheet("color: green; font-style: normal;")
                else:
                    self.ui.Status_dt.setText("gagal, brankas terkunci")
                    self.ui.Status_dt.setStyleSheet("color: red; font-style: normal;")
                    self.send_telegram_notification(current_name, current_status)
            else:
                self.ui.Status_dt.setText("No status set")
                self.ui.Status_dt.setStyleSheet("color: #888888; font-style: italic;")
        
        # Use QTimer for non-blocking delay instead of time.sleep()
        QTimer.singleShot(5000, self.return_to_detection)  # 5000ms = 5 seconds
    
    def return_to_detection(self):
        """Return to detection window after delay"""
        widget.setCurrentIndex(6)  # Go specifically to index 6 (detection window)
    
    def get_current_name(self):
        """Get the current name from your data source"""
        # Replace this with your actual data retrieval logic
        # For example: return self.parent().current_name if self.parent() else None
        return "Sample Name"  # Placeholder
    
    def get_current_status(self):
        """Get the current status from your data source"""
        # Replace this with your actual data retrieval logic
        # For example: return self.parent().current_status if self.parent() else None
        return "Active"  # Placeholder
    
    def send_telegram_notification(self, name, status):
        """Send Telegram notification for failed access attempt"""
        try:
            import requests
            from datetime import datetime
            
            # Your Telegram Bot Token and Chat ID
            BOT_TOKEN = "7549815599:AAEMtGbvEpTef4lOLg2_x8FYhaPvMbna9Y4"  # Replace with your actual bot token
            CHAT_ID = "1084665313"     # Replace with your actual chat ID
            
            # Create message
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            message = f"🚨 AKSES GAGAL TERDETEKSI 🚨\n\n"
            message += f"📅 Waktu: {timestamp}\n"
            message += f"👤 Nama: {name if name else 'Unknown'}\n"
            message += f"🔐 Status: {status}\n"
            message += f"⚠️ Brankas tetap terkunci untuk keamanan"
            
            # Send message
            url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
            data = {
                'chat_id': CHAT_ID,
                'text': message,
                'parse_mode': 'HTML'
            }
            
            response = requests.post(url, data=data, timeout=5)
            
            if response.status_code == 200:
                print("Telegram notification sent successfully")
            else:
                print(f"Failed to send Telegram notification: {response.status_code}")
                
        except Exception as e:
            print(f"Error sending Telegram notification: {e}")        
    
    def teststart(self):
        # Your existing test start code
        pass
    
    def testshutdown(self):
        # Your existing test shutdown code
        pass
# the solvent data ...
header = ['No','Nama', ' Tanggal/Waktu', ' Aktivitas']
# use numbers for numeric data to sort properly
# data_list = [
# (1, "yanto", "12 januari 25/ 11:11:11", "login"),
# (2, "agus sedunia", "25 januari 25/12:12:12", "login"),
# (2, "agus sedunia", "25 januari 25/12:12:12", "login"),
# ]



if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet("""
        * {
            color: white;
        }
    """)
    widget=QStackedWidget()
    mainwindow=MainWindow()
    mainmenu=SecondWindow()
    # hapusdata=Hapusdata()
    tambahdata=TambahData()
    password=Password()
    log=LogWindow()
    hapusdata=Hapusdata()
    deteksi=Deteksi()
    prev=Preview()
    capture=ImageGallery()
    widget.addWidget(mainwindow)
    widget.addWidget(mainmenu)
    widget.addWidget(password)
    widget.addWidget(tambahdata)
    widget.addWidget(log)
    widget.addWidget(hapusdata)
    widget.addWidget(deteksi)
    widget.addWidget(capture)
    widget.addWidget(prev)
    # widget = MainWindow()
    widget.show()
    # widget.showFullScreen()
    sys.exit(app.exec())
