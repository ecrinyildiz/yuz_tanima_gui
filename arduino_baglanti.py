# -*- coding: utf-8 -*-

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
import serial.tools.list_ports
from serial import Serial
from devre_semasi import *

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

        self.cikis_butonu = QtWidgets.QPushButton(self.centralwidget)
        self.cikis_butonu.setObjectName("cikis_butonu")
        self.gridLayout.addWidget(self.cikis_butonu, 4,1,1,1)

        self.port_listesi = QtWidgets.QComboBox(self.centralwidget)
        self.port_listesi.setObjectName("port_listesi")
        self.gridLayout.addWidget(self.port_listesi, 0, 1, 1, 1)

        self.isletim_sistemi_label = QtWidgets.QLabel(self.centralwidget)
        self.isletim_sistemi_label.setObjectName("isletim_sistemi_label")
        self.gridLayout.addWidget(self.isletim_sistemi_label, 0, 0, 1, 1)

        self.uyari_labeli = QtWidgets.QLabel ( self.centralwidget )
        self.uyari_labeli.setObjectName ( "uyari_labeli" )
        self.gridLayout.addWidget ( self.uyari_labeli, 2, 0, 1, 1 )

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
        self.devreyi_gorme_butonu.clicked.connect(self.devre_semasi_goster)
        self.kaydet_butonu.clicked.connect(self.kaydet_gonder)
        self.cikis_butonu.clicked.connect(Arduino1.hide)

        QtCore.QMetaObject.connectSlotsByName(Arduino1)
        self.portlari_getir()
        # self.uyari_labeli.setVisible(False)



    def kaydet_gonder(self):
        secim = self.port_listesi.currentText ()
        if len ( ports ) == 0:
            print ( "usb portunuzda bağlantı yok" )
            msg = QMessageBox ()
            msg.setIcon ( QMessageBox.Warning )
            msg.setText ( "Hata" )
            msg.setWindowTitle ( "Hata" )
            msg.setDetailedText ( "Olası Hata: USB bağlantısı yok." )
            msg.setStandardButtons( QMessageBox.Ok)
            msg.exec()


        else:

            print ( secim + " seçildi." )
            print(type(secim))
            arduinoyu_bagla(secim)
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle(" ")
            msg.setText("Bağlantı Başarılı.")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec()
            Arduino1.hide()



    def portlari_getir(self):
        a = (serial.tools.list_ports.comports ())
        b = 0

        for i in a:
            print(i)
            port_isimler = ( str ( a [b] ).split ( " -" ) [0] )
            self.port_listesi.addItem ( str ( port_isimler ) )
            b += 1
        if len(a) == 0:
            self.port_listesi.setEnabled(False)
            self.uyari_labeli.setVisible ( True )
        else:
            self.uyari_labeli.setVisible ( False )





    def devre_semasi_goster(self):
        ui7.setupUi7 ( devre_semasi )
        devre_semasi.show ()







    def retranslateUi(self, Arduino1):
        _translate = QtCore.QCoreApplication.translate
        Arduino1.setWindowTitle(_translate("MainWindow", "Arduino Bağlantı Ekranı"))
        self.kaydet_butonu.setText(_translate("MainWindow", "Kaydet"))
        self.isletim_sistemi_label.setText(_translate("MainWindow", "Portunuzu seçiniz: "))
        self.cikis_butonu.setText(_translate("MainWindow", "Çıkış"))
        self.devreyi_gorme_butonu.setText(_translate("MainWindow", "Devreyi görmek için tıklayınız."))
        self.uyari_labeli.setText(_translate("MainWindow", "Portunuzda bağlantı yok!"))
        myFont=QtGui.QFont()
        myFont.setBold(True)
        self.uyari_labeli.setFont(myFont)
        self.uyari_labeli.setStyleSheet('color: red')






if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Arduino1 = QtWidgets.QMainWindow()
    ui3 = Arduino()
    ui3.setupUi3(Arduino1 )
    Arduino1.show()
    sys.exit(app.exec_())

    ui7 = Ui_MainWindow ()
    ui7.setupUi7 ( devre_semasi )
    devre_semasi.show ()

