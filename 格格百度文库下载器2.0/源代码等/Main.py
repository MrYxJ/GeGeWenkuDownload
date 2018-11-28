# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(730, 790)
        MainWindow.setFixedSize(730,790)
        MainWindow.setMinimumSize(QtCore.QSize(730, 0))
        MainWindow.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 16pt \"楷体\";\n"
"background-color: rgb(122, 200, 187);\n"
"\n"
"\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(70, 190, 651, 31))
        self.lineEdit.setStyleSheet("border-color: rgb(85, 255, 127);\n"
"background-color: rgb(255, 255, 255);")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_set_file_path = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_set_file_path.setGeometry(QtCore.QRect(600, 680, 121, 51))
        self.pushButton_set_file_path.setStyleSheet("font: 13pt \"隶书\";\n"
"color: rgb(85, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.pushButton_set_file_path.setObjectName("pushButton_set_file_path")
        self.pushButton_download = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_download.setGeometry(QtCore.QRect(410, 250, 111, 41))
        self.pushButton_download.setStyleSheet("font: 18pt \"隶书\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.pushButton_download.setObjectName("pushButton_download")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 670, 141, 20))
        self.label.setStyleSheet("font: 12pt \"楷体\";\n"
"\n"
"color: rgb(0, 0, 0);")
        self.label.setObjectName("label")
        self.label_file_path = QtWidgets.QLabel(self.centralwidget)
        self.label_file_path.setGeometry(QtCore.QRect(10, 690, 581, 31))
        self.label_file_path.setStyleSheet("font: 11pt \"Arial Rounded MT Bold\";\n"
"color: rgb(255, 0, 0);")
        self.label_file_path.setObjectName("label_file_path")
        self.pushButton_clear = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_clear.setGeometry(QtCore.QRect(180, 250, 111, 41))
        self.pushButton_clear.setStyleSheet("font: 14pt \"隶书\";\n"
"color: rgb(255, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"\n"
"\n"
"")
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.pushButton_history = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_history.setGeometry(QtCore.QRect(610, 330, 111, 41))
        self.pushButton_history.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 85, 255);\n"
"font: 12pt \"隶书\";")
        self.pushButton_history.setObjectName("pushButton_history")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 180, 51, 51))
        self.label_2.setStyleSheet("font: 14pt \"Comic Sans MS\";\n"
"color: rgb(0, 0, 0);")
        self.label_2.setObjectName("label_2")
        self.pushButton_about = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_about.setGeometry(QtCore.QRect(650, 0, 75, 23))
        self.pushButton_about.setStyleSheet("font: 12pt \"楷体\";\n"
"color: rgb(0, 170, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.pushButton_about.setObjectName("pushButton_about")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(140, 20, 451, 111))
        self.label_3.setStyleSheet("font: 48pt \"华文行楷\";\n"
"color: rgb(0, 0, 0);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(220, 120, 301, 31))
        self.label_4.setStyleSheet("font: 17pt \"楷体\";\n"
"color: rgb(255, 85, 0);")
        self.label_4.setObjectName("label_4")
        self.textBrowser_status = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_status.setGeometry(QtCore.QRect(10, 390, 711, 281))
        self.textBrowser_status.setStyleSheet("background-image: url(:/history/96130b71ly1fbpxqnxcfaj20j30j4q33.jpg);\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"font: 10pt \"黑体\";")
        self.textBrowser_status.setObjectName("textBrowser_status")
        self.pushButton_clearstatus = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_clearstatus.setGeometry(QtCore.QRect(10, 340, 141, 41))
        self.pushButton_clearstatus.setStyleSheet("font: 14pt \"隶书\";\n"
"color: rgb(255, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.pushButton_clearstatus.setObjectName("pushButton_clearstatus")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 730, 27))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.action_queue = QtWidgets.QAction(MainWindow)
        self.action_queue.setObjectName("action_queue")
        self.action_pdf = QtWidgets.QAction(MainWindow)
        self.action_pdf.setObjectName("action_pdf")
        self.action_path = QtWidgets.QAction(MainWindow)
        self.action_path.setObjectName("action_path")
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action_history = QtWidgets.QAction(MainWindow)
        self.action_history.setObjectName("action_history")
        self.action_hide_firefox = QtWidgets.QAction(MainWindow)
        self.action_hide_firefox.setObjectName("action_hide_firefox")
        self.menu.addAction(self.action_queue)
        self.menu.addAction(self.action_history)
        self.menu_2.addAction(self.action_pdf)
        self.menu_2.addAction(self.action_path)
        self.menu_2.addAction(self.action_hide_firefox)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        self.pushButton_clear.clicked.connect(self.lineEdit.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "格格百度文库下载器2.0【代码已开源】"))
        MainWindow.setToolTip(_translate("MainWindow", "<html><head/><body><p>如果觉得方便，可以考虑去[关于]里给作者加一个鸡腿！</p></body></html>"))
        MainWindow.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>软件源码：https://github.com/MrYxJ/GeGeWenkuDownload</p><p>欢迎start，关注。</p></body></html>"))
        self.pushButton_set_file_path.setText(_translate("MainWindow", "设置文件路径"))
        self.pushButton_download.setText(_translate("MainWindow", "下载"))
        self.label.setText(_translate("MainWindow", "当前文件下载路径："))
        self.label_file_path.setText(_translate("MainWindow", "C:\\gsisbest"))
        self.pushButton_clear.setText(_translate("MainWindow", "清除Link"))
        self.pushButton_history.setText(_translate("MainWindow", "历史下载记录"))
        self.label_2.setText(_translate("MainWindow", "LINK:"))
        self.pushButton_about.setText(_translate("MainWindow", "关于"))
        self.label_3.setText(_translate("MainWindow", "百度文库下载器"))
        self.label_4.setText(_translate("MainWindow", "让每个人更加便利提升自己"))
        self.textBrowser_status.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'黑体\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'楷体\'; font-weight:600; color:#000000;\">下载状态：当前任务未开始......</span></p></body></html>"))
        self.pushButton_clearstatus.setText(_translate("MainWindow", "清空下载状态"))
        self.menu.setTitle(_translate("MainWindow", "更多功能"))
        self.menu_2.setTitle(_translate("MainWindow", "高级设置"))
        self.action_queue.setText(_translate("MainWindow", "批量下载百度文库文挡"))
        self.action_pdf.setText(_translate("MainWindow", "设置下载PDF文件分辨率"))
        self.action_path.setText(_translate("MainWindow", "设置文件下载路径"))
        self.action.setText(_translate("MainWindow", "设置批量下载多进程核数"))
        self.action_history.setText(_translate("MainWindow", "历史下载记录"))
        self.action_hide_firefox.setText(_translate("MainWindow", "设置下载过程浏览器的隐藏"))

import mainui_rc
