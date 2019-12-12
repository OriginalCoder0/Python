
### 问题描述


本周课程主要讲解Python网络爬虫的基础内容。具体有：网页信息解析库的使用（Xpath，BeautifulSoup，PyQuery），Fiddler抓包工具和浏览器的伪装介绍、Ajax的信息爬取和验证码的识别： 

- **分页爬取豆瓣网图书Top250信息**，并分别使用三种网页信息解析库（Xpath，BeautifulSoup，PyQuery），并将信息写入文件中： 
  网址：<https://book.douban.com/top250?start=0> 



![](https://gitee.com/luhuadong/Python_Learning/raw/master/8th_week/homework/image/%E8%B1%86%E7%93%A3%E5%9B%BE%E4%B9%A6250.png)

![](https://gitee.com/luhuadong/Python_Learning/raw/master/8th_week/homework/image/%E8%B1%86%E7%93%A3%E5%9B%BE%E4%B9%A6250-%E5%91%BD%E4%BB%A4%E8%A1%8C.png)



- 访问京东商城网址，选择多个商品放入购物车后查看自己的购物车，显示效果如下 。请**使用Python爬取京东商城网址购物车中的所有商品信息**: 
  如URL地址：<https://cart.jd.com/cart.action> 



![](https://gitee.com/luhuadong/Python_Learning/raw/master/8th_week/homework/image/%E4%BA%AC%E4%B8%9C%E8%B4%AD%E7%89%A9%E8%BD%A64items.png)

![](https://gitee.com/luhuadong/Python_Learning/raw/master/8th_week/homework/image/%E4%BA%AC%E4%B8%9C%E8%B4%AD%E7%89%A9%E8%BD%A64items-%E5%91%BD%E4%BB%A4%E8%A1%8C.png)



- 访问百度图片网站，在搜索框中输入“街拍”并点击搜索按钮，具体效果如下，请使用python程序爬取搜索的图片，并存储到指定目录下。 
  具体参考URL地址：<http://image.baidu.com> 

![](https://gitee.com/luhuadong/Python_Learning/raw/master/8th_week/homework/image/%E7%99%BE%E5%BA%A6%E8%A1%97%E6%8B%8D.png)

![](https://gitee.com/luhuadong/Python_Learning/raw/master/8th_week/homework/image/%E7%99%BE%E5%BA%A6%E8%A1%97%E6%8B%8D-%E6%9C%AC%E5%9C%B0.png)



### 解题提示

1. 第一道题请参考《豆瓣电影Top250信息爬取》实战。 
2. 采用浏览器伪装技术获取京东购物车信息（维持Cookie信息） 
3. 第三道题请参考Ajax数据爬取（如今日头条的美图爬取） 



### 批改标准

- 豆瓣图书Top250信息爬取（30分） 
- 京东购物车商品信息爬取（30分） 
- 百度图片的关键字“街拍”搜索图片信息爬取（30分）。 
- 其他项：(10分)（文件结构清晰，代码整洁，要求适量的注释）。
