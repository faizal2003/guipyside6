# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'hapusdata.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTextEdit, QWidget)

class Ui_HapusData(object):
    def setupUi(self, HapusData):
        if not HapusData.objectName():
            HapusData.setObjectName(u"HapusData")
        HapusData.resize(1024, 600)
        HapusData.setMinimumSize(QSize(1024, 600))
        HapusData.setMaximumSize(QSize(1024, 600))
        HapusData.setStyleSheet(u"background-image: url(:/menu/START(2) 1.png);")
        self.centralwidget = QWidget(HapusData)
        self.centralwidget.setObjectName(u"centralwidget")
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(320, 270, 391, 41))
        self.textEdit.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(420, 360, 191, 61))
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(u"background-color: rgb(237, 51, 59);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(410, 20, 191, 191))
        self.frame.setStyleSheet(u"background-image: url(:/menu/Group 4.png);\n"
"background-repeat:false;\n"
"border-radius: 10;")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(200, 270, 101, 31))
        font1 = QFont()
        font1.setPointSize(21)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(30, 0, 80, 91))
        self.pushButton.setStyleSheet(u"background-image: url(:/menu/arrow 1.png);\n"
"background-repeat:false;\n"
"border-radius: 10;")
        HapusData.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(HapusData)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1024, 23))
        HapusData.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(HapusData)
        self.statusbar.setObjectName(u"statusbar")
        HapusData.setStatusBar(self.statusbar)

        self.retranslateUi(HapusData)

        QMetaObject.connectSlotsByName(HapusData)
    # setupUi

    def retranslateUi(self, HapusData):
        HapusData.setWindowTitle(QCoreApplication.translate("HapusData", u"MainWindow", None))
        self.pushButton_2.setText(QCoreApplication.translate("HapusData", u"Hapus", None))
        self.label.setText(QCoreApplication.translate("HapusData", u" Nama :", None))
        self.pushButton.setText("")
    # retranslateUi

