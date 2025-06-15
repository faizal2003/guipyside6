# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'capture.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QListView, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_CaptureWindow(object):
    def setupUi(self, CaptureWindow):
        if not CaptureWindow.objectName():
            CaptureWindow.setObjectName(u"CaptureWindow")
        CaptureWindow.resize(1024, 600)
        CaptureWindow.setMinimumSize(QSize(1024, 600))
        CaptureWindow.setMaximumSize(QSize(1024, 600))
        CaptureWindow.setStyleSheet(u"background-image: url(:/menu/START(2) 1.png);")
        self.centralwidget = QWidget(CaptureWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(340, 20, 331, 81))
        self.frame.setMinimumSize(QSize(0, 0))
        self.frame.setMaximumSize(QSize(811, 181))
        self.frame.setStyleSheet(u"background-image: url(:/menu/Untitled.png);\n"
"background-repeat:false;\n"
"border-radius: 10;")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.listView = QListView(self.centralwidget)
        self.listView.setObjectName(u"listView")
        self.listView.setGeometry(QRect(110, 100, 771, 431))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(30, 0, 91, 80))
        self.pushButton.setStyleSheet(u"background-image: url(:/menu/arrow 1.png);\n"
"background-repeat:false;\n"
"border-radius: 10;")
        CaptureWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(CaptureWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1024, 23))
        CaptureWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(CaptureWindow)
        self.statusbar.setObjectName(u"statusbar")
        CaptureWindow.setStatusBar(self.statusbar)

        self.retranslateUi(CaptureWindow)

        QMetaObject.connectSlotsByName(CaptureWindow)
    # setupUi

    def retranslateUi(self, CaptureWindow):
        CaptureWindow.setWindowTitle(QCoreApplication.translate("CaptureWindow", u"MainWindow", None))
        self.pushButton.setText("")
    # retranslateUi

