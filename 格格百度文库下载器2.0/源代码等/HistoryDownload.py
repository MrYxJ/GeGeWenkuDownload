# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HistoryDownload.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(688, 675)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 671, 591))
        self.tableWidget.setStyleSheet("")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(0, 0, 0))
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.pushButton_delete = QtWidgets.QPushButton(Form)
        self.pushButton_delete.setGeometry(QtCore.QRect(170, 610, 121, 41))
        self.pushButton_delete.setStyleSheet("font: 14pt \"楷体\";\n"
"")
        self.pushButton_delete.setObjectName("pushButton_delete")
        self.pushButton_delete_all = QtWidgets.QPushButton(Form)
        self.pushButton_delete_all.setGeometry(QtCore.QRect(380, 610, 121, 41))
        self.pushButton_delete_all.setStyleSheet("font: 14pt \"楷体\";")
        self.pushButton_delete_all.setObjectName("pushButton_delete_all")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "历史下载记录"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "文档名称"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "文档类型"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "下载时间"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "下载路径"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "下载网址"))
        self.pushButton_delete.setText(_translate("Form", "选择删除"))
        self.pushButton_delete_all.setText(_translate("Form", "全部删除"))

import mainui_rc
