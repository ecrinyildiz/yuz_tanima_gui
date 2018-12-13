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
        # self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        # self.pushButton.setObjectName("pushButton")
        # self.gridLayout.addWidget(self.pushButton, 2, 0, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setRowCount(1)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setObjectName("tableWidget")
        self.gridLayout.addWidget(self.tableWidget, 1, 0, 1, 1)
        kayitli_kisiler.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(kayitli_kisiler)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 538, 20))
        self.menubar.setObjectName("menubar")
        kayitli_kisiler.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(kayitli_kisiler)
        self.statusbar.setObjectName("statusbar")
        kayitli_kisiler.setStatusBar(self.statusbar)

        self.retranslateUi(kayitli_kisiler)
        # self.pushButton.clicked.connect(self.kisilere_ekle)
        QtCore.QMetaObject.connectSlotsByName(kayitli_kisiler)

    def kisilere_ekle(self):
        connection = sqlite3.connect("DetectedFaces.db")
        query = "SELECT * FROM isimler"
        result = connection.execute(query)
        self.tableWidget.setRowCount(0)
        query2 = "pragma table_info(isimler)"
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
        _translate = QtCore.QCoreApplication.translate
        kayitli_kisiler.setWindowTitle(_translate("kayitli_kisiler", "Kişi Listesi"))
        # self.pushButton.setText(_translate("kayitli_kisiler", "Kişileri Göster"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    kayitli_kisiler = QtWidgets.QMainWindow()
    ui4 = Ui_kayitli_kisiler()
    ui4.setupUi(kayitli_kisiler)
    kayitli_kisiler.show()
    sys.exit(app.exec_())

