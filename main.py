#!/usr/bin/python
"""
Author   : Shaid Hasan Shawon
Facebook : www.facebook.com/tmshawon 
E-mail   : localhost200ok@gmail.com

"""

import sys
from PyQt4 import QtGui
from window import Ui_MainWindow
from about import Ui_Dialog
import os

class aboutDialog(QtGui.QDialog):
	def __init__(self):
		QtGui.QDialog.__init__(self)
		self.ui = Ui_Dialog()
		self.ui.setupUi(self)
		# self.ui.aboutclose.clicked.connect(self.aboutclose_Clicked)

	# def aboutclose_Clicked(self):
	# 	self.close()


class Main(QtGui.QMainWindow):
	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.ui.startwifi.clicked.connect(self.startwifi_clicked)
		self.ui.stopwifi.clicked.connect(self.stopwifi_clicked)
		self.ui.exitapp.clicked.connect(self.exitapp_clicked)

		self.ui.actionAbout.triggered.connect(self.actionAbout_triggered)
		self.ui.popAboutDailog = aboutDialog()

		self.ui.stopwifi.setEnabled(False)

	def startwifi_clicked(self):
		ssid = str(self.ui.wifiname.text())
		password = str(self.ui.wifipassword.text())

		if ssid == '' or password == '':
			self.ui.status.setText("Invalid Name & Password")
		else:
			os.system('netsh wlan set hostednetwork mode=allow ssid='+ssid+' key='+password+'')
			os.system('netsh wlan start hostednetwork')
			self.ui.status.setText("Hotspot Started")
			self.ui.startwifi.setEnabled(False)
			self.ui.stopwifi.setEnabled(True)


	def stopwifi_clicked(self):
		self.ui.startwifi.setEnabled(True)
		self.ui.stopwifi.setEnabled(False)
		os.system('netsh wlan stop hostednetwork')
		self.ui.status.setText("Hotspot Stopped")

	def exitapp_clicked(self):
		self.close()

	def actionAbout_triggered(self):
		self.ui.popAboutDailog.show()


if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	window = Main()
	window.setWindowTitle('T1G3R WIFI HOTSPOT')
	window.show()
	sys.exit(app.exec_())
