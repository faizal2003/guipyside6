# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'deteksi.ui'
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
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_Deteksi(object):
    def setupUi(self, Deteksi):
        if not Deteksi.objectName():
            Deteksi.setObjectName(u"Deteksi")
        Deteksi.resize(1024, 600)
        Deteksi.setMinimumSize(QSize(1024, 600))
        Deteksi.setMaximumSize(QSize(1024, 600))
        Deteksi.setStyleSheet(u"background-image: url(:/menu/START(2) 1.png);")
        self.centralwidget = QWidget(Deteksi)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(140, 40, 721, 391))
        self.label.setStyleSheet(u"color: rgb(237, 51, 59);\n"
"background-color: rgb(237, 51, 59);")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(380, 460, 251, 71))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"color: rgb(46, 194, 126);")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(30, 0, 80, 91))
        self.pushButton_2.setStyleSheet(u"background-image: url(:/menu/arrow 1.png);\n"
"background-repeat:false;\n"
"border-radius: 10;")
        Deteksi.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Deteksi)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1024, 23))
        Deteksi.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Deteksi)
        self.statusbar.setObjectName(u"statusbar")
        Deteksi.setStatusBar(self.statusbar)

        self.retranslateUi(Deteksi)

        QMetaObject.connectSlotsByName(Deteksi)
    # setupUi

    def retranslateUi(self, Deteksi):
        Deteksi.setWindowTitle(QCoreApplication.translate("Deteksi", u"MainWindow", None))
        self.label.setText("")
        self.pushButton.setText(QCoreApplication.translate("Deteksi", u"Deteksi", None))
        self.pushButton_2.setText("")
    # retranslateUi

