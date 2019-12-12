# 第5周作业：商城后台

### 作业说明

Django 项目代码位于 shop 目录，shopdb.sql 为数据库导出文件。



### 截图

![](https://gitee.com/luhuadong/Python_Learning/raw/master/5th_week/homework/images/login.png)

![](https://gitee.com/luhuadong/Python_Learning/raw/master/5th_week/homework/images/users.png)

![](https://gitee.com/luhuadong/Python_Learning/raw/master/5th_week/homework/images/goods.png)



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



