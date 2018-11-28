import sys,time,os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtCore import QDateTime
from Main import  Ui_MainWindow
from BaiduwenkuFirefox import cralw
from HistoryDownloadFunction import  HistoryWindow
from QueueDownloadFunction import QueueWindow
from SetPdfFunction import SetPdfWindow
from SetFirefoxFunction import SetFirefoxWindow
from AboutFunction import AboutWindow
import mainui_rc
from multiprocessing import Pool
import multiprocessing
import webbrowser

class Download_Thread(QtCore.QThread):
    sinOut = pyqtSignal(str,int)
    def __init__(self, parent=None):
        super(Download_Thread, self).__init__(parent)
        self.cra = cralw()

    def Run(self, url, file_path):
        self.url = url
        self.file_path = file_path
        self.start()

    def run(self):
        print('url2:',self.url)
        status = self.cra.test_one(self.url,self.file_path)
        self.sinOut.emit(self.url,status)

class QueueDownload_Thread(QtCore.QThread):
    sinOut = pyqtSignal(str,int)
    sinOut2 = pyqtSignal(str)
    def __init__(self, parent=None):
        super(QueueDownload_Thread, self).__init__(parent)
        self.cra = cralw()

    def Run(self, txt_path, file_path):
        #print('file_path',txt_path)
        ulist = self.cra.read_from_txt(txt_path)
        self.sinOut2.emit('从[%s]文件导入任务网址！' % txt_path)
        for url in ulist:
            self.sinOut2.emit(url)
        self.sinOut2.emit('所有任务导入完毕，开始执行批量下载！')
        self.ulist = ulist
        self.file_path = file_path
        self.start()

    def run(self):
        for url in self.ulist:
            status = self.cra.test_one(url,self.file_path)
            self.sinOut.emit(url,status)
        self.sinOut2.emit('文件全部批量下载完成储存在[%s]。'%(self.file_path))

class MainWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setWindowTitle("格格百度文档下载器")
        self.setWindowIcon(QIcon("male.png"))
        self.center()#居中显示
        self.setupUi(self)
        self.file_path = os.getcwd()
        self.display_path(self.file_path)
        self.pushButton_download.clicked.connect(self.download)
        self.pushButton_set_file_path.clicked.connect(self.set_file_path)
        self.pushButton_history.clicked.connect(self.show_download_history)
        self.pushButton_about.clicked.connect(self.about)
        self.pushButton_clearstatus.clicked.connect(self.clear_status)
        self.action_history.triggered.connect(self.show_download_history)
        self.action_path.triggered.connect(self.set_file_path)
        self.action_queue.triggered.connect(self.queue_download_window)
        self.action_pdf.triggered.connect(self.set_pdf_ratio)
        self.action_hide_firefox.triggered.connect(self.set_firefox)
        self.cra_config = {'ratio':'medium+','display':False }
        self.process_num = 1

    def center(self):
        screen=QDesktopWidget().screenGeometry()
        size=self.geometry()
        self.move((screen.width()-size.width())/2,(screen.height()-size.height())/2)

    def display_path(self,path_name):
        self.label_file_path.setText(path_name)

    def set_file_path(self):
        path = QtWidgets.QFileDialog.getExistingDirectory(self,"设置文件下载路径",self.file_path)
        if path == '':
            path = self.file_path
        self.file_path = path
        self.display_path(path)

    def exit(self):
        result=QMessageBox.question(self,("question"),("你确定要退出吗？"),
                    QMessageBox.Yes|QMessageBox.No)
        if result==QMessageBox.Yes: sys.exit(1)
        else:pass

    def failed_warn(self,url,status):
        #print('url:',url,'status:',status)
        warns = ''
        if url == '':
            warns = '文库链接不能为空！'
        elif url == 'sgg' or url == '水格格' or url == '格格' or url == 'gg':
            warns = '格格,要相信你是最好的！'
        elif url == 'MrYx':
            warns = '恭喜你，哈哈哈！找到开发者，MrYx QQ:529674242!'
        elif status == 1:
            warns = '[%s] 不是百度文库文章的地址,请输入合法的百度文库链接！' % url
        elif status == 2:
            warns = '尝试打开浏览器失败，请确认您的电脑安装了火狐浏览器'
        elif status == 3:
            warns = '浏览器像服务器发送请求失败，请过一段时间尝试'
        elif status == 4:
            warns = '该页面不是要求的需要爬取页面'
        elif status == 5:
            warns = '文章已经删除或link失效，当前页面不是正常文章界面，无法爬取'
        elif status == 6:
            warns = '付费文档显示不完全,无法下载'
        elif status == 0:
            warns = '[%s]文档下载成功！\n如果网速慢等原因下载不完美，可以再尝试一次！'% url
        warn = QMessageBox.warning(self, ("下载结果"), (warns), QMessageBox.Yes)

    def download(self,url = False):
        if url == False:
            url = self.lineEdit.text()
        self.Download = Download_Thread()
        self.Download.sinOut.connect(self.failed_warn)
        self.Download.cra.sinOut.connect(self.append_status)
        try:
            self.Download.cra.display = self.cra_config['display']
            self.Download.cra.default_ratio = self.cra_config['ratio']
        except Exception as e:
            print('e',e)
        # 开始执行run()函数里的内容
        self.Download.Run(url,self.file_path)

    def about(self):
        self.a = AboutWindow()
        self.a.show()

    def show_download_history(self):
        self.win = HistoryWindow()
        self.win.exec_()

    def append_status(self,sstr):
        self.textBrowser_status.append(sstr)

    def clear_status(self):
        self.textBrowser_status.setText('')

    def queue_download_window(self):
        self.queuewindow = QueueWindow()
        self.queuewindow.sinOut.connect(self.queue_download_start)
        self.queuewindow.show()

    def queue_download_start(self,file_name):
        self.queuewindow.hide()
        #print("批量下载开始....txt文件导入路径:%s"%  file_name)
        self.textBrowser_status.append('批量下载开始....txt文件导入路径:%s' % file_name)
        if os.path.exists(file_name) == False:
            warn = QMessageBox.warning(self, ("警告"), ("老铁，请确认导入地址为[%s]的txt文件存在!"%file_name), QMessageBox.Yes)
            return
        self.Download = QueueDownload_Thread()
        self.Download.sinOut.connect(self.failed_warn)
        self.Download.sinOut2.connect(self.append_status)
        self.Download.cra.sinOut.connect(self.append_status)
        self.Download.cra.display = self.cra_config['display']
        self.Download.cra.default_ratio = self.cra_config['ratio']
        self.Download.Run(file_name, self.file_path)

    def set_pdf_ratio(self):
        self.setpdf = SetPdfWindow(self.cra_config['ratio'])
        self.setpdf.show()
        self.setpdf.sinOut.connect(self.modifyratio)

    def set_firefox(self):
        self.setpdf = SetFirefoxWindow(self.cra_config['display'])
        self.setpdf.show()
        self.setpdf.sinOut.connect(self.modifyfirefox)

    def modifyratio(self,ratio):
        self.cra_config['ratio'] = ratio

    def modifyfirefox(self,flag):
        if flag == 'True':
            self.cra_config['display']= True
        else :
            self.cra_config['display'] = False

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)  # 所有 QT都需要
    myshow = MainWindow()
    myshow.show()
    sys.exit(app.exec_())