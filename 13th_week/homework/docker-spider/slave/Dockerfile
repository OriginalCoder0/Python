FROM python:alpine
#COPY . /code
VOLUME ["/code"]

# 更新apk源并安装依赖
RUN apk update && \
	apk add --no-cache gcc openssl-dev openssl libressl libc-dev linux-headers libffi-dev libxml2-dev libxml2 libxslt-dev

# 更新setuptools并安装Python模块
RUN pip install --upgrade setuptools && \
	pip install requests lxml scrapy redis scrapy-redis

WORKDIR /code/aobag/aobag/spiders
#EXPOSE 5000
CMD ["scrapy", "runspider", "customer.py"]
