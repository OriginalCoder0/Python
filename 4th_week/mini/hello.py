import os
import sys

from django.conf import settings

DEBUG = os.environ.get('DEBUG', 'on') == 'on'

SECRET_KEY = os.environ.get('SECRET_KEY', os.urandom(32))

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost').split(',')


# 这些设置通常会包含在 settings.py 文件

settings.configure(
    DEBUG=DEBUG,
    SECRET_KEY=SECRET_KEY,
    ROOT_URLCONF=__name__,
    ALLOWED_HOSTS=ALLOWED_HOSTS,
    MIDDLEWARE_CLASSES=(
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ),
)

"""
settings.configure(
    DEBUG=True,
    SECRET_KEY='thisisthesecretkey',
    ROOT_URLCONF=__name__,
    MIDDLEWARE_CLASSES=(
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ),
)
"""


from django.conf.urls import url
from django.core.wsgi import get_wsgi_application
from django.http import HttpResponse


# 通常会放在应用程序内的 views.py 文件

def index(request):
    return HttpResponse('Hello World')


# 路由，通常放在根目录中的 urls.py 文件

urlpatterns = (
    url(r'^$', index),
)


# Web 服务器网关接口（WSGI）
# 每一个服务器都需要使用一个正确定义的 WSGI 应用
# Django 通过 get_wsgi_application 提供了一个用于创建这个应用的简单接口

application = get_wsgi_application()


# 典型的 Django 项目带有一个 manage.py 文件

if __name__ == "__main__":
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)

