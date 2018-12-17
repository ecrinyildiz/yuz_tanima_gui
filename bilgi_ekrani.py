# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_bilgi_ekrani(object):
    def setupUi5(self, bilgi_ekrani):
        bilgi_ekrani.setObjectName("bilgi_ekrani")
        bilgi_ekrani.resize(465, 126)
        bilgi_ekrani.setMouseTracking(True)
        self.centralwidget = QtWidgets.QWidget(bilgi_ekrani)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.label_3.setTextFormat(QtCore.Qt.PlainText)
        self.label_3.setScaledContents(False)
        self.label_3.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.label_3.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 1, 1, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setInputMethodHints(QtCore.Qt.ImhNone)
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setWordWrap(False)
        self.label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        bilgi_ekrani.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(bilgi_ekrani)
        self.statusbar.setObjectName("statusbar")
        bilgi_ekrani.setStatusBar(self.statusbar)

        self.retranslateUi(bilgi_ekrani)
        QtCore.QMetaObject.connectSlotsByName(bilgi_ekrani)

    def retranslateUi(self, bilgi_ekrani):
        _translate = QtCore.QCoreApplication.translate
        bilgi_ekrani.setWindowTitle(_translate("bilgi_ekrani", "Bilgi Ekranı"))
        self.label_2.setText(_translate("bilgi_ekrani", "İletişim: ecrin_3@hotmail.com"))
        self.label_3.setText(_translate("bilgi_ekrani", "Aralık 2018"))
        self.label.setText(_translate("bilgi_ekrani", "Ecrin Yıldız tarafından yapılmıştır. Her türlü kullanıma ve paylaşıma açıktır."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    bilgi_ekrani = QtWidgets.QMainWindow()
    ui5 = Ui_bilgi_ekrani()
    ui5.setupUi5(bilgi_ekrani)
    bilgi_ekrani.show()
    sys.exit(app.exec_())

