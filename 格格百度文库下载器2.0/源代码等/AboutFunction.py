import sys,time,os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem
from About import Ui_Form
import webbrowser

class AboutWindow(QtWidgets.QDialog,Ui_Form):
    def __init__(self):
        super(AboutWindow,self).__init__()
        self.setWindowTitle("格格百度文档下载器")
        self.center()#居中显示
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.open_github)
        self.pushButton_1.clicked.connect(self.open_money)

    def center(self):
        screen=QDesktopWidget().screenGeometry()
        size=self.geometry()
        self.move((screen.width()-size.width())/2,(screen.height()-size.height())/2)

    def open_github(self):
        webbrowser.open("https://github.com/MrYxJ/GeGeWenkuDownload")

    def open_money(self):
        webbrowser.open("https://raw.githubusercontent.com/MrYxJ/GeGeWenkuDownload/master/%E6%A0%BC%E6%A0%BC%E7%99%BE%E5%BA%A6%E6%96%87%E5%BA%93%E4%B8%8B%E8%BD%BD%E5%99%A82.0/%E6%BA%90%E4%BB%A3%E7%A0%81%E7%AD%89/picture/wechat.jpg")



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)  # 所有 QT都需要
    myshow = AboutWindow()
    myshow.show()
    sys.exit(app.exec_())