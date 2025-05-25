# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tambahdata.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTextEdit,
    QWidget)

class Ui_TambahData(object):
    def setupUi(self, TambahData):
        if not TambahData.objectName():
            TambahData.setObjectName(u"TambahData")
        TambahData.resize(1024, 600)
        TambahData.setMinimumSize(QSize(1024, 600))
        TambahData.setMaximumSize(QSize(1024, 600))
        TambahData.setStyleSheet(u"background-image: url(:/menu/START(2) 1.png);\n"
"background-repeat: false;")
        self.centralwidget = QWidget(TambahData)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(30, 0, 80, 91))
        self.pushButton.setStyleSheet(u"background-image: url(:/menu/arrow 1.png);\n"
"background-repeat:false;\n"
"border-radius: 10;")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(50, 390, 211, 51))
        self.pushButton_2.setStyleSheet(u"background-image: url(:/tambahdata/Group 3tambahdata.png);\n"
"background-repeat:false;\n"
"border-radius: 10;")
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(50, 470, 211, 51))
        self.pushButton_3.setStyleSheet(u"background-image: url(:/tambahdata/Group 1 (1).png);\n"
"background-repeat:false;\n"
"border-radius: 10;")
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(910, 0, 71, 81))
        self.pushButton_4.setStyleSheet(u"background-image: url(:/tambahdata/reset 1.png);\n"
"background-repeat:false;\n"
"border-radius: 10;")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 120, 81, 31))
        self.label.setStyleSheet(u"background-image: url(:/tambahdata/Nama.png);\n"
"background-repeat:false;\n"
"")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 200, 211, 41))
        self.label_2.setStyleSheet(u"background-image: url(:/tambahdata/Ambil Gambar.png);\n"
"background-repeat:false;\n"
"")
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(330, 110, 651, 51))
        self.textEdit.setStyleSheet(u"background-color: rgb(237, 51, 59);")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(330, 190, 651, 341))
        self.widget.setStyleSheet(u"background-color: rgb(170, 0, 0);")
        self.label_camera = QLabel(self.widget)
        self.label_camera.setObjectName(u"label_camera")
        self.label_camera.setGeometry(QRect(5, 7, 641, 331))
        TambahData.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(TambahData)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1024, 23))
        TambahData.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(TambahData)
        self.statusbar.setObjectName(u"statusbar")
        TambahData.setStatusBar(self.statusbar)

        self.retranslateUi(TambahData)

        QMetaObject.connectSlotsByName(TambahData)
    # setupUi

    def retranslateUi(self, TambahData):
        TambahData.setWindowTitle(QCoreApplication.translate("TambahData", u"MainWindow", None))
        self.pushButton.setText("")
        self.pushButton_2.setText("")
        self.pushButton_3.setText("")
        self.pushButton_4.setText("")
        self.label.setText("")
        self.label_2.setText("")
        self.label_camera.setText("")
    # retranslateUi

