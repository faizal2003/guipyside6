# This Python file uses the following encoding: utf-8
import sys
import ui_src
from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow
from ui_mainmenu import Ui_MainMenu
from ui_tambahdata import Ui_TambahData

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.pressed.connect(self.teststart)
        self.ui.pushButton_2.pressed.connect(self.testshutdown)

    def teststart(self):
        print("button start pressed")
        widget.setCurrentIndex(widget.currentIndex() + 1)
    def testshutdown(self):
        print("button shut down pressed")
        sys.exit(app.exec())


class SecondWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainMenu()
        self.ui.setupUi(self)
        self.ui.pushButton_5.pressed.connect(self.back_action)
        self.ui.pushButton_2.pressed.connect(self.tambahdata_action)

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
        self.ui.pushButton.pressed.connect(self.back_action)

    def back_action(self):
        print("button start pressed")
        widget.setCurrentIndex(widget.currentIndex() - 1)

    def testshutdown(self):
        print("button shut down pressed")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget=QStackedWidget()
    mainwindow=MainWindow()
    mainmenu=SecondWindow()
    tambahdata=TambahData()
    widget.addWidget(mainwindow)
    widget.addWidget(mainmenu)
    widget.addWidget(tambahdata)
    # widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
