import sys,time,os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem
from SetFirefox import Ui_Dialog

class SetFirefoxWindow(QtWidgets.QDialog,Ui_Dialog):
    sinOut = pyqtSignal(str)
    def __init__(self,flag):
        super(SetFirefoxWindow,self).__init__()
        self.setWindowTitle("格格百度文档下载器")
        self.center()#居中显示
        self.setupUi(self)
        if flag == False:
            self.radioButton_hide.setChecked(True)
        else:
            self.radioButton_show.setChecked(True)
        self.pushButton_check.clicked.connect(self.checked)
        self.pushButton_cancel.clicked.connect(self.cancel)

    def center(self):
        screen=QDesktopWidget().screenGeometry()
        size=self.geometry()
        self.move((screen.width()-size.width())/2,(screen.height()-size.height())/2)

    def checked(self):
        if self.radioButton_show.isChecked():
            result = QMessageBox.question(self, ("question"), ("你确定将下载过程截屏任务的浏览器显示出来，会看起来很奇怪？" ), QMessageBox.Yes | QMessageBox.No)
            if result ==QMessageBox.Yes :
                self.sinOut.emit('True')
                self.close()
            else : pass
        else:
            self.sinOut.emit('False')
            self.close()

    def cancel(self):
        self.close()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)  # 所有 QT都需要
    myshow = SetFirefoxWindow(False)
    myshow.show()
    sys.exit(app.exec_())