# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainmenu.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_MainMenu(object):
    def setupUi(self, MainMenu):
        if not MainMenu.objectName():
            MainMenu.setObjectName(u"MainMenu")
        MainMenu.resize(1024, 600)
        MainMenu.setMinimumSize(QSize(1024, 600))
        MainMenu.setMaximumSize(QSize(1024, 600))
        MainMenu.setAutoFillBackground(False)
        MainMenu.setStyleSheet(u"background-image: url(:/menu/START(2) 1.png);\n"
"background-repeat: false;")
        self.centralwidget = QWidget(MainMenu)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(60, 320, 201, 201))
        self.pushButton.setStyleSheet(u"background-image: url(:/menu/Group 2.png);\n"
"background-repeat:false;\n"
"border-radius: 10;")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(300, 320, 201, 201))
        self.pushButton_2.setStyleSheet(u"background-image: url(:/menu/Group 3.png);\n"
"background-repeat:false;\n"
"border-radius: 10;")
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(540, 320, 201, 201))
        self.pushButton_3.setStyleSheet(u"background-image: url(:/menu/Group 4.png);\n"
"background-repeat:false;\n"
"border-radius: 10;")
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(780, 320, 201, 201))
        self.pushButton_4.setStyleSheet(u"background-image: url(:/menu/Group 5.png);\n"
"background-repeat:false;\n"
"border-radius: 10;")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(380, 60, 241, 191))
        self.frame.setStyleSheet(u"background-image: url(:/menu/Group 1.png);\n"
"background-repeat:false;\n"
"border-radius: 10;")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(30, 0, 80, 91))
        self.pushButton_5.setStyleSheet(u"background-image: url(:/menu/arrow 1.png);\n"
"background-repeat:false;\n"
"border-radius: 10;")
        MainMenu.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainMenu)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1024, 23))
        MainMenu.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainMenu)
        self.statusbar.setObjectName(u"statusbar")
        MainMenu.setStatusBar(self.statusbar)

        self.retranslateUi(MainMenu)

        QMetaObject.connectSlotsByName(MainMenu)
    # setupUi

    def retranslateUi(self, MainMenu):
        MainMenu.setWindowTitle(QCoreApplication.translate("MainMenu", u"MainWindow", None))
        self.pushButton.setText("")
        self.pushButton_2.setText("")
        self.pushButton_3.setText("")
        self.pushButton_4.setText("")
        self.pushButton_5.setText("")
    # retranslateUi

