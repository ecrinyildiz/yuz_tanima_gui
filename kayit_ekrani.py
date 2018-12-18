# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
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

        self.ornek_sayisi_label = QtWidgets.QLabel ( self.centralwidget )
        self.ornek_sayisi_label.setObjectName ( "ornek_sayisi_label" )
        self.gridLayout.addWidget ( self.ornek_sayisi_label, 4, 0, 1, 1 )

        self.ornek_sayisi = QtWidgets.QLineEdit(self.centralwidget)
        self.ornek_sayisi.setObjectName("ornek_sayisi")
        self.gridLayout.addWidget(self.ornek_sayisi, 4, 1, 1, 2)

        self.kayit_no_label = QtWidgets.QLabel(self.centralwidget)
        self.kayit_no_label.setObjectName("kayit_no_label")
        self.gridLayout.addWidget(self.kayit_no_label, 1, 0, 1, 1)
        self.kayit_no_label2 = QtWidgets.QLabel ( self.centralwidget )
        self.kayit_no_label2.setObjectName ( "kayit_no_label2" )
        self.gridLayout.addWidget ( self.kayit_no_label2, 1, 1, 1, 1 )
        self.soyad_label = QtWidgets.QLabel(self.centralwidget)
        self.soyad_label.setObjectName("soyad_label")
        self.gridLayout.addWidget(self.soyad_label, 3, 0, 1, 1)
        self.isim_label = QtWidgets.QLabel(self.centralwidget)
        self.isim_label.setObjectName("isim_label")
        self.gridLayout.addWidget(self.isim_label, 2, 0, 1, 1)
        self.kaydet_butonu = QtWidgets.QPushButton(self.centralwidget)
        self.kaydet_butonu.setObjectName("kaydet_butonu")
        self.gridLayout.addWidget(self.kaydet_butonu, 6, 1, 1, 1)
        self.soyad_text = QtWidgets.QLineEdit(self.centralwidget)
        self.soyad_text.setObjectName("soyad_text")
        self.gridLayout.addWidget(self.soyad_text, 3, 1, 1, 1)
        self.isim_text = QtWidgets.QLineEdit(self.centralwidget)
        self.isim_text.setObjectName("isim_text")
        self.gridLayout.addWidget(self.isim_text, 2, 1, 1, 1)
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
        yeni_kayit_ekrani.setTabOrder(self.isim_text, self.soyad_text)
        yeni_kayit_ekrani.setTabOrder(self.soyad_text, self.ornek_sayisi)
        yeni_kayit_ekrani.setTabOrder(self.ornek_sayisi , self.kaydet_butonu)
        yeni_kayit_ekrani.setTabOrder(self.kaydet_butonu, self.cikis_butonu)


    def kaydet_gonder(self):
        a = c.execute ( "select * from kayitli_kisiler" )
        b =  ( len ( a.fetchall () ) + 1 )
        isim = self.isim_text.text ()
        soyad = self.soyad_text.text ()
        ornek_sayisi = int(self.ornek_sayisi.text())
        print(type(ornek_sayisi))
        msg = QMessageBox()
        Bilgileriniz = "Id no: " + str(b) + "\nİsim: " + str ( isim ) + "\nSoyisim: " + str ( soyad + "\nÖrnek sayısı: " + str(ornek_sayisi))
        msg.setText(Bilgileriniz)
        msg.setWindowTitle("Bilgileriniz")
        retval = msg.exec()
        retval
        kaydet(isim, soyad, ornek_sayisi)
        self.isim_text.setText ( "" )
        self.soyad_text.setText ( "" )
        self.ornek_sayisi.setText( "" )
        print(type(b))
        msg2 = QMessageBox ()
        msg2.setWindowTitle(" ")
        msg2.setText ( "Kayıt Başarılı." )
        retval2 = msg2.exec ()
        retval2



    def retranslateUi(self, yeni_kayit_ekrani):
        b = id_no_bul()
        _translate = QtCore.QCoreApplication.translate
        yeni_kayit_ekrani.setWindowTitle(_translate("yeni_kayit_ekrani", "Kayıt Ekranı"))
        self.label.setText(_translate("yeni_kayit_ekrani", "Kameranın önünde hafifçe kafanızı sağa ve sola doğru çeviriniz"))
        self.kayit_no_label.setText(_translate("yeni_kayit_ekrani", "Kayıt No:"))
        self.kayit_no_label2.setText ( _translate ( "yeni_kayit_ekrani", str(b) ) )
        self.soyad_label.setText(_translate("yeni_kayit_ekrani", "Soyisim:"))
        self.isim_label.setText(_translate("yeni_kayit_ekrani", "İsim:"))
        self.kaydet_butonu.setText(_translate("yeni_kayit_ekrani", "Kaydet"))
        self.cikis_butonu.setText(_translate("yeni_kayit_ekrani", "Çıkış"))
        self.ornek_sayisi_label.setText(_translate("yeni_kayit_ekrani", "Kaç adet örnek istiyorsunuz?"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    yeni_kayit_ekrani = QtWidgets.QMainWindow()
    ui2 = Kayit_Ekrani()
    ui2.setupUi2(yeni_kayit_ekrani)
    yeni_kayit_ekrani.show()
    sys.exit(app.exec_())

