# This Python file uses the following encoding: utf-8
import sys
import ui_src
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow
from ui_mainmenu import Ui_MainMenu
from ui_tambahdata import Ui_TambahData
from ui_password import Ui_Password
from ui_log import Ui_Log



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
        self.ui.pushButton.pressed.connect(self.back_action)

    def back_action(self):
        print("button start pressed")
        widget.setCurrentIndex(widget.currentIndex() - 1)

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
        self.ui.tableView.setFont(font)
        self.ui.tableView.setFixedSize(700, 450)
        self.ui.tableView.resizeColumnsToContents()
        # self.ui.tableView.setSortingEnabled(True)
        
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
(2, "agus sedunia", "25 januari 25/12:12:12", "login"),
(2, "agus sedunia", "25 januari 25/12:12:12", "login"),
(2, "agus sedunia", "25 januari 25/12:12:12", "login"),
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
