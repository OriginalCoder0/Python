# 第四周：Python Web 开发基础（下）

本周的内容是 Django 框架的基本知识，包括框架中的 URL 路由配置、Model 模型层、View 视图和 Template 模板等模块内容，并且可以使用它们构建自己的 Web 项目，完成对 MySQL 数据库信息的各种操作。以及项目中各种实用技能，如 Ajax、文件上传、搜索分页、富文本编辑器和中间件等。


**作业：**

通过本周学习使用 Django 框架完成一个《在线相册信息管理》，要求实现在线相册信息的增、删、改、查等操作，要求使用到的技术有：Django 框架、MySQL 数据存储、文件上传、图片缩放、数据分页，并提交数据库。

显示效果如下：

![图片](https://gitee.com/luhuadong/Python_Learning/raw/master/4th_week/images/homework_refer01.png)

![图片](https://gitee.com/luhuadong/Python_Learning/raw/master/4th_week/images/homework_refer02.png)

![图片](https://gitee.com/luhuadong/Python_Learning/raw/master/4th_week/images/homework_refer03.png)

![图片](https://gitee.com/luhuadong/Python_Learning/raw/master/4th_week/images/homework_refer04.png)

**思路：**

参考老师的课堂实例，首先实现数据的增、删、改、查操作，然后再考虑带图片上传的处理。
注意：相册中上传的图片不写入数据库，只要将上传的图片名信息写入表中即可。


**批改标准：**

 - Django 框架搭建（10分）
 - 相册信息添加功能（信息添加、图片上传和缩放）（30分）
 - 相册信息浏览（信息和图片的浏览，分页功能）（20分）
 - 相册信息编辑（信息编辑、可更换图片）（20分）
 - 相册信息删除（要求同时删除图片）（10分）
 - 文件结构清晰，代码整洁，要求适量的注释（10分）


