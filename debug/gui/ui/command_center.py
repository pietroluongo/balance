# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'command-center.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(320, 240)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.motor_control = QPushButton(self.centralwidget)
        self.motor_control.setObjectName(u"motor_control")

        self.verticalLayout.addWidget(self.motor_control)

        self.pid_adjust = QPushButton(self.centralwidget)
        self.pid_adjust.setObjectName(u"pid_adjust")

        self.verticalLayout.addWidget(self.pid_adjust)

        self.console = QPushButton(self.centralwidget)
        self.console.setObjectName(u"console")

        self.verticalLayout.addWidget(self.console)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 320, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Centro de Comando", None))
        self.motor_control.setText(QCoreApplication.translate("MainWindow", u"Controle do Motor", None))
        self.pid_adjust.setText(QCoreApplication.translate("MainWindow", u"Ajuste PID", None))
        self.console.setText(QCoreApplication.translate("MainWindow", u"Console", None))
    # retranslateUi

