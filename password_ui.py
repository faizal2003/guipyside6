# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'password.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_Password(object):
    def setupUi(self, Password):
        if not Password.objectName():
            Password.setObjectName(u"Password")
        Password.resize(1024, 600)
        Password.setMinimumSize(QSize(1024, 600))
        Password.setMaximumSize(QSize(1024, 600))
        Password.setStyleSheet(u"background-image: url(:/menu/START(2) 1.png);\n"
"background-repeat: false;")
        self.centralwidget = QWidget(Password)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(30, 0, 71, 81))
        self.pushButton.setStyleSheet(u"background-image: url(:/menu/arrow 1.png);\n"
"background-repeat:false;\n"
"border-radius: 10;")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(340, 180, 341, 61))
        self.label.setStyleSheet(u"background-image: url(:/password/Password.png);\n"
"color: rgb(255, 255, 255);\n"
"background-repea: false;")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(440, 380, 141, 51))
        self.pushButton_2.setStyleSheet(u"background-image: url(:/password/Rectangle 2submit.png);\n"
"background-repeat:false;\n"
"border-radius: 10;")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(280, 300, 491, 51))
        self.lineEdit.setStyleSheet(u"background-color: rgb(170, 0, 0);\n"
"color: rgb(255, 255, 255);")
        Password.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Password)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1024, 23))
        Password.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Password)
        self.statusbar.setObjectName(u"statusbar")
        Password.setStatusBar(self.statusbar)

        self.retranslateUi(Password)

        QMetaObject.connectSlotsByName(Password)
    # setupUi

    def retranslateUi(self, Password):
        Password.setWindowTitle(QCoreApplication.translate("Password", u"MainWindow", None))
        self.pushButton.setText("")
        self.label.setText("")
        self.pushButton_2.setText("")
    # retranslateUi

