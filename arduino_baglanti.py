# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'arduino_baglanti.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import serial.tools.list_ports
from modules import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5 import QtGui, QtCore

class Arduino(object):

    def setupUi3(self, Arduino1):
        Arduino1.setObjectName("MainWindow")
        Arduino1.resize(390, 229)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../icons/arduino.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Arduino1.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(Arduino1)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        self.kaydet_butonu = QtWidgets.QPushButton(self.centralwidget)
        self.kaydet_butonu.setObjectName("kaydet_butonu")
        self.gridLayout.addWidget(self.kaydet_butonu, 3, 1, 1, 1)

        self.isletim_sistemi_label = QtWidgets.QLabel(self.centralwidget)
        self.isletim_sistemi_label.setObjectName("isletim_sistemi_label")
        self.gridLayout.addWidget(self.isletim_sistemi_label, 0, 0, 1, 1)

        self.windows_butonu = QtWidgets.QRadioButton(self.centralwidget)
        self.windows_butonu.setObjectName("windows_butonu")
        self.gridLayout.addWidget(self.windows_butonu, 0, 1, 1, 1)
        self.windows_butonu.toggled.connect(lambda: self.kaydet_gonder(self.windows_butonu))

        self.linux_butonu = QtWidgets.QRadioButton(self.centralwidget)
        self.linux_butonu.setObjectName("linux_butonu")
        self.gridLayout.addWidget(self.linux_butonu, 0, 2, 1, 1)
        self.linux_butonu.toggled.connect(lambda: self.kaydet_gonder(self.linux_butonu))

        self.devreyi_gorme_butonu = QtWidgets.QPushButton(self.centralwidget)
        self.devreyi_gorme_butonu.setObjectName("devreyi_gorme_butonu")
        self.gridLayout.addWidget(self.devreyi_gorme_butonu, 3, 0, 1, 1)

        Arduino1.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Arduino1)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 390, 22))
        self.menubar.setObjectName("menubar")
        Arduino1.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Arduino1)
        self.statusbar.setObjectName("statusbar")
        Arduino1.setStatusBar(self.statusbar)


        self.retranslateUi(Arduino1)
        self.kaydet_butonu.clicked.connect(Arduino1.hide)
        self.devreyi_gorme_butonu.clicked.connect(self.devre_semasi_goster)
        QtCore.QMetaObject.connectSlotsByName(Arduino1)


    def kaydet_gonder(self, b):
        if len ( ports ) == 0:
            print ( "usb portunuzda bağlantı yok" )
        else:

            if b.text () == "Linux":
                if b.isChecked () == True:
                    print ( b.text () + " seçildi." )
                    secim = "1"
                    arduinoyu_bagla(secim)


            if b.text () == "Windows":
                if b.isChecked () == True:
                    print ( b.text () + " seçildi." )
                    secim = "2"
                    arduinoyu_bagla(secim)




    def devre_semasi_goster(self):
        pass

    def retranslateUi(self, Arduino1):
        _translate = QtCore.QCoreApplication.translate
        Arduino1.setWindowTitle(_translate("MainWindow", "Arduino Bağlantı Ekranı"))
        self.kaydet_butonu.setText(_translate("MainWindow", "Kaydet"))
        self.isletim_sistemi_label.setText(_translate("MainWindow", "İşletim Sisteminizi seçiniz."))
        self.windows_butonu.setText(_translate("MainWindow", "Windows"))
        self.linux_butonu.setText(_translate("MainWindow", "Linux"))
        self.devreyi_gorme_butonu.setText(_translate("MainWindow", "Devreyi görmek için tıklayınız."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Arduino1 = QtWidgets.QMainWindow()
    ui3 = Arduino()
    ui3.setupUi3(Arduino1 )
    Arduino1.show()
    sys.exit(app.exec_())

