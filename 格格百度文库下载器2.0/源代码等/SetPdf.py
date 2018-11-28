# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SetPdf.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(443, 300)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(90, 10, 251, 51))
        self.label.setStyleSheet("font: 16pt \"楷体\";")
        self.label.setObjectName("label")
        self.radioButton = QtWidgets.QRadioButton(Dialog)
        self.radioButton.setGeometry(QtCore.QRect(110, 70, 111, 20))
        self.radioButton.setStyleSheet("font: 14pt \"黑体\";")
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_2.setGeometry(QtCore.QRect(110, 110, 151, 20))
        self.radioButton_2.setStyleSheet("font: 14pt \"黑体\";")
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_3.setGeometry(QtCore.QRect(110, 150, 251, 20))
        self.radioButton_3.setStyleSheet("font: 14pt \"黑体\";")
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_4.setGeometry(QtCore.QRect(110, 190, 161, 20))
        self.radioButton_4.setStyleSheet("font: 14pt \"黑体\";")
        self.radioButton_4.setObjectName("radioButton_4")
        self.pushButton_check = QtWidgets.QPushButton(Dialog)
        self.pushButton_check.setGeometry(QtCore.QRect(100, 240, 81, 31))
        self.pushButton_check.setStyleSheet("font: 14pt \"楷体\";")
        self.pushButton_check.setObjectName("pushButton_check")
        self.pushButton_cancel = QtWidgets.QPushButton(Dialog)
        self.pushButton_cancel.setGeometry(QtCore.QRect(250, 240, 71, 31))
        self.pushButton_cancel.setStyleSheet("font: 14pt \"楷体\";")
        self.pushButton_cancel.setObjectName("pushButton_cancel")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "设置下载PDF文件分辨率"))
        self.radioButton.setText(_translate("Dialog", "595x842"))
        self.radioButton_2.setText(_translate("Dialog", "1240x1750"))
        self.radioButton_3.setText(_translate("Dialog", "1487x2150（默认）"))
        self.radioButton_4.setText(_translate("Dialog", "2479x3508"))
        self.pushButton_check.setText(_translate("Dialog", "确认"))
        self.pushButton_cancel.setText(_translate("Dialog", "取消"))

