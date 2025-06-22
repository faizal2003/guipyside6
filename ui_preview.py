# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'preview.ui'
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
    QSizePolicy, QStatusBar, QWidget)

class Ui_Preview(object):
    def setupUi(self, Preview):
        if not Preview.objectName():
            Preview.setObjectName(u"Preview")
        Preview.resize(1024, 600)
        Preview.setMinimumSize(QSize(1024, 600))
        Preview.setMaximumSize(QSize(1024, 600))
        font = QFont()
        font.setBold(False)
        Preview.setFont(font)
        Preview.setStyleSheet(u"background-image: url(:/bg/START 1.png);")
        self.centralwidget = QWidget(Preview)
        self.centralwidget.setObjectName(u"centralwidget")
        self.preview = QLabel(self.centralwidget)
        self.preview.setObjectName(u"preview")
        self.preview.setGeometry(QRect(220, 20, 611, 321))
        self.preview.setStyleSheet(u"")
        self.Nama = QLabel(self.centralwidget)
        self.Nama.setObjectName(u"Nama")
        self.Nama.setGeometry(QRect(210, 390, 91, 41))
        font1 = QFont()
        font1.setPointSize(19)
        font1.setBold(True)
        self.Nama.setFont(font1)
        self.Nama.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);")
        self.Nama_dt = QLabel(self.centralwidget)
        self.Nama_dt.setObjectName(u"Nama_dt")
        self.Nama_dt.setGeometry(QRect(330, 390, 391, 41))
        self.Nama_dt.setFont(font1)
        self.Nama_dt.setStyleSheet(u"")
        self.Status = QLabel(self.centralwidget)
        self.Status.setObjectName(u"Status")
        self.Status.setGeometry(QRect(210, 460, 91, 31))
        self.Status.setFont(font1)
        self.Status_dt = QLabel(self.centralwidget)
        self.Status_dt.setObjectName(u"Status_dt")
        self.Status_dt.setGeometry(QRect(330, 450, 391, 41))
        self.Status_dt.setFont(font1)
        self.Status_dt.setStyleSheet(u"")
        Preview.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Preview)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1024, 23))
        Preview.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Preview)
        self.statusbar.setObjectName(u"statusbar")
        Preview.setStatusBar(self.statusbar)

        self.retranslateUi(Preview)

        QMetaObject.connectSlotsByName(Preview)
    # setupUi

    def retranslateUi(self, Preview):
        Preview.setWindowTitle(QCoreApplication.translate("Preview", u"MainWindow", None))
        self.preview.setText("")
        self.Nama.setText(QCoreApplication.translate("Preview", u"Nama: ", None))
        self.Nama_dt.setText("")
        self.Status.setText(QCoreApplication.translate("Preview", u"Status: ", None))
        self.Status_dt.setText("")
    # retranslateUi

