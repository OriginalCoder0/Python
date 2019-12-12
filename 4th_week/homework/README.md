## 第四周作业

本周作业代码位于 album 目录

### 0. 效果图

![](https://gitee.com/luhuadong/Python_Learning/raw/master/4th_week/homework/images/album_home.png)

![](https://gitee.com/luhuadong/Python_Learning/raw/master/4th_week/homework/images/album_index.png)

![](https://gitee.com/luhuadong/Python_Learning/raw/master/4th_week/homework/images/album_add.png)

![](https://gitee.com/luhuadong/Python_Learning/raw/master/4th_week/homework/images/album_update.png)

![](https://gitee.com/luhuadong/Python_Learning/raw/master/4th_week/homework/images/album_pic.png)

### 1. 创建 Django 项目

创建 album 在线相册信息管理项目：

```
$ django-admin startproject album
$ cd album/
```

在 album 项目中，创建 myapp 应用：

```
$ python3 manage.py startapp myapp
```

新建 templates 目录和 static 目录，pics 目录用于保存后续上传的图片：

```
$ mkdir templates static
$ mkdir -p static/pics
```

修改 settings.py 文件：

```
ALLOWED_HOSTS = ["localhost", "127.0.0.1", "192.168.3.119"]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'album',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
```

在 MySQL 数据库中创建一个 album 数据库，Collation 选择 `utf8_general_ci` 。

在 album/\_\_init\_\_.py 添加如下内容：

```
import pymysql
pymysql.install_as_MySQLdb()
```

创建数据表及数据迁移：

```
$ python3 manage.py makemigrations
$ python3 manage.py migrate
```

### 2. 注意事项

在您的机器上运行该项目，您可能需要修改数据库连接的相关信息，包括 NAME、USER、PASSWORD 等参数。