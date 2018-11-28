# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QueueDownload.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(531, 409)
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(20, 10, 501, 191))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton_txt = QtWidgets.QPushButton(Form)
        self.pushButton_txt.setGeometry(QtCore.QRect(210, 230, 121, 31))
        self.pushButton_txt.setStyleSheet("font: 12pt \"楷体\";")
        self.pushButton_txt.setObjectName("pushButton_txt")
        self.pushButton_download = QtWidgets.QPushButton(Form)
        self.pushButton_download.setGeometry(QtCore.QRect(210, 350, 121, 31))
        self.pushButton_download.setStyleSheet("font: 12pt \"楷体\";")
        self.pushButton_download.setObjectName("pushButton_download")
        self.label_path = QtWidgets.QLabel(Form)
        self.label_path.setGeometry(QtCore.QRect(20, 280, 501, 31))
        self.label_path.setStyleSheet("font: 10pt \"楷体\";\n"
"color: rgb(255, 0, 0);")
        self.label_path.setObjectName("label_path")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "批量下载导入文件窗口"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">使用批量下载说明：</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">1.首先新建一个txt文件。</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">2.在txt文件里面编辑粘贴入要下载的所有百度文库文档</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">的链接，一行一条链接。</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">3.点击【导入txt文件】，点击</span><span style=\" font-size:10pt; font-weight:600;\">【开始下载】，</span><span style=\" font-size:10pt;\">观察主页面下载状态等待下载完成。</span></p></body></html>"))
        self.pushButton_txt.setText(_translate("Form", "导入txt文件"))
        self.pushButton_download.setText(_translate("Form", "开始下载"))
        self.label_path.setText(_translate("Form", "文件路径："))

