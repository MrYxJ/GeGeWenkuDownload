#coding:utf-8
#coded by MrYx in laibo 2018.2.6
from selenium import webdriver
from bs4 import  BeautifulSoup
from PIL import Image
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.firefox.options import Options
from selenium.webdriver.ie.options import Options
import time
from time import sleep
import os
import requests
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, landscape,portrait
import hashlib
import urllib
import sys
import sqlite3

from multiprocessing import Pool
import multiprocessing

'''
 
 注意，此程序运行时候，千万不要再打开火狐浏览器（Firefox）！
                                    Author:  MrYx 
                                    Mail:529674242@qq.com

'''

class cralw():
    def __init__(self):
        self.default_ratio = 'medium+'
        self.pdf_ratio = {'super': [2479,3488],'medium+':[1487,2090],
                          'medium':[1240,1740],'small':[595,832]  } #设置doc文件浏览器准备截图大小
        #mongo 连接参数
        # self.client = pymongo.MongoClient('mongodb://192.168.2.211:27017/')
        # self.mongo_db = self.client['baiduwenku']
        # self.collection = self.mongo_db['wenku_links']
        #
        # #sql service 连接参数
        # self.host = 'localhost'
        # self.user = 'sa'
        # self.password = '123456'
        # self.db_name = 'baiduwenku'
        # self.db = pymssql.connect(self.host, self.user, self.password, self.db_name)
        # self.cursor = self.db.cursor()

    def init(self, url):
        '''
        在对某个特定url下载文章初始化操作，包括打开浏览器，发送请求，判断链接合法性
        :param url:
        :return:
        '''
        self.article_content = ''
        self.article_title = ''
        self.article_url = url
        self.article_page_tag = '**********'  # 文章详情每页分隔符
        wait_time =1
        #print('url:',url)
        if 'wenku.baidu.com/view' not in self.article_url:
            print('%s 不是百度文库文章的地址,停止爬取！' % self.article_url)
            self.permit = False
            return

        try: #尝试打开浏览器
            self.options = webdriver.FirefoxOptions()
            self.options.add_argument('--headless')  # 不弹出浏览器界面
            self.browser = webdriver.Firefox(firefox_options= self.options)
        except Exception as e:
            print('error:', e)
            print('尝试打开浏览器失败，请确认您的电脑安装了火狐浏览器！Error information',e)
            try:
                self.browser.quit()
            except:
                pass
            self.permit = False
            return

        while True: # 浏览器向url地址发送请求
            try:
                self.browser.get(self.article_url)
                break
            except Exception as e:
                print('Error information:',e,'\t[%s]s latter,try connection again!'%wait_time)
                sleep(wait_time)
                wait_time <<=1
                if wait_time >= 512:
                    print('This file can\'t cralw!')
                    self.permit = False
                    return

        try:
            if self.browser.find_element_by_css_selector('.doc-container'):
                print('该页面不是要求的需要爬取页面！')
                self.permit = False
                return
        except:pass

        cnt =0 #判断page-count 是否能被查找到，判断界面是否完全被加载出来
        while cnt < 6:  # 如果page-count元素没加载出来，就等待页面加载,尝试过多次数就说明网页不符合爬取要求
            try:
                self.page_num = int(self.clean_word(self.browser.find_element_by_css_selector('.page-count').text[1:]))
                break
            except:
                cnt +=1
                print('Waiting to find element')
                #self.browser.get(url)
                time.sleep(3)


        if cnt >= 6: # 文章已经删除或url失效，当前页面不是正常文章界面，无法爬取
            print('This  can\'t cralw!')
            self.permit = False
            return

        try: #付费文档显示不完全
            if self.browser.find_elements_by_css_selector('.vip-free-buy') or self.browser.find_element_by_css_selector(
                    '.down-btn-area.pay-doc-btn'):
                print('%s 此文档是付费文档,停止爬取！' % self.article_url)
                self.permit = False
                return
        except:
            pass

        self.permit = True  # 说明该网页是符合爬取并且正常打开的
        try:
            self.article_title = self.clean_word(self.browser.find_elements_by_css_selector('.reader_ab_test.with-top-banner')[0].text)
            type = self.browser.find_element_by_css_selector(".reader_ab_test.with-top-banner b").get_attribute('class')
            if type == 'ic ic-ppt':
                self.article_format = 'PPT'
            elif type == 'ic ic-doc' or type == 'ic ic-pdf':
                self.article_format = 'PDF'
            elif type == 'ic ic-txt':
                self.article_format = 'TXT'
            else:
                self.type = 'Doc'
            print(self.article_title, '\t\t', self.article_format, '\t\t', self.article_url)
        except Exception as e:
            print('get title or get type error information:', e)
            self.permit = False
            return

    def clean_word(self, sstr):
        '''
        去除字符串里所有转义字符标点
        :param sstr:
        :return:
        '''
        return "".join(sstr.split())

    def click_fullscreen(self):
        '''
        模拟浏览器点击百度文库全屏浏览模式，方便截取
        :return:
        '''
        cnt = 1
        while cnt <= 16:
            try:
                fullscreen_btn = self.browser.find_element_by_css_selector(
                    ".ic.reader-fullScreen.xllDownloadLayerHit_left")
                fullscreen_btn.click()
                top_page = self.browser.find_elements_by_css_selector(".reader_ab_test.with-top-banner")
                self.browser.execute_script('arguments[0].scrollIntoView();', top_page[-1])
                print('浏览器全屏完毕！')
                break
            except Exception as e:
                self.browser.get(self.article_url)
                cnt *= 2
                sleep(cnt)

    def click_more_btn(self):
        '''
        模拟点击，点开继续阅读，显示剩下要爬的内容
        :return:
        '''
        try:
            more_page = self.browser.find_elements_by_css_selector("#html-reader-go-more")
            self.browser.execute_script('arguments[0].scrollIntoView();', more_page[-1])
            more_page_btn = self.browser.find_element_by_css_selector(".moreBtn.goBtn")
            more_page_btn.click()
            top_page = self.browser.find_elements_by_css_selector(".reader_ab_test.with-top-banner")
            self.browser.execute_script('arguments[0].scrollIntoView();', top_page[-1])
        except:
            pass

    def clear_screen(self):
        '''
        模拟点击，关闭全屏多余弹窗，广告
        :return:
        '''
        try: #去掉顶部百度栏
            self.browser.execute_script("""
            var element = document.querySelector(".fix-searchbar-wrap");
            if (element)
                element.parentNode.removeChild(element);
            """)
        except Exception as e: print('clear top bar error information:',e)

        try:
            self.browser.execute_script("document.getElementsByClassName('fix-adsbar-wrap __FIXED__')[0].style='display:none'")
        except : pass
        try: # 隐藏全屏后侧边的条栏
            if self.article_format!='ppt': self.browser.execute_script("document.getElementById('activity-tg').style='display:none'")
        except Exception as e: pass #print('clear right bar error information:',e)

        try: # 隐藏底部输入页码条栏
            self.browser.execute_script("document.getElementsByClassName('reader-tools-bar-wrap')[0].style='display:none'")
            #ok = self.browser.find_element_by_css_selector('.reader-tools-bar-wrap.ugctest.tools-bar-small.tools-bar-smaller')
        except Exception as e:  print('clear down bar error information:',e)

        try:
            self.browser.find_element_by_css_selector('.close.fenxiang').click()
        except: pass
        try:
            self.browser.find_element_by_css_selector(".close-dialog.close-pop").click()
        except: pass
        try:
            self.browser.find_element_by_css_selector('.close-icon.close.close-pop').click()
        except: pass

    def show_down_bar(self):
        try: # 将隐藏的下面输入页码条栏显示出来，为了手动输入页数，换一面截图
            self.browser.execute_script("document.getElementsByClassName('reader-tools-bar-wrap')[0].style='display:block'")
        except Exception as e: print('show down bar error information:',e)
    # def get_code_from_on_page(self, type, num):
    #     '''
    #     获取页码为num的页面的代码内容
    #     :param type:
    #     :param num:
    #     :return:
    #     '''
    #     dict_type = {'txt':'#reader-pageNo-','doc':'.mod.reader-page.complex.reader-page-','ppt':'.ppt-page-item.ppt-bd.reader-pageNo-'}
    #     op = dict_type[type]+str(num)
    #     text = self.browser.find_element_by_css_selector(op).get_attribute('innerHTML')
    #     #print('text:',text)
    #     return text
    def scrapture_page_to_png_and_get_code(self):
        '''
        将word,pdf文章每一页截屏成png放在文件中
        :param page_list: 文章分页元素
        :param file_path: 保存png的文件夹
        :return:
        '''
        for index in range(self.page_num):
            cnt = 0
            while cnt <50:
                try:
                    self.browser.find_element_by_css_selector('.page-input').clear()
                    break
                except:
                    print('Waiting to find element')
                    time.sleep(1)
                    cnt += 1
            if cnt >50: continue

            self.browser.find_element_by_css_selector('.page-input').send_keys(str(index+1))
            self.browser.find_element_by_css_selector('.page-input').send_keys(Keys.ENTER)
            if index  % 50==0: sleep(1)
            while True:
                try:
                    Flag1 = self.browser.find_element_by_css_selector('.reader-tools-bar')
                    break
                except:
                    sleep(1)

            Flag2 = Flag1.find_element_by_css_selector('.ic.reader-fullScreen.xllDownloadLayerHit_left')
            if Flag2 and Flag2.get_attribute('title') == '全屏显示' :
                self.click_fullscreen()

            self.clear_screen() #去掉各种栏

            while True:
                try:
                    self.browser.save_screenshot(self.article_url_md5+str(index+1)+'.png')
                    break
                except:pass
            print('[%s]\'s [%s] page is capturing successfully' % (self.article_title, str(index+1)))
            self.show_down_bar()
    # def cut_all_png(self):
    #     '''
    #     裁剪截取每页图片的百度框，使其更纯粹,使用隐藏栏目后不需要
    #     :param self:
    #     :param file_path:
    #     :return:
    #     '''
    #     for i in range(self.page_num):
    #         img = Image.open(self.article_url_md5+str(i+1)+'.png')
    #         img2 = img.crop((0,self.rule[self.article_format][2],img.size[0],img.size[1]-self.rule[self.article_format][3]))
    #         self.width = img2.size[0]
    #         self.height = img2.size[1]
    #         img2.save(self.article_url_md5+str(i+1)+'.png')
    #         print('[%s]\'s [%s] pages cutting successfully' % (self.article_title, str(i+1)))
    def save_as_pdf(self, output_path = None, file_name = None):
        '''
        将截屏得到的图片合成pdf并可以放入指定的路径和指定的名称,最后删除图片，当传入指定路径名为空时，默认生成路径是程序同一目录下，传入的文件名称为空时则命名为url的md5
        :param self:
        :param file_path:
        :return:
        '''
        if output_path != None : output_path = output_path + '\\'
        else : output_path= ''
        c = canvas.Canvas(output_path+file_name+'.pdf',pagesize = portrait(A4))
        (maxw,maxh) = portrait(A4)
        for i in range(self.page_num):
            #img.show()
            #print(img.size[0],img.size[1])
            while True :
                try:
                    c.drawImage(self.article_url_md5+str(i+1)+'.png',0,0,maxw,maxh)
                    c.showPage()
                    break
                except:pass
            print('[%s]\'s [%s] page from png to pdf successful!'% (self.article_title,str(i+1)))
        try:
             c.save()
        except:pass
        start = 1
        while True:
           try:#程序太快了 保证后面删的时候 文件不会被占用
              for i in range(start,self.page_num+1):
                  os.remove(self.article_url_md5+str(i)+'.png')
                  start = i+1
              break
           except:
              print('[%s]\'s [%s] png waitting to be deleted!' % (self.article_title,str(start)))

    def get_url_md5(self):
        '''
        返回url的加密md5码
        :return:
        '''
        m = hashlib.md5()
        m.update(self.article_url.encode("utf8"))
        self.article_url_md5 = m.hexdigest()

    def get_classify(self):
        '''
        获取文件的分类
        :return:
        '''
        classify_arr = self.browser.find_elements_by_css_selector('#page-curmbs ul li')
        try:
            self.article_classify = ''
            first = True
            for classify_result in classify_arr:  # 文章分类
                if first : first = False
                else : self.article_classify = self.article_classify + '####'
                self.article_classify =self.article_classify + classify_result.text
        except:
            self.article_format = None

    def get_txt_to_txt(self, output_path = None, file_name = None):
        '''

        :param output_path:
        :param file_name:
        :return:
        '''
        if output_path != None:
            output_path = output_path + '\\'
        else:
            output_path = ''
        if file_name == None: file_name = self.article_title
        content = self.browser.page_source.encode('utf-8')
        soup = BeautifulSoup(content.decode('utf-8'),'lxml')
        reads = soup.select('.reader-page-wrap')
        first = True
        cnt = 1
        with open(output_path+file_name+'.txt','w') as f:
            for read in reads:
                if first:
                    first = False
                else:
                    self.article_content = self.article_content + self.article_page_tag
                self.article_content = self.article_content + str(read)
                for p in read.find_all('p'):
                    try:
                        f.write(p.text)
                    except:
                        pass
                print('[%s]\'s [%s] page is getting successfully!' % (self.article_title,cnt))
                cnt +=1

        if output_path == '': output_path_now = os.getcwd()
        else : output_path_now = output_path
        print('[%s] have successful downloaded in [%s] name [%s]' % (self.article_title, output_path_now, self.article_url_md5))

    def get_url_to_png(self, url, path, name):
        '''

        :param url:
        :param path:
        :param name:
        :return:
        '''
        while True:
            try:
                response = requests.get(url)
                response.raise_for_status()
                break
            except :
                print('Network connection badly,download ppt pages try again!')
        with open(path+'\\'+name+'.png','wb') as f:
            f.write(response.content)

    def get_ppt_to_png(self, output_path = None, file_name = None):
        '''

        :param output_path:
        :param file_name:
        :return:
        '''
        if output_path != None:
            output_path = output_path + '\\'
        else:
            output_path = ''
        if file_name == None: file_name = self.article_title

        file_path =  output_path + file_name
        if not os.path.exists(file_path):
            os.mkdir(file_path)

        for index,png in enumerate(self.browser.find_elements_by_css_selector('.ppt-page-item')):
            url = png.find_element_by_css_selector('img').get_attribute('src')
            if url == None :
                url = png.find_element_by_css_selector('img').get_attribute('data-src')
            self.get_url_to_png(url,file_path,str(index+1))

    def cralw_to_file_and_code(self, fpath=None, fname=None):
        '''

        :param fpath: 保存文件的路径
        :return:
        '''
        if self.permit == False:
            self.browser.quit()
            return
        print('[%s] have totally [%s] pages:'  %(self.article_title,self.page_num))
        print('files type',self.article_format)
        now = time.time()
        if fname == None: fname = self.article_title
        if self.article_format == 'TXT':
            self.click_more_btn()
            self.get_txt_to_txt(output_path=fpath, file_name=fname)

        elif self.article_format == 'PPT':
            self.click_more_btn()
            self.get_ppt_to_png(output_path=fpath, file_name=fname)

        else:
            self.click_more_btn()
            self.click_fullscreen()
            self.browser.set_window_size(self.pdf_ratio[self.default_ratio][0], self.pdf_ratio[self.default_ratio][1])
            self.scrapture_page_to_png_and_get_code()
            self.save_as_pdf(output_path=fpath, file_name=fname)

        self.browser.quit()
        if fpath == None:fpath = os.getcwd()+'\\'
        print('[%s] have successful downloaded in [%s] name [%s]' % (self.article_title, fpath, self.article_title))
        self.file_path = fpath
        print('Total cost time : %ss' % (time.time() - now))

    def add_record_to_sqlite(self):
        conn = sqlite3.connect('baiduwenku.db')
        cursor= conn.cursor()
        try:
            cursor.execute('CREATE TABLE IF NOT EXISTS download_record(url_md5 VARCHAR(30), url VARCHAR(60),name VARCHAR(30),format VARCHAR(10),path VARCHAR(60),time VARCHAR(30))')
        except Exception as e:
            print('建表Error:\n',e)

        now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        sql = 'insert into download_record (url_md5,url,name,format,path,time) values (?,?,?,?,?,?)'
        paras = (self.article_url_md5,self.article_url,self.article_title,self.article_format,self.file_path,now_time)
        cursor.execute(sql,paras)
        conn.commit()
        cursor.close()
        conn.close()
        print('[%s] 下载记录插入sqlite3数据库成功'%self.article_title)

    def read_from_txt(self, f_path):
        ulist = []
        with open(f_path, 'r') as f:
            for line in f.readlines():
                line = self.clean_word(line)
                if line != '':
                    ulist.append(line)
        print(f_path, 'read completed!')
        return ulist

    def read_from_sqlite(self):
        conn = sqlite3.connect('baiduwenku.db')
        cursor = conn.cursor()
        try:
            cursor.execute(
                'CREATE TABLE IF NOT EXISTS download_record(url_md5 VARCHAR(30), url VARCHAR(60),name VARCHAR(30),format VARCHAR(10),path VARCHAR(60),time VARCHAR(30))')
        except Exception as e:
            print('建表Error:\n', e)
        num = cursor.rowcount
        lines = cursor.execute('SELECT * FROM download_record')
        Format = '{0:{3}<10} {1:{3}<20} {2:{3}<35}'
        Format1 = '{0:{2}<4} {1:{2}<60}'

        #print(Format.format('文件名称','文件类型','下载路径','下载时间','网址',chr(12288)))
        for line in lines:
            url = line[1]
            name = line[2]
            format = line[3]
            path = line[4]
            time =line[5]
            print(Format.format(name, time, path, chr(12288)))
            print(Format1.format(format, url, chr(12288)))
            print('\n')
        cursor.close()
        conn.close()
        return num

    def delete_record_from_sqlite(self,url = None):
        conn = sqlite3.connect('baiduwenku.db')
        cursor = conn.cursor()
        try:
            cursor.execute(
                'CREATE TABLE IF NOT EXISTS download_record(url_md5 VARCHAR(30) PRIMARY KEY, url VARCHAR(60),name VARCHAR(30),format VARCHAR(10),path VARCHAR(60),time VARCHAR(30))')
        except Exception as e:
            print('建表Error:\n', e)
        if url == 'all':
            try:
                cursor.execute('DELETE FROM download_record')
                print('删除所有下载记录成功！')
            except Exception as e:
                print('删除所有下载记录失败！\n Error information:',e)
        else:
            try:
                sql = 'DELETE FROM download_record WHERE url = \'%s\'' % url
                cursor.execute(sql)
                print('删除[%s]下载记录成功！' % url)
            except Exception as e:
                print('删除[%s]下载记录失败！\n Error information:'% url,e)
        conn.commit()
        cursor.close()
        conn.close()

    def test_one(self, url, fpath = None):
        self.init(url)
        if self.permit == False:
            try:
                self.browser.quit()
            except:pass
            return
        self.get_url_md5()
        self.cralw_to_file_and_code(fpath)
        self.add_record_to_sqlite()
        print('\n')

    def __del__(self):  # python 析构函数
        try:
            self.browser.quit()
        except:pass
        #self.db.close()
        # self.collection.close()

    def menu(self):
        print('\t\t\t欢迎使用<格格文库下载器>')
        print('[1].下载百度文库文档')
        print('[2].批量下载百度文库文挡')
        print('[3].设置下载PDF文件的分辨率')
        print('[4].设置文件下载的路径')
        print('[5].查看历史下载记录')
        print('[6].删除历史下载记录')
        print('[7].设置批量下载时多进程的数量')
        print('[0].帮助')
        print('[exit].退出')


def run_menu():
    cra = cralw()
    file_path = None
    process_num = 4
    while True:
        os.system('cls')
        cra.menu()
        op = input('\n输入您选择功能序号：')
        if op == '1':
            url = input('请输入您要下载的百度文库文章的地址: ')
            os.system('cls')
            cra.test_one(url, file_path)
            c = input('下载完毕，按任意键返回功能菜单！')
        elif op == '2':
            while True:
                instructions = '''
 使用批量下载说明：
      1.首先找到此程序根目录下，找到一个名为urls的txt文件，如果没有请新建一个。
      2.在名为urls的txt文件里面粘贴入要下载的所有文件的百度文库链接，一行一条链接。
      3.输入[任意键]开始多进程的工作下载。
                  '''
                print(instructions)
                file_name = 'urls.txt'
                c = input('确保完成将所有链接写入[%s]文件中，按任意键开始！(输入[break]取消)' % file_name)
                if c == 'break':
                    c = input('取消批量下载成功，按任意键返回主菜单！')
                    break

                if os.path.exists(file_name) == False:
                    print('当前目录下[%s]不存在，请按照下载说明完成操作！'%file_name)
                    continue

                ulist = cra.read_from_txt(file_name)
                print('当前批量下载的进程数为：[%s]' % process_num)
                p = Pool(process_num)
                for url in ulist:
                    print(url)
                    p.apply_async(cralw().test_one, args=(url,file_path,))

                p.close()
                p.join()

                c = input('[%s]内文件全部批量下载完成，按任意键返回主菜单！'%file_name)
                f = open(file_name,'w')
                f.truncate()
                f.close()
                break
        elif op == '3':
            os.system('cls')
            introduce = '''
              [1].低分辨率-   595x842\n
              [2].中等分辨率- 1240x1754\n
              [3].中高分辨率- 1487x2150\n
              [4].超高分辨率- 2479x3508\n
                    '''
            while True:
                print(introduce)
                print(
                    '当前设置分辨率：%sx%s' % (
                    cra.pdf_ratio[cra.default_ratio][0], cra.pdf_ratio[cra.default_ratio][1]))
                print('###推荐设置中高分辨率 %sx%s\n' % (cra.pdf_ratio['medium+'][0], cra.pdf_ratio['medium+'][1]))
                op = input('您选择设置：')
                try:
                    if op == '1':
                        cra.default_ratio = 'small'
                    elif op == '2':
                        cra.default_ratio = 'medium'
                    elif op == '3':
                        cra.default_ratio = 'medium+'
                    elif op == '4':
                        cra.default_ratio = 'super'
                    else:
                        raise Exception
                except Exception:
                    print('输入错误，重新输入！')
                else:
                    break
            c = input('修改成功！\n按任意键返回功能菜单')
        elif op == '4':
            while True:
                os.system('cls')
                if file_path == None:
                    path = os.getcwd()
                else:
                    path = file_path
                print('当前下载路径：[%s]' % path)
                path = input('输入你想要存放下载文件的路径（取消修改输入[break]）：')
                if os.path.exists(path):
                    file_path = cra.clean_word(path)
                    print('修改成功！当前下载路径是: [%s]' % file_path)
                    c = input('\n按任意键返回功能菜单')
                    break
                elif path == 'break':
                    print('取消修改当前下载路径！')
                    c = input('\n按任意键返回功能菜单')
                    break
                else:
                    print('此路径不存在，请重新输入！')
                    c = input('\n按任意键返回功能菜单')
        elif op =='5':
            os.system('cls')
            cra.read_from_sqlite()
            c = input('\n按任意键返回功能菜单')
        elif op =='6':
             os.system('cls')
             num = cra.read_from_sqlite()
             if num ==0:
                 print('当前下载记录为0！')
                 break
             url = input('输入您想删除的下载记录的网址:(输入[all]删除全部下载记录！)')
             url = cra.clean_word(url)
             cra.delete_record_from_sqlite(url)
             c = input('\n按任意键返回功能菜单')
        elif op == '7':
            print('默认批量下载多进程数为：[4]')
            print('当前设置批量下载多进程数为：[%s]'% process_num)
            print('此设置根据您电脑CPU核数和性能决定，建议不要设置过大，范围：[1~8] ')
            while True:
                try:
                    num = int(input('您设置批量下载多进程数量：'))
                    if num>0 and num<=8:
                        process_num = num
                    else: raise Exception
                    break
                except Exception as e:
                    print('请输入合法1~8之间的数字！')
            c = input('按任意键返回功能菜单！')
        elif op == '0':
            os.system('cls')
            introduce = '''
##百度文库下载器##

#### 注意：运行此程序确保电脑有火狐浏览器。####

###实现的意义###:
支持对百度文库所有能浏览的学习资料，学术论文，工作手册等所有文档（pdf,word,txt,ppt）
非常便利（免登陆，消费劵)，稳定保证原文档(包括带有复杂图表插图)并支持批量的下载到本地。
并保证此程序绝对绿色，安全。
###声明###：
本程序原理仅是模拟浏览器以截图文章到本地形式，软件开放初衷是方便大家学习时，下载各种资料到本地离线使用，
不带有盈利目的，更请不要用此程序下载文档来获取利益。同时百度文库上文档也都是百度账号的用户自愿上传，
不存在侵权行为。

###提示###：
这是格格下载器1.1版本，批量下载，保存历史下载纪录等功能都已补充，交互界面待后续开发完善，遇到八阿哥（bug）和意见可以email,qq作者。

###开发作者###：
SGG
Email:529674242@qq.com
'''
            print(introduce)
            c = input('按任意键返回功能菜单！')
            if c == 'sgg':
                os.system('cls')
                loves = '\n格格是世界上最胖（棒）的女孩，，2018年加油！'
                print(loves)
                c = input('按任意键返回功能菜单！')
        elif op == 'exit':
            return
        else:
            print('输入不合法，请重新输入！！')
            c = input('按任意键返回功能菜单！')


# def read_from_momgo(self):
#     ulist = self.collection.find_and_modify({'status_detail': 0}, update={'$set': {'status_detail': 1}})
#     if ulist == None : return None
#     url = ulist['article_url']
#     id = ulist['article_id']
#     print('url:',url,'\t id:',id)
#     return url,id

# def update_mongo_done(self,id):
#     self.collection.update({'article_id':id}, {'$set': {'status_detail': 2}})

# def write_to_sqls(self, item):
#     sql = "INSERT INTO article_detail_new(article_url_md5, article_url, article_format, article_title," \
#           "article_classify, article_content) VALUES ('%s', '%s', '%s', '%s', '%s', '%s')" \
#           % (item['article_url_md5'], item['article_url'], item['article_format'], item['article_title'],
#              item['article_classify'], item['article_content'])
#     try:
#         print('sql:\n',sql)
#         self.cursor.execute(sql)
#         self.db.commit()
#     except Exception as e:
#         print('Add sqls failed:',e)
#     else : print('[%s] 文章详情 hava successful writed to sql service!'% (self.article_title))

# def run(self,fpath = None):
#     '''
#     从mongo中获取要下载文件的url，进行批量下载
#     :param fpath: 下载文件路径，空则默认下载到程序同一目录下
#     :return:
#     '''
#     wait_time = 1
#     while True:
#         url,id= self.read_from_momgo()
#         if url == None:
#             if wait_time >= 24*3600+10: #超过一天没有数据更新就停止
#                 print('Mongo数据库里已经没有更新的链接，请重新尝试启动！')
#                 return
#             sleep(wait_time)
#             wait_time <<=2
#             continue
#         self.test_one(url = url,id = id,fpath= fpath)
#         wait_time = 1

if __name__ == '__main__':
    multiprocessing.freeze_support()
    run_menu()



