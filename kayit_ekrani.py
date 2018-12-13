# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kayit_ekrani.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5 import QtGui, QtCore
from modules import *

class Kayit_Ekrani(object):

    def setupUi2(self, yeni_kayit_ekrani):
        yeni_kayit_ekrani.setObjectName("yeni_kayit_ekrani")
        yeni_kayit_ekrani.resize(509, 234)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../icons/yeni_dosya.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        yeni_kayit_ekrani.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(yeni_kayit_ekrani)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 4, 1, 1, 1)
        self.kayit_no_label = QtWidgets.QLabel(self.centralwidget)
        self.kayit_no_label.setObjectName("kayit_no_label")
        self.gridLayout.addWidget(self.kayit_no_label, 1, 0, 1, 1)
        self.cinsiyet_label = QtWidgets.QLabel(self.centralwidget)
        self.cinsiyet_label.setObjectName("cinsiyet_label")
        self.gridLayout.addWidget(self.cinsiyet_label, 3, 0, 1, 1)
        self.isim_label = QtWidgets.QLabel(self.centralwidget)
        self.isim_label.setObjectName("isim_label")
        self.gridLayout.addWidget(self.isim_label, 2, 0, 1, 1)
        self.kaydet_butonu = QtWidgets.QPushButton(self.centralwidget)
        self.kaydet_butonu.setObjectName("kaydet_butonu")
        self.gridLayout.addWidget(self.kaydet_butonu, 6, 1, 1, 1)
        self.cinsiyet_text = QtWidgets.QLineEdit(self.centralwidget)
        self.cinsiyet_text.setObjectName("cinsiyet_text")
        self.gridLayout.addWidget(self.cinsiyet_text, 3, 1, 1, 1)
        self.isim_text = QtWidgets.QLineEdit(self.centralwidget)
        self.isim_text.setObjectName("isim_text")
        self.gridLayout.addWidget(self.isim_text, 2, 1, 1, 1)
        self.kayit_no_text = QtWidgets.QLineEdit(self.centralwidget)
        self.kayit_no_text.setObjectName("kayit_no_text")
        self.gridLayout.addWidget(self.kayit_no_text, 1, 1, 1, 1)
        self.cikis_butonu = QtWidgets.QPushButton(self.centralwidget)
        self.cikis_butonu.setObjectName("cikis_butonu")
        self.gridLayout.addWidget(self.cikis_butonu, 7, 1, 1, 1)
        yeni_kayit_ekrani.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(yeni_kayit_ekrani)
        self.statusbar.setObjectName("statusbar")
        yeni_kayit_ekrani.setStatusBar(self.statusbar)


        self.retranslateUi(yeni_kayit_ekrani)
        self.cikis_butonu.clicked.connect(yeni_kayit_ekrani.close)
        self.kaydet_butonu.clicked.connect(self.kaydet_gonder)
        QtCore.QMetaObject.connectSlotsByName(yeni_kayit_ekrani)
        yeni_kayit_ekrani.setTabOrder(self.kayit_no_text, self.isim_text)
        yeni_kayit_ekrani.setTabOrder(self.isim_text, self.cinsiyet_text)
        yeni_kayit_ekrani.setTabOrder(self.cinsiyet_text, self.kaydet_butonu)
        yeni_kayit_ekrani.setTabOrder(self.kaydet_butonu, self.cikis_butonu)


    def kaydet_gonder(self):
        id = int ( self.kayit_no_text.text () )
        isim = self.isim_text.text ()
        cinsiyet = self.cinsiyet_text.text ()
        msg = QMessageBox()
        Bilgileriniz = "Id no: " + str ( id ) + "\nİsim: " + str ( isim ) + "\nCinsiyet: " + str ( cinsiyet )
        msg.setText(Bilgileriniz)
        msg.setWindowTitle("Bilgileriniz")
        retval = msg.exec()
        retval
        kaydet(id, isim, cinsiyet)
        self.kayit_no_text.setText("")
        self.isim_text.setText ( "" )
        self.cinsiyet_text.setText ( "" )
        msg2 = QMessageBox ()
        msg2.setWindowTitle(" ")
        msg2.setText ( "Kayıt Başarılı." )
        retval2 = msg2.exec ()
        retval2



    def retranslateUi(self, yeni_kayit_ekrani):
        _translate = QtCore.QCoreApplication.translate
        yeni_kayit_ekrani.setWindowTitle(_translate("yeni_kayit_ekrani", "Kayıt Ekranı"))
        self.label.setText(_translate("yeni_kayit_ekrani", "Kameranın önünde hafifçe kafanızı sağa ve sola doğru çeviriniz"))
        self.kayit_no_label.setText(_translate("yeni_kayit_ekrani", "Kayıt No:"))
        self.cinsiyet_label.setText(_translate("yeni_kayit_ekrani", "Cinsiyet:"))
        self.isim_label.setText(_translate("yeni_kayit_ekrani", "İsim:"))
        self.kaydet_butonu.setText(_translate("yeni_kayit_ekrani", "Kaydet"))
        self.cikis_butonu.setText(_translate("yeni_kayit_ekrani", "Çıkış"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    yeni_kayit_ekrani = QtWidgets.QMainWindow()
    ui2 = Kayit_Ekrani()
    ui2.setupUi2(yeni_kayit_ekrani)
    yeni_kayit_ekrani.show()
    sys.exit(app.exec_())

