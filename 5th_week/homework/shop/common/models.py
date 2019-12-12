from django.db import models
from datetime import datetime


# Create your models here.


class Users(models.Model):
    ''' 用户信息模型 '''
    username = models.CharField(max_length=32)
    name = models.CharField(max_length=16)
    password = models.CharField(max_length=32)
    sex = models.IntegerField(default=1)
    address = models.CharField(max_length=255)
    code = models.CharField(max_length=6)
    phone = models.CharField(max_length=16)
    email = models.CharField(max_length=50)
    state = models.IntegerField(default=1)
    addtime = models.DateTimeField(default=datetime.now)

    def toDict(self):
        ''' 返回当前数据对象信息的字典类型格式 '''
        return {'id': self.id, 'username': self.username, 'name': self.name, 'password': self.password, 'address': self.address, 'phone': self.phone, 'email': self.email, 'state': self.state, 'addtime': self.addtime}

    class Meta:
        db_table = "users"


class Types(models.Model):
    ''' 商品类别模型 '''
    name = models.CharField(max_length=32)
    pid = models.IntegerField(default=0)
    path = models.CharField(max_length=255)

    class Meta:
        db_table = "type" # 没有s！


class Goods(models.Model):
    ''' 商品信息模型 '''
    typeid = models.IntegerField()
    goods = models.CharField(max_length=32)
    company = models.CharField(max_length=50)
    content = models.TextField()
    price = models.FloatField()
    picname = models.CharField(max_length=255)
    store = models.IntegerField(default=0)
    num = models.IntegerField(default=0)
    clicknum = models.IntegerField(default=0)
    state = models.IntegerField(default=1)
    addtime = models.DateTimeField(default=datetime.now)

    def toDict(self):
        return {'id': self.id, 'typeid': self.typeid, 'goods': self.goods, 'company': self.company, 'price': self.price, 'picname': self.picname, 'store': self.store, 'num': self.num, 'clicknum': self.clicknum, 'state': self.state}

    class Meta:
        db_table = "goods"
