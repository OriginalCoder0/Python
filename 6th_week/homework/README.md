# 第6周作业：商城前台 & 后台完善

### 作业说明

Django 项目代码位于 myobject 目录，shopdb.sql 为数据库导出文件。

> 如果运行出错，请与我联系！



#### 完成功能

- 商城项目前后台搭建
- 会员登录和注册功能
- 会员中心个人信息浏览和编辑
- 会员密码重置功能
- 商城首页商品展示（根据点击量，显示在“热品推荐”栏目）
- 前后台验证码模块分离



### 截图

#### （1）会员前台注册

![](https://gitee.com/luhuadong/Python_Learning/raw/master/6th_week/homework/images/django-shop-vip-register.png)

#### （2）会员中心-个人信息

![](https://gitee.com/luhuadong/Python_Learning/raw/master/6th_week/homework/images/django-shop-vip-info.png)

#### （3）会员中心-修改密码

![](https://gitee.com/luhuadong/Python_Learning/raw/master/6th_week/homework/images/django-shop-vip-reset-password.png)

#### （4）商城首页-热品推荐

![](https://gitee.com/luhuadong/Python_Learning/raw/master/6th_week/homework/images/django-shop-sell-hot.png)

#### （5）会员订单查询

![](https://gitee.com/luhuadong/Python_Learning/raw/master/6th_week/homework/images/django-shop-vip-orders.png)

#### （6）后台订单处理

![](https://gitee.com/luhuadong/Python_Learning/raw/master/6th_week/homework/images/django-shop-admin-orders.png)





### 操作记录



创建数据库和数据表，可以偷懒，直接导入 shopdb.sql：

```
$ mysql -u root -p shopdb < shopdb.sql
```

创建 Django 项目：

```
$ django-admin startproject shop
```

修改 shop/settings.py：

```

```

在 shop/\_\_init\_\_.py 中添加：

```
import pymysql
pymysql.install_as_MySQLdb()
```

数据迁移：

```
$ python3 manage.py migrate
```

启动项目：

```
$ python3 manage.py runserver
```

导出数据库：

```
mysqldump -u root -p shopdb > shopdb.sql
```



