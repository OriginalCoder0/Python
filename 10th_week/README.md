#  第10周：Python网络爬虫进阶实战（中）

本周课程主要讲解网络爬虫进阶实战的应用。具体有：

- Selenium 动态渲染页面信息爬取
- Scrapy 框架与 Selenium 的结合
- IP 代理的设置、收费代理服务的使用
- 分布式爬虫原理、Scrapy 分布式的实现
- MongoDB 和 Redis 非关系型数据库的使用



关于**实战案例**有：

- 爬取淘宝网站的商品信息
- 微信公众号文章信息爬取实战



通过本周学习，让学员掌握动态渲染页面爬取、代理的使用、Redis 非关系型数据库操作，使用 Redis 非关系数据存储爬取信息、Linux 操作系统的使用，Docker 容器操作、基于 Scrapy 分布式爬虫实现。



---

### 本周作业

#### 问题描述

- 使用Scrapy框架和Selenium配合爬取**京东网站商品列表信息**（>=50页）
  - 网址：<https://list.jd.com/list.html?cat=670,671,672>
  - 爬取字段信息由自己定制，这里不做要求。
- 使用 scrapy-redis 分布式爬取 **CSDN 学院平台中所有课程信息**
  - 如：<https://edu.csdn.net/courses/k> 爬取所有课程详情 url 地址  
  - 然后再通过队列 url 中对应的每个课程详情信息，使用分布式爬取。  如：<https://edu.csdn.net/course/detail/5466>
  - 要求内容：课程标题、课时、讲师、适合人群、学习人数、价格、课程大纲。



#### 解题提示

1. 第一道题请参考 Scrapy+selenium 课堂案例。
2. 第二道题参考 Scrapy+Redis 爬虫实战案例。



#### 批改标准

- Scrapy-Selenium 爬取京东商品信息（45分）
- Scrapy-Redis 分布式爬取 CSDN 学院课程信息（45分）
- 其他项（10分）
  - 文件结构清晰
  - 代码整洁
  - 适量的注释



