
### 实现的功能
- word,pdf类型文件下载为高清分辨率pdf文件。
- txt文件下载还原txt文件。
- PPT幻灯片下载为高清图集。


### 注意 
   - 在服务器上直接运行.py文件后关闭时，隐藏的firefox并没有关闭，需要手动或运行```kill_process.py```结束其进程。
   - 在运行该程序时，不要打开火狐浏览器（Firefox）。
   - 每运行一个```cralw.run()```程序是单线程,单进程的,可以一次性打开多个程序之间互不影响，形成多进程运行。
   
### 每个函数的参数及作用详见代码

### 程序流程图
![流程图](http://pic.suiyiyun.cn/598486/1.jpg)



### 实现的主要技术：
- 对HTTP协议理解，使用python的requests库分析服务器返回response各种资源（html,json等）
- 使用测试工具selenium模拟对浏览器各种操作
- 利用测试工具selenium与解析库Beautifulsoup的CSS选择器方式对网页元素的定位与解析
- 相关文档爬取运用的广度优先算法
- 批量下载的使用多线程技术 
- 调用reportlab库将多张图片合成一个pdf文件

### 实现主要难点：
- 对百度文库不同类型文件的下载策略的分析（pdf，txt，ppt文件的解析方式都不相同）：
- 选择selenium + firefox截图方案，并配置环境 
- selenium操作浏览器的一些细节（为了要截图时干净，要对网页除文章以外广告等元素隐藏，删除，更新等）
- 百度动态加载每一页内容，需要边滑动浏览器，边截图当前页面。
- 当前浏览器截图时浏览器大小等参数需要调试，使截出图片高清无瑕疵。

### 实现的过程参考资料工具：

- [python3.6+selenium+firefox环境配置](http://blog.csdn.net/chaowanghn/article/details/54708275)
- [利用 Python + Selenium 实现页面截图](https://www.jianshu.com/p/7ed519854be7)
- [selenium 常见元素定位方法和操作](http://blog.csdn.net/eastmount/article/details/48108259)
- [Beautifulsoup4.04  文档](http://beautifulsoup.readthedocs.io/zh_CN/latest/)
- [pyhton正则表达式指南](http://www.cnblogs.com/huxi/archive/2010/07/04/1771073.html)
- [在线测试正则表达式](http://tool.oschina.net/regex/)

- [python3.6程序打包exe](http://blog.csdn.net/lqzdreamer/article/details/77917493)
- [使用python显示当前系统中的所有进程并关闭某一进程](https://www.cnblogs.com/ljmjjy0820/p/7896154.html)

- [Mongo文档](http://www.runoob.com/mongodb/mongodb-update.html)

