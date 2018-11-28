import sys,time,os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem
from BaiduwenkuFirefox import cralw
from HistoryDownload import Ui_Form

class HistoryWindow(QtWidgets.QDialog,Ui_Form):
    def __init__(self):
        super(HistoryWindow,self).__init__()
        self.setWindowTitle("格格百度文档下载器")
        self.center()#居中显示
        self.setupUi(self)
        self.cra = cralw()
        self.show_all_history()
        self.pushButton_delete_all.clicked.connect(self.delete_all)
        self.pushButton_delete.clicked.connect(self.delete_select)

    def center(self):
        screen=QDesktopWidget().screenGeometry()
        size=self.geometry()
        self.move((screen.width()-size.width())/2,(screen.height()-size.height())/2)

    def show_all_history(self):
        all = self.cra.read_from_sqlite()
        num = len(all)
        self.tableWidget.setRowCount(num)
        index =0
        for line in all:
            url = line[1]
            name = line[2]
            format = line[3]
            path = line[4]
            time = line[5]
            newItem = QTableWidgetItem(name)
            self.tableWidget.setItem(index,0,newItem)
            newItem = QTableWidgetItem(format)
            self.tableWidget.setItem(index, 1, newItem)
            newItem = QTableWidgetItem(time)
            self.tableWidget.setItem(index, 2, newItem)
            newItem = QTableWidgetItem(path)
            self.tableWidget.setItem(index, 3, newItem)
            newItem = QTableWidgetItem(url)
            self.tableWidget.setItem(index, 4, newItem)
            index = index +1
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setSelectionMode(QTableWidget.MultiSelection )
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.resizeColumnsToContents()
        return num

    def delete_select(self,event):
        items = self.tableWidget.selectedItems()
        selectRow = []
        index = 0
        for item in items:
            index +=1
            if (index)%3==0:
                time = item.text()
            if (index)%5==0:
                url = item.text()
                selectRow.append({'time':time,'url':url})
                index =0

        if selectRow == []:
            warn = QMessageBox.warning(self, ("警告"), ("你真调皮，当前选择删除的历史下载记录为空！"), QMessageBox.Yes)
            return
        result = QMessageBox.question(self, ("删除确认"), ("你确定要删除选择的下载记录吗？如果觉得做的不错欢迎给作者加鸡腿！"),
                                      QMessageBox.Yes | QMessageBox.No)
        if result == QMessageBox.Yes:
            for row in selectRow:
                #print(row['time'],row['url'])
                self.cra.delete_record_from_sqlite(url = row['url'],time = row['time'])
            self.show_all_history()
        else:
            pass

    def delete_all(self):
        if self.show_all_history()==0:
            warn = QMessageBox.warning(self, ("警告"), ("你真调皮，当前历史下载记录为空！"), QMessageBox.Yes)
            return
        result = QMessageBox.question(self, ("删除确认"), ("你确定要删除所有下载记录吗？如果觉得做的不错欢迎给作者加鸡腿！"),
                            QMessageBox.Yes | QMessageBox.No)
        if result == QMessageBox.Yes:
            self.cra.delete_record_from_sqlite('all')
            self.show_all_history()
        else:
            pass



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)  # 所有 QT都需要
    myshow = HistoryWindow()
    myshow.show()
    sys.exit(app.exec_())