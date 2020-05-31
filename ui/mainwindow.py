# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(429, 268)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.myViewer = QtWidgets.QTabWidget(self.centralwidget)
        self.myViewer.setObjectName("myViewer")
        self.temperature = QtWidgets.QWidget()
        self.temperature.setObjectName("temperature")
        self.temperature_text = QtWidgets.QLabel(self.temperature)
        self.temperature_text.setGeometry(QtCore.QRect(30, 0, 371, 121))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.temperature_text.setFont(font)
        self.temperature_text.setObjectName("temperature_text")
        self.myViewer.addTab(self.temperature, "")
        self.pressure = QtWidgets.QWidget()
        self.pressure.setObjectName("pressure")
        self.pressure_text = QtWidgets.QLabel(self.pressure)
        self.pressure_text.setGeometry(QtCore.QRect(30, 0, 371, 121))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.pressure_text.setFont(font)
        self.pressure_text.setObjectName("pressure_text")
        self.myViewer.addTab(self.pressure, "")
        self.humidity = QtWidgets.QWidget()
        self.humidity.setObjectName("humidity")
        self.humidity_text = QtWidgets.QLabel(self.humidity)
        self.humidity_text.setGeometry(QtCore.QRect(30, 0, 371, 121))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.humidity_text.setFont(font)
        self.humidity_text.setObjectName("humidity_text")
        self.myViewer.addTab(self.humidity, "")
        self.verticalLayout.addWidget(self.myViewer)
        self.read = QtWidgets.QPushButton(self.centralwidget)
        self.read.setObjectName("read")
        self.verticalLayout.addWidget(self.read)
        self.button = QtWidgets.QPushButton(self.centralwidget)
        self.button.setObjectName("button")
        self.verticalLayout.addWidget(self.button)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 429, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.myViewer.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.temperature_text.setText(_translate("MainWindow", "None"))
        self.myViewer.setTabText(self.myViewer.indexOf(self.temperature), _translate("MainWindow", "Temperature"))
        self.pressure_text.setText(_translate("MainWindow", "None"))
        self.myViewer.setTabText(self.myViewer.indexOf(self.pressure), _translate("MainWindow", "Pressure"))
        self.humidity_text.setText(_translate("MainWindow", "None"))
        self.myViewer.setTabText(self.myViewer.indexOf(self.humidity), _translate("MainWindow", "Humidity"))
        self.read.setText(_translate("MainWindow", "Read"))
        self.button.setText(_translate("MainWindow", "PushButton"))

