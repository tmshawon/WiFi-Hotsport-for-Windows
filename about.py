# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about.ui'
#
# Created: Sat Sep  5 22:10:29 2015
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(348, 252)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icone/logo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.aboutDialog = QtGui.QWidget(Dialog)
        self.aboutDialog.setObjectName(_fromUtf8("aboutDialog"))
        self.aboutclose = QtGui.QPushButton(self.aboutDialog)
        self.aboutclose.setGeometry(QtCore.QRect(250, 180, 71, 31))
        self.aboutclose.setObjectName(_fromUtf8("aboutclose"))
        self.label = QtGui.QLabel(self.aboutDialog)
        self.label.setGeometry(QtCore.QRect(70, 20, 201, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.aboutDialog)
        self.label_2.setGeometry(QtCore.QRect(10, 200, 41, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.aboutDialog)
        self.label_3.setGeometry(QtCore.QRect(130, 50, 81, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.aboutDialog)
        self.label_4.setGeometry(QtCore.QRect(90, 70, 161, 17))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.aboutDialog)
        self.label_5.setGeometry(QtCore.QRect(90, 120, 161, 21))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.aboutDialog)
        self.label_6.setGeometry(QtCore.QRect(90, 90, 151, 17))
        self.label_6.setOpenExternalLinks(True)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.aboutDialog)
        self.label_7.setGeometry(QtCore.QRect(120, 140, 91, 20))
        self.label_7.setOpenExternalLinks(True)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout.addWidget(self.aboutDialog)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.aboutclose, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "About Hotspot", None))
        Dialog.setToolTip(_translate("Dialog", "<html><head/><body><p>About Hotspot</p></body></html>", None))
        self.aboutDialog.setToolTip(_translate("Dialog", "About Author", None))
        self.aboutclose.setToolTip(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" color:#55aa00;\">Close About</span></p></body></html>", None))
        self.aboutclose.setText(_translate("Dialog", "Close", None))
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#4285c7;\">T1G3R WIFI HOTSPOT</span></p></body></html>", None))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; color:#ca1610;\">v1.0</span></p></body></html>", None))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Created By,</span></p></body></html>", None))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">SHAID HASAN SHAWON</span></p></body></html>", None))
        self.label_5.setText(_translate("Dialog", "Copyright 2015,Team Error", None))
        self.label_6.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><a href=\"https://www.facebook.com/tmshawon\"><span style=\" text-decoration: underline; color:#0000ff;\">Contact With Author</span></a></p></body></html>", None))
        self.label_7.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><a href=\"http://teamerror.org/\"><span style=\" text-decoration: underline; color:#0000ff;\">OUR WEBSITE</span></a></p></body></html>", None))

