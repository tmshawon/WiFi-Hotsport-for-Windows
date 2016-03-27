# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created: Sat Sep  5 22:25:25 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(426, 277)
        MainWindow.setMinimumSize(QtCore.QSize(426, 277))
        MainWindow.setMaximumSize(QtCore.QSize(426, 277))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("logo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.wifiname = QtGui.QLineEdit(self.widget)
        self.wifiname.setGeometry(QtCore.QRect(50, 50, 311, 31))
        self.wifiname.setCursorPosition(0)
        self.wifiname.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.wifiname.setObjectName(_fromUtf8("wifiname"))
        self.wifipassword = QtGui.QLineEdit(self.widget)
        self.wifipassword.setGeometry(QtCore.QRect(50, 90, 311, 31))
        self.wifipassword.setObjectName(_fromUtf8("wifipassword"))
        self.startwifi = QtGui.QPushButton(self.widget)
        self.startwifi.setGeometry(QtCore.QRect(50, 130, 91, 41))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("start.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.startwifi.setIcon(icon1)
        self.startwifi.setCheckable(False)
        self.startwifi.setChecked(False)
        self.startwifi.setAutoRepeat(False)
        self.startwifi.setAutoExclusive(False)
        self.startwifi.setAutoDefault(True)
        self.startwifi.setDefault(False)
        self.startwifi.setFlat(False)
        self.startwifi.setObjectName(_fromUtf8("startwifi"))
        self.stopwifi = QtGui.QPushButton(self.widget)
        self.stopwifi.setGeometry(QtCore.QRect(160, 130, 91, 41))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("stop.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stopwifi.setIcon(icon2)
        self.stopwifi.setObjectName(_fromUtf8("stopwifi"))
        self.exitapp = QtGui.QPushButton(self.widget)
        self.exitapp.setGeometry(QtCore.QRect(270, 130, 91, 41))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("exit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exitapp.setIcon(icon3)
        self.exitapp.setObjectName(_fromUtf8("exitapp"))
        self.label = QtGui.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(50, 0, 301, 41))
        self.label.setObjectName(_fromUtf8("label"))
        self.status = QtGui.QLabel(self.widget)
        self.status.setGeometry(QtCore.QRect(50, 180, 261, 21))
        self.status.setText(_fromUtf8(""))
        self.status.setObjectName(_fromUtf8("status"))
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(330, 180, 31, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.widget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 426, 27))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.menuFile.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.actionQuit, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "T1G3R WIFI HOTSPOT", None))
        self.wifiname.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#55aa00;\">Any Name</span></p></body></html>", None))
        self.wifiname.setPlaceholderText(_translate("MainWindow", "WiFi Name", None))
        self.wifipassword.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#00aa00;\">Password Minimum 8 characters</span></p></body></html>", None))
        self.wifipassword.setPlaceholderText(_translate("MainWindow", "WiFi Password", None))
        self.startwifi.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#55aa00;\">Start WiFi</span></p></body></html>", None))
        self.startwifi.setText(_translate("MainWindow", "START", None))
        self.stopwifi.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#55aa00;\">Stop WiFI</span></p></body></html>", None))
        self.stopwifi.setText(_translate("MainWindow", "STOP", None))
        self.exitapp.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#55aa00;\">Quit App</span></p></body></html>", None))
        self.exitapp.setText(_translate("MainWindow", "EXIT", None))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#0079b6;\">T1G3R WIFI HOTSPOT</span></p></body></html>", None))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#e20f0f;\">V1.0</span></p></body></html>", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.actionQuit.setText(_translate("MainWindow", "Quit", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))

