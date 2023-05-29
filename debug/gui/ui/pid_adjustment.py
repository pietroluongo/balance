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
        MainWindow.resize(879, 243)
        self.action_Salvar_ajuste = QAction(MainWindow)
        self.action_Salvar_ajuste.setObjectName(u"action_Salvar_ajuste")
        self.action_Sair = QAction(MainWindow)
        self.action_Sair.setObjectName(u"action_Sair")
        self.action_Carregar_ajuste = QAction(MainWindow)
        self.action_Carregar_ajuste.setObjectName(u"action_Carregar_ajuste")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
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
        self.p_dial.setSingleStep(10)
        self.p_dial.setPageStep(100)
        self.p_dial.setValue(0)
        self.p_dial.setInvertedAppearance(False)
        self.p_dial.setNotchTarget(0.000000000000000)
        self.p_dial.setNotchesVisible(True)

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


        self.horizontalLayout.addLayout(self.pOuterLayout)

        self.iOuterLayout = QVBoxLayout()
        self.iOuterLayout.setObjectName(u"iOuterLayout")
        self.i_value = QLCDNumber(self.centralwidget)
        self.i_value.setObjectName(u"i_value")
        self.i_value.setAutoFillBackground(False)
        self.i_value.setFrameShape(QFrame.Box)
        self.i_value.setFrameShadow(QFrame.Raised)
        self.i_value.setSmallDecimalPoint(False)
        self.i_value.setDigitCount(5)
        self.i_value.setSegmentStyle(QLCDNumber.Filled)
        self.i_value.setProperty("value", 1.000000000000000)

        self.iOuterLayout.addWidget(self.i_value)

        self.iInnerLayout = QGridLayout()
        self.iInnerLayout.setObjectName(u"iInnerLayout")
        self.i_dial = QDial(self.centralwidget)
        self.i_dial.setObjectName(u"i_dial")
        self.i_dial.setMaximum(1000)
        self.i_dial.setSingleStep(10)
        self.i_dial.setPageStep(100)
        self.i_dial.setValue(0)
        self.i_dial.setInvertedAppearance(False)
        self.i_dial.setNotchTarget(0.000000000000000)
        self.i_dial.setNotchesVisible(True)

        self.iInnerLayout.addWidget(self.i_dial, 0, 0, 1, 1)

        self.i_label = QLabel(self.centralwidget)
        self.i_label.setObjectName(u"i_label")
        self.i_label.setFont(font)
        self.i_label.setScaledContents(False)
        self.i_label.setAlignment(Qt.AlignCenter)

        self.iInnerLayout.addWidget(self.i_label, 0, 1, 1, 1)


        self.iOuterLayout.addLayout(self.iInnerLayout)


        self.horizontalLayout.addLayout(self.iOuterLayout)

        self.dOuterLayout = QVBoxLayout()
        self.dOuterLayout.setObjectName(u"dOuterLayout")
        self.d_value = QLCDNumber(self.centralwidget)
        self.d_value.setObjectName(u"d_value")
        self.d_value.setAutoFillBackground(False)
        self.d_value.setFrameShape(QFrame.Box)
        self.d_value.setFrameShadow(QFrame.Raised)
        self.d_value.setSmallDecimalPoint(False)
        self.d_value.setDigitCount(5)
        self.d_value.setSegmentStyle(QLCDNumber.Filled)
        self.d_value.setProperty("value", 1.000000000000000)

        self.dOuterLayout.addWidget(self.d_value)

        self.dInnerLayout = QGridLayout()
        self.dInnerLayout.setObjectName(u"dInnerLayout")
        self.d_dial = QDial(self.centralwidget)
        self.d_dial.setObjectName(u"d_dial")
        self.d_dial.setMaximum(1000)
        self.d_dial.setSingleStep(10)
        self.d_dial.setPageStep(100)
        self.d_dial.setValue(0)
        self.d_dial.setInvertedAppearance(False)
        self.d_dial.setNotchTarget(0.000000000000000)
        self.d_dial.setNotchesVisible(True)

        self.dInnerLayout.addWidget(self.d_dial, 0, 0, 1, 1)

        self.d_label = QLabel(self.centralwidget)
        self.d_label.setObjectName(u"d_label")
        self.d_label.setFont(font)
        self.d_label.setScaledContents(False)
        self.d_label.setAlignment(Qt.AlignCenter)

        self.dInnerLayout.addWidget(self.d_label, 0, 1, 1, 1)


        self.dOuterLayout.addLayout(self.dInnerLayout)


        self.horizontalLayout.addLayout(self.dOuterLayout)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.send_m0_btn = QPushButton(self.centralwidget)
        self.send_m0_btn.setObjectName(u"send_m0_btn")

        self.horizontalLayout_2.addWidget(self.send_m0_btn)

        self.send_m1_btn = QPushButton(self.centralwidget)
        self.send_m1_btn.setObjectName(u"send_m1_btn")

        self.horizontalLayout_2.addWidget(self.send_m1_btn)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

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
        self.i_label.setText(QCoreApplication.translate("MainWindow", u"I", None))
        self.d_label.setText(QCoreApplication.translate("MainWindow", u"D", None))
        self.send_m0_btn.setText(QCoreApplication.translate("MainWindow", u"Enviar", None))
        self.send_m1_btn.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menu_Arquivo.setTitle(QCoreApplication.translate("MainWindow", u"&Arquivo", None))
    # retranslateUi

