在命令行启动

```
$ python3 hello.py runserver
```



安装 Gunicorn

```
$ pip3 install gunicorn==19.3.0
```

安装完毕，可以通过 gunicorn 命令来运行

```
$ gunicorn hello --log-file=-
```
