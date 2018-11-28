import sys,time,os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem
from BaiduwenkuFirefox import cralw
from QueueDownload import Ui_Form

class QueueWindow(QtWidgets.QDialog,Ui_Form):
    sinOut = pyqtSignal(str)
    def __init__(self):
        super(QueueWindow,self).__init__()
        self.setWindowTitle("格格百度文档下载器")
        self.center()#居中显示
        self.setupUi(self)
        self.pushButton_txt.clicked.connect(self.import_txt)
        self.pushButton_download.clicked.connect(self.start_queuedownload)
        self.cra = cralw()
        self.file_name= ''

    def center(self):
        screen=QDesktopWidget().screenGeometry()
        size=self.geometry()
        self.move((screen.width()-size.width())/2,(screen.height()-size.height())/2)

    def import_txt(self):
        path = QtWidgets.QFileDialog.getOpenFileName(self, '导入txt文件路径','')
        if path[0].find('.txt')==-1:
           warn = QMessageBox.warning(self, ("警告"), ("老铁，请确保打开是txt文件！"), QMessageBox.Yes)
           return
        self.label_path.setText(path[0])
        self.file_name = path[0]

    def start_queuedownload(self):
        if self.file_name == '':
             warn = QMessageBox.warning(self, ("警告"), ("老铁，请先导入txt文件"), QMessageBox.Yes)
             return

        self.sinOut.emit(self.file_name)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)  # 所有 QT都需要
    myshow = QueueWindow()
    myshow.show()
    sys.exit(app.exec_())