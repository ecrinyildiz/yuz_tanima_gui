#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from kayit_ekrani import *
from modules import *
from arduino_baglanti import *
from kisi_listesi import *
from bilgi_ekrani import *

class Ui_MainWindow(object):
    def setupUi1(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(568, 316)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.yeni_kayit_butonu = QtWidgets.QPushButton(self.centralwidget)
        self.yeni_kayit_butonu.setAutoDefault(False)
        self.yeni_kayit_butonu.setObjectName("yeni_kayit_butonu")
        self.gridLayout.addWidget(self.yeni_kayit_butonu, 0, 0, 1, 1)
        self.arduino_baglanti_butonu = QtWidgets.QPushButton(self.centralwidget)
        self.arduino_baglanti_butonu.setEnabled(True)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/arduino.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.arduino_baglanti_butonu.setIcon(icon1)
        self.arduino_baglanti_butonu.setObjectName("arduino_baglanti_butonu")
        self.gridLayout.addWidget(self.arduino_baglanti_butonu, 0, 1, 1, 1)
        self.kisileri_gosterme_butonu = QtWidgets.QPushButton(self.centralwidget)
        self.kisileri_gosterme_butonu.setEnabled(True)
        self.kisileri_gosterme_butonu.setObjectName("kisileri_gosterme_butonu")
        self.gridLayout.addWidget(self.kisileri_gosterme_butonu, 1, 1, 1, 1)

        self.veri_setini_egit_butonu = QtWidgets.QPushButton(self.centralwidget)
        self.veri_setini_egit_butonu.setObjectName("veri_setini_egit_butonu")
        self.gridLayout.addWidget(self.veri_setini_egit_butonu, 1, 0, 1, 1)


        self.yuz_tanima_butonu = QtWidgets.QPushButton(self.centralwidget)
        self.yuz_tanima_butonu.setObjectName("yuz_tanima_butonu")
        self.gridLayout.addWidget(self.yuz_tanima_butonu, 2, 0, 1, 1)
        self.cikis_butonu = QtWidgets.QPushButton(self.centralwidget)
        self.cikis_butonu.setObjectName("cikis_butonu")
        self.gridLayout.addWidget(self.cikis_butonu, 3, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 568, 22))
        self.menubar.setObjectName("menubar")
        self.menuDosya = QtWidgets.QMenu(self.menubar)
        self.menuDosya.setObjectName("menuDosya")
        self.menu_yardim = QtWidgets.QMenu(self.menubar)
        self.menu_yardim.setObjectName("menu_yardim")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setEnabled(True)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.bilgi_menu = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/help.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bilgi_menu.setIcon(icon2)
        self.bilgi_menu.setObjectName("bilgi_menu")
        self.yeni_kayit_menu = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/yeni_dosya.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.yeni_kayit_menu.setIcon(icon3)
        self.yeni_kayit_menu.setObjectName("yeni_kayit_menu")
        self.veriyi_egit_menu = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/training.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.veriyi_egit_menu.setIcon(icon4)
        self.veriyi_egit_menu.setObjectName("veriyi_egit_menu")
        self.cikis_menu = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cikis_menu.setIcon(icon5)
        self.cikis_menu.setShortcutContext(QtCore.Qt.WidgetShortcut)
        self.cikis_menu.setObjectName("cikis_menu")

        self.arduino_baglantisi = QtWidgets.QAction(MainWindow)
        self.arduino_baglantisi.setIcon(icon1)
        self.arduino_baglantisi.setObjectName("arduino_baglantisi")


        self.menuDosya.addAction(self.yeni_kayit_menu)
        self.menuDosya.addAction(self.veriyi_egit_menu)
        self.menuDosya.addAction ( self.arduino_baglantisi )
        self.menuDosya.addSeparator()
        self.menuDosya.addAction(self.cikis_menu)
        self.menu_yardim.addAction(self.bilgi_menu)
        self.menubar.addAction(self.menuDosya.menuAction())
        self.menubar.addAction(self.menu_yardim.menuAction())
        self.retranslateUi(MainWindow)
        self.yeni_kayit_butonu.clicked.connect(self.kayit_ekrani_ac)
        self.veri_setini_egit_butonu.clicked.connect(self.veri_setini_egit)
        self.yuz_tanima_butonu.clicked.connect(self.yuz_tanimayi_baslat)
        self.arduino_baglanti_butonu.clicked.connect(self.arduino_baglantisini_baslat)
        self.cikis_butonu.clicked.connect(QtCore.QCoreApplication.instance().quit)
        self.kisileri_gosterme_butonu.clicked.connect(self.kisileri_goster)
        self.yeni_kayit_menu.triggered.connect(self.kayit_ekrani_ac)
        self.bilgi_menu.triggered.connect(self.bilgi_ekrani)
        self.cikis_menu.triggered.connect(QtCore.QCoreApplication.quit)
        self.veriyi_egit_menu.triggered.connect(self.veri_setini_egit)
        self.arduino_baglantisi.triggered.connect(self.arduino_baglantisini_baslat)


        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.yeni_kayit_butonu, self.veri_setini_egit_butonu)
        MainWindow.setTabOrder(self.veri_setini_egit_butonu, self.yuz_tanima_butonu)
        MainWindow.setTabOrder(self.yuz_tanima_butonu, self.cikis_butonu)
        MainWindow.setTabOrder(self.cikis_butonu, self.arduino_baglanti_butonu)


    def kisileri_goster(self):
        ui4.setupUi4(kayitli_kisiler)
        ui4.kisilere_ekle()
        kayitli_kisiler.show()


    def kayit_ekrani_ac(self):
        ui2.setupUi2(yeni_kayit_ekrani)
        yeni_kayit_ekrani.show()


    def veri_setini_egit(self):
        training()


    def yuz_tanimayi_baslat(self):
        detect()


    def arduino_baglantisini_baslat(self):
        ui3.setupUi3(Arduino1)
        Arduino1.show()

    def bilgi_ekrani(self):
        ui5.setupUi5 ( bilgi_ekrani )
        bilgi_ekrani.show ()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Yüz Tanıma Sistemi"))
        self.yeni_kayit_butonu.setText(_translate("MainWindow", "Yeni Kayıt"))
        self.arduino_baglanti_butonu.setText(_translate("MainWindow", "Arduino Bağlantısı"))
        self.kisileri_gosterme_butonu.setText(_translate("MainWindow", "Kişi Listesi"))
        self.veri_setini_egit_butonu.setText(_translate("MainWindow", "Veri Setini Eğit"))
        self.yuz_tanima_butonu.setText(_translate("MainWindow", "Yüz Tanımayı Başlat"))
        self.cikis_butonu.setText(_translate("MainWindow", "Çıkış"))
        self.menuDosya.setTitle(_translate("MainWindow", "Dosya"))
        self.menu_yardim.setTitle(_translate("MainWindow", "Yardım"))
        self.bilgi_menu.setText(_translate("MainWindow", "Bilgi"))
        self.bilgi_menu.setShortcut(_translate("MainWindow", "Ctrl+H"))
        self.yeni_kayit_menu.setText(_translate("MainWindow", "Yeni Kayıt"))
        self.yeni_kayit_menu.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.veriyi_egit_menu.setText(_translate("MainWindow", "Veriyi Eğit"))
        self.veriyi_egit_menu.setShortcut(_translate("MainWindow", "Ctrl+T"))
        self.cikis_menu.setText(_translate("MainWindow", "Çıkış"))
        self.cikis_menu.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.arduino_baglantisi.setText(_translate("MainWindow", "Arduino Bağlantısı"))
        self.arduino_baglantisi.setShortcut(_translate("MainWindow", "Ctrl+R"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)


    yeni_kayit_ekrani = QtWidgets.QMainWindow ()
    ui2 = Kayit_Ekrani ()
    ui2.setupUi2 ( yeni_kayit_ekrani )

    Arduino1 = QtWidgets.QMainWindow ()
    ui3 = Arduino ()
    ui3.setupUi3 ( Arduino1 )

    bilgi_ekrani = QtWidgets.QMainWindow ()
    ui5 = Ui_bilgi_ekrani ()
    ui5.setupUi5 ( bilgi_ekrani )

    kayitli_kisiler = QtWidgets.QMainWindow ()
    ui4 = Ui_kayitli_kisiler ()
    ui4.setupUi4 ( kayitli_kisiler )

    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi1(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    
