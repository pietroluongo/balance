# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pid_adjustment.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QDial, QFrame, QGridLayout,
    QHBoxLayout, QLCDNumber, QLabel, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(879, 313)
        self.action_Salvar_ajuste = QAction(MainWindow)
        self.action_Salvar_ajuste.setObjectName(u"action_Salvar_ajuste")
        self.action_Sair = QAction(MainWindow)
        self.action_Sair.setObjectName(u"action_Sair")
        self.action_Carregar_ajuste = QAction(MainWindow)
        self.action_Carregar_ajuste.setObjectName(u"action_Carregar_ajuste")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_5 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pOuterLayout = QVBoxLayout()
        self.pOuterLayout.setObjectName(u"pOuterLayout")
        self.p_value = QLCDNumber(self.centralwidget)
        self.p_value.setObjectName(u"p_value")
        self.p_value.setAutoFillBackground(False)
        self.p_value.setFrameShape(QFrame.Box)
        self.p_value.setFrameShadow(QFrame.Raised)
        self.p_value.setSmallDecimalPoint(False)
        self.p_value.setDigitCount(5)
        self.p_value.setSegmentStyle(QLCDNumber.Filled)
        self.p_value.setProperty("value", 1.000000000000000)

        self.pOuterLayout.addWidget(self.p_value)

        self.pInnerLayout = QGridLayout()
        self.pInnerLayout.setObjectName(u"pInnerLayout")
        self.p_dial = QDial(self.centralwidget)
        self.p_dial.setObjectName(u"p_dial")
        self.p_dial.setMaximum(1000)
        self.p_dial.setValue(0)
        self.p_dial.setInvertedAppearance(False)

        self.pInnerLayout.addWidget(self.p_dial, 0, 0, 1, 1)

        self.p_label = QLabel(self.centralwidget)
        self.p_label.setObjectName(u"p_label")
        font = QFont()
        font.setFamilies([u"DejaVu Sans"])
        font.setPointSize(32)
        self.p_label.setFont(font)
        self.p_label.setScaledContents(False)
        self.p_label.setAlignment(Qt.AlignCenter)

        self.pInnerLayout.addWidget(self.p_label, 0, 1, 1, 1)


        self.pOuterLayout.addLayout(self.pInnerLayout)


        self.horizontalLayout_2.addLayout(self.pOuterLayout)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.lcdNumber_3 = QLCDNumber(self.centralwidget)
        self.lcdNumber_3.setObjectName(u"lcdNumber_3")
        self.lcdNumber_3.setAutoFillBackground(False)
        self.lcdNumber_3.setFrameShape(QFrame.Box)
        self.lcdNumber_3.setFrameShadow(QFrame.Raised)
        self.lcdNumber_3.setSmallDecimalPoint(False)
        self.lcdNumber_3.setDigitCount(5)
        self.lcdNumber_3.setSegmentStyle(QLCDNumber.Filled)
        self.lcdNumber_3.setProperty("value", 1.000000000000000)

        self.verticalLayout_4.addWidget(self.lcdNumber_3)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.dial_3 = QDial(self.centralwidget)
        self.dial_3.setObjectName(u"dial_3")

        self.gridLayout_3.addWidget(self.dial_3, 0, 0, 1, 1)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)
        self.label_6.setScaledContents(False)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_6, 0, 1, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout_3)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.lcdNumber_2 = QLCDNumber(self.centralwidget)
        self.lcdNumber_2.setObjectName(u"lcdNumber_2")
        self.lcdNumber_2.setAutoFillBackground(False)
        self.lcdNumber_2.setFrameShape(QFrame.Box)
        self.lcdNumber_2.setFrameShadow(QFrame.Raised)
        self.lcdNumber_2.setSmallDecimalPoint(False)
        self.lcdNumber_2.setDigitCount(5)
        self.lcdNumber_2.setSegmentStyle(QLCDNumber.Filled)
        self.lcdNumber_2.setProperty("value", 1.000000000000000)

        self.verticalLayout_3.addWidget(self.lcdNumber_2)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.dial_2 = QDial(self.centralwidget)
        self.dial_2.setObjectName(u"dial_2")

        self.gridLayout_2.addWidget(self.dial_2, 0, 0, 1, 1)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)
        self.label_5.setScaledContents(False)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_5, 0, 1, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout_2)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_5.addWidget(self.pushButton)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 879, 22))
        self.menu_Arquivo = QMenu(self.menubar)
        self.menu_Arquivo.setObjectName(u"menu_Arquivo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu_Arquivo.menuAction())
        self.menu_Arquivo.addAction(self.action_Salvar_ajuste)
        self.menu_Arquivo.addAction(self.action_Carregar_ajuste)
        self.menu_Arquivo.addSeparator()
        self.menu_Arquivo.addAction(self.action_Sair)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Ajuste PID", None))
        self.action_Salvar_ajuste.setText(QCoreApplication.translate("MainWindow", u"&Salvar ajuste", None))
        self.action_Sair.setText(QCoreApplication.translate("MainWindow", u"&Sair", None))
        self.action_Carregar_ajuste.setText(QCoreApplication.translate("MainWindow", u"&Carregar ajuste", None))
        self.p_label.setText(QCoreApplication.translate("MainWindow", u"P", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"I", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"D", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Enviar", None))
        self.menu_Arquivo.setTitle(QCoreApplication.translate("MainWindow", u"&Arquivo", None))
    # retranslateUi

