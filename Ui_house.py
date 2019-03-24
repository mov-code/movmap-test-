# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'J:\PYQT\第一测试\house.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        Dialog.setSizeGripEnabled(True)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(140, 20, 131, 20))
        self.label.setObjectName("label")
        self.gtwhois = QtWidgets.QPushButton(Dialog)
        self.gtwhois.setGeometry(QtCore.QRect(50, 100, 75, 23))
        self.gtwhois.setObjectName("gtwhois")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(50, 200, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(250, 100, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(250, 200, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")

        self.retranslateUi(Dialog)
        self.gtwhois.clicked.connect(Dialog.hide)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "欢迎使用MOVMAP"))
        self.gtwhois.setText(_translate("Dialog", "Whois查询"))
        self.pushButton_2.setText(_translate("Dialog", "PushButton"))
        self.pushButton_3.setText(_translate("Dialog", "PushButton"))
        self.pushButton_4.setText(_translate("Dialog", "PushButton"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

