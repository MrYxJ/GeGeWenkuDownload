import sys,time,os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem
from SetPdf import Ui_Dialog

class SetPdfWindow(QtWidgets.QDialog,Ui_Dialog):
    sinOut = pyqtSignal(str)
    def __init__(self,ratio = 'medium+'):
        super(SetPdfWindow,self).__init__()
        self.setWindowTitle("格格百度文档下载器")
        self.center()#居中显示
        self.setupUi(self)
        self.ratio = ratio
        self.init()
        self.pushButton_check.clicked.connect(self.checked)
        self.pushButton_cancel.clicked.connect(self.cancel)

    def init(self):
        if self.ratio == 'small':
            self.radioButton_1.setChecked(True)
        elif self.ratio == 'medium':
            self.radioButton_2.setChecked(True)
        elif self.ratio == 'medium+':
            self.radioButton_3.setChecked(True)
        elif self.ratio == 'super':
            self.radioButton_4.setChecked(True)

    def center(self):
        screen=QDesktopWidget().screenGeometry()
        size=self.geometry()
        self.move((screen.width()-size.width())/2,(screen.height()-size.height())/2)

    def checked(self):
        if self.radioButton_1.isChecked() : self.ratio = 'small'
        if self.radioButton_2.isChecked() : self.ratio = 'medium'
        if self.radioButton_3.isChecked() : self.ratio = 'medium+'
        if self.radioButton_4.isChecked() : self.ratio = 'super'
        result = QMessageBox.question(self, ("question"), ("你确定将下载PDF文件分辨率修改成[%s]？"% self.ratio ), QMessageBox.Yes | QMessageBox.No)
        if result ==QMessageBox.Yes :
            self.sinOut.emit(self.ratio)
            self.close()
        else : pass

    def cancel(self):
        self.close()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)  # 所有 QT都需要
    myshow = SetPdfWindow()
    myshow.show()
    sys.exit(app.exec_())