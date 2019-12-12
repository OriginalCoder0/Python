## 准备数据

### 创建数据库

```
CREATE DATABASE IF NOT EXISTS mydemo;

use mydemo;
```

### 创建数据表

```
CREATE TABLE stu(
	id int unsigned not null auto_increment PRIMARY KEY, 
	name char(16) not null, 
	age tinyint unsigned not null, 
	sex char(1) not null, 
	classid char(8)
);
```

### 插入数据

```
INSERT INTO stu(name,age,sex,classid) VALUES('Allen',20,'0','python07');
```

初步是这样的：

```
mysql> select * from stu;
+----+--------+-----+-----+----------+
| id | name   | age | sex | classid  |
+----+--------+-----+-----+----------+
|  1 | Allen  |  20 | 0   | python07 |
|  2 | Bob    |  20 | 0   | python07 |
|  3 | Carrie |  19 | 0   | python07 |
|  4 | Joe    |  20 | 0   | python07 |
|  5 | Elsa   |  21 | 0   | python07 |
|  6 | Herry  |  21 | 0   | python07 |
|  7 | James  |  22 | 0   | python07 |
|  8 | Ken    |  20 | 0   | python07 |
+----+--------+-----+-----+----------+
8 rows in set (0.00 sec)

```

---

## 使用 shell 交互模式操作数据库

```
$ python3 manage.py shell
```

### 逐条输入

```
from myapp.models import Stu

mod = Stu.objects


# 获取所有信息

lists = mod.all()

for v in lists:
	print(v)


# 获取单条信息

stu=mod.get(id=8)
stu.sex=1
stu.save()

```

---

## 在项目代码中操作数据库

在 myapp/views.py 中添加如下内容：

```
def stu(request):
	mod = Stu.objects
	list = mod.all()
	print(list)

	return HttpResponse("okay")"")
```

在 myapp/urls.py 中添加：

```
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^stu$', views.stu),
]
```

启动服务：

```
$ python3 manage.py runserver
```

浏览器输入 url ：<http://localhost:8000/myapp/stu>



---

## 数据迁移

```
$ python3 manage.py migrate

Operations to perform:
	Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
	Applying contenttypes.0001_initial... OK
	Applying auth.0001_initial... OK
	Applying admin.0001_initial... OK
	Applying admin.0002_logentry_remove_auto_add... OK
	Applying contenttypes.0002_remove_content_type_name... OK
	Applying auth.0002_alter_permission_name_max_length... OK
	Applying auth.0003_alter_user_email_max_length... OK
	Applying auth.0004_alter_user_username_opts... OK
	Applying auth.0005_alter_user_last_login_null... OK
	Applying auth.0006_require_contenttypes_0002... OK
	Applying auth.0007_alter_validators_add_error_messages... OK
	Applying auth.0008_alter_user_username_max_length... OK
	Applying sessions.0001_initial... OK

```

此时，在 mysql 数据库中增加了 10 张数据表

- auth_group
- auth_group_permissions
- auth_permission
- auth_user
- auth_user_groups
- auth_user_user_permissions
- django_admin_log
- django_content_type
- django_migrations
- django_session

### 创建管理员账号

```
$ python3 manage.py createsuperuser

Username (leave blank to use 'rudy'): admin
Email address: luhuadong@163.com
Password: admin123
Password (again): 
Superuser created successfully.
																			   '')
```
