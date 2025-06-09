# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'log.ui'
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTableView,
    QWidget)

class Ui_Log(object):
    def setupUi(self, Log):
        if not Log.objectName():
            Log.setObjectName(u"Log")
        Log.resize(1024, 600)
        Log.setMinimumSize(QSize(1024, 600))
        Log.setMaximumSize(QSize(1024, 600))
        Log.setStyleSheet(u"background-image: url(:/menu/START(2) 1.png);\n"
"background-repeat: false;")
        self.centralwidget = QWidget(Log)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(30, 10, 81, 81))
        self.pushButton.setStyleSheet(u"background-image: url(:/menu/arrow 1.png);\n"
"background-repeat:false;\n"
"border-radius: 10;")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(330, 10, 361, 91))
        self.widget.setStyleSheet(u"background-image: url(:/password/Rectangle 2 log.png);\n"
"background-repeat: false;")
        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(150, 190, 561, 231))
        self.tableView.setStyleSheet(u"background-color: rgb(255,255,255);\n"
"gridline-color:  rgb(255, 255, 255);\n"
"color: rgb(0,0,0);")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(850, 10, 161, 61))
        Log.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Log)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1024, 23))
        Log.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Log)
        self.statusbar.setObjectName(u"statusbar")
        Log.setStatusBar(self.statusbar)

        self.retranslateUi(Log)

        QMetaObject.connectSlotsByName(Log)
    # setupUi

    def retranslateUi(self, Log):
        Log.setWindowTitle(QCoreApplication.translate("Log", u"MainWindow", None))
        self.pushButton.setText("")
        self.pushButton_2.setText(QCoreApplication.translate("Log", u"Perbarui", None))
    # retranslateUi

