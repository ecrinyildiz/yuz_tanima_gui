# -*- coding: utf-8 -*-



from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap

class Ui_MainWindow(object):
    def setupUi7(self, devre_semasi):
        devre_semasi.setObjectName("Devre Şeması")
        devre_semasi.resize(1019, 478)
        self.centralwidget = QtWidgets.QWidget(devre_semasi)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        self.pic = QtWidgets.QLabel(self.centralwidget)
        self.pic.setObjectName("pic")
        self.gridLayout.addWidget(self.pic,1,1,1,1)

        devre_semasi.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(devre_semasi)
        self.statusbar.setObjectName("statusbar")
        devre_semasi.setStatusBar(self.statusbar)

        self.retranslateUi(devre_semasi)
        QtCore.QMetaObject.connectSlotsByName(devre_semasi)

    def retranslateUi(self, devre_semasi):
        _translate = QtCore.QCoreApplication.translate
        devre_semasi.setWindowTitle(_translate("MainWindow", "Devre Şeması"))
        pixmap = QPixmap("img/devre.jpg")
        self.pic.setPixmap(pixmap)




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    devre_semasi = QtWidgets.QMainWindow()
    ui7 = Ui_MainWindow()
    ui7.setupUi7(devre_semasi)
    devre_semasi.show()
    sys.exit(app.exec_())

