# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SetFirefox.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(434, 300)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 30, 371, 71))
        self.label.setStyleSheet("font: 14pt \"楷体\";")
        self.label.setObjectName("label")
        self.radioButton_hide = QtWidgets.QRadioButton(Dialog)
        self.radioButton_hide.setGeometry(QtCore.QRect(110, 100, 96, 20))
        self.radioButton_hide.setStyleSheet("font: 16pt \"楷体\";")
        self.radioButton_hide.setObjectName("radioButton_hide")
        self.radioButton_show = QtWidgets.QRadioButton(Dialog)
        self.radioButton_show.setGeometry(QtCore.QRect(250, 100, 96, 20))
        self.radioButton_show.setStyleSheet("font: 16pt \"楷体\";")
        self.radioButton_show.setObjectName("radioButton_show")
        self.pushButton_check = QtWidgets.QPushButton(Dialog)
        self.pushButton_check.setGeometry(QtCore.QRect(120, 200, 81, 31))
        self.pushButton_check.setStyleSheet("font: 14pt \"楷体\";")
        self.pushButton_check.setObjectName("pushButton_check")
        self.pushButton_cancel = QtWidgets.QPushButton(Dialog)
        self.pushButton_cancel.setGeometry(QtCore.QRect(230, 200, 71, 31))
        self.pushButton_cancel.setStyleSheet("font: 14pt \"楷体\";")
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 130, 371, 71))
        self.label_2.setStyleSheet("font: 14pt \"楷体\";\n"
"color: rgb(255, 0, 0)")
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "设置在下载过程中驱动的浏览器是否隐藏"))
        self.radioButton_hide.setText(_translate("Dialog", "隐藏"))
        self.radioButton_show.setText(_translate("Dialog", "显示"))
        self.pushButton_check.setText(_translate("Dialog", "确认"))
        self.pushButton_cancel.setText(_translate("Dialog", "取消"))
        self.label_2.setText(_translate("Dialog", "在平时使用中建议隐藏，显示只是为了\n"
"演示下载过程浏览器的工作原理及作用。"))

