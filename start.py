# -*- coding: utf-8 -*-

"""
Module implementing Dialog.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog

from Ui_home import Ui_Dialog
a = 0
class Dialog(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Dialog, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot(int)
    def on_dial_valueChanged(self, value):
        a = int(value)
        self.label.setText(str(value))
    def on_pushButton_clicked(self):
        if int(self.dial.value()) == 7:
            self.label.setText("密码正确，即将跳转")
            Home = QtGui.QDialog()
            ui = Dialog2()
            ui.setupUi(Home)
            Home.show()
            Home.exec_()
            self.form.show()
        else:
            self.label.setText("密码错误，请重试")
if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    dlg = Dialog()
    dlg.show()
    sys.exit(app.exec_())
