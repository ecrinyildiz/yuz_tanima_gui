# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class Ui_kayitli_kisiler(object):
    def setupUi4(self, kayitli_kisiler):
        kayitli_kisiler.setObjectName("kayitli_kisiler")
        kayitli_kisiler.resize(538, 469)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/people.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        kayitli_kisiler.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(kayitli_kisiler)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.kisi_silme_butonu = QtWidgets.QPushButton(self.centralwidget)
        self.kisi_silme_butonu.setObjectName("kisi_silme_butonu")
        self.gridLayout.addWidget(self.kisi_silme_butonu, 2, 0, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setRowCount(1)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setObjectName("tableWidget")
        self.gridLayout.addWidget(self.tableWidget, 1, 0, 1, 1)
        self.kisi_sayisi = QtWidgets.QLabel(self.centralwidget)
        self.kisi_sayisi.setObjectName("kisi_sayisi")
        self.gridLayout.addWidget(self.kisi_sayisi, 3,0,2,2)
        kayitli_kisiler.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(kayitli_kisiler)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 538, 20))
        self.menubar.setObjectName("menubar")
        kayitli_kisiler.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(kayitli_kisiler)
        self.statusbar.setObjectName("statusbar")
        kayitli_kisiler.setStatusBar(self.statusbar)
        self.retranslateUi(kayitli_kisiler)
        self.kisi_silme_butonu.clicked.connect(self.kisi_sil)
        QtCore.QMetaObject.connectSlotsByName(kayitli_kisiler)


    def kisi_sil(self):
        connection = sqlite3.connect ( "DetectedFaces.db" )
        content = "Select * from kayitli_kisiler"
        res = connection.execute(content)
        for row in enumerate(res):
            if row[0] == self.tableWidget.currentRow():
                bilgiler = row[1]
                id = bilgiler[0]
                isim = bilgiler[1]
                soyisim = bilgiler[2]
                connection.execute("DELETE from kayitli_kisiler where id = ? and isim = ? and soyad = ?",(id,isim,soyisim))
                connection.commit()
                self.kisilere_ekle()
        connection = sqlite3.connect ( "DetectedFaces.db" )
        query = "SELECT * FROM kayitli_kisiler"
        a = connection.execute ( query )
        self.kisi_sayisi.setText("Toplam Kişi sayısı: "+str(len(a.fetchall())))


    def kisilere_ekle(self):
        connection = sqlite3.connect("DetectedFaces.db")
        query = "SELECT * FROM kayitli_kisiler"
        result = connection.execute(query)
        self.tableWidget.setRowCount(0)
        query2 = "pragma table_info(kayitli_kisiler)"
        result2 = connection.execute(query2)
        result2_= result2.fetchall()
        labels = (result2_[0][1], result2_[1][1], result2_[2][1])
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        self.tableWidget.setHorizontalHeaderLabels(labels)
        connection.close()
        

    def retranslateUi(self, kayitli_kisiler):
        connection = sqlite3.connect ( "DetectedFaces.db" )
        query = "SELECT * FROM kayitli_kisiler"
        a = connection.execute(query)

        _translate = QtCore.QCoreApplication.translate
        kayitli_kisiler.setWindowTitle(_translate("kayitli_kisiler", "Kişi Listesi"))
        self.kisi_silme_butonu.setText ( _translate ( "MainWindow", "Kişiyi Sil" ) )
        self.kisi_sayisi.setText( "Toplam Kişi sayısı: "+str(len(a.fetchall())))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    kayitli_kisiler = QtWidgets.QMainWindow()
    ui4 = Ui_kayitli_kisiler()
    ui4.setupUi4(kayitli_kisiler)
    kayitli_kisiler.show()
    sys.exit(app.exec_())

