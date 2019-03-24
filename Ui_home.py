# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'J:\PYQT\第一测试\home.ui'
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
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(210, 70, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 200, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.dial = QtWidgets.QDial(Dialog)
        self.dial.setGeometry(QtCore.QRect(100, 40, 50, 64))
        self.dial.setMaximum(10)
        self.dial.setObjectName("dial")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(120, 110, 54, 12))
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        self.pushButton_2.clicked.connect(Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "进入"))
        self.pushButton_2.setText(_translate("Dialog", "退出"))
        self.label.setText(_translate("Dialog", "0"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

