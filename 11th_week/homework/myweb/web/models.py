from django.db import models

# Create your models here.


class Books(models.Model):
    """ 图书信息模型 """

    title = models.CharField(max_length=255) #书名
    author = models.CharField(max_length=64) #作者
    press = models.CharField(max_length=255)  #出版社
    original = models.CharField(max_length=255)#原作名
    translator = models.CharField(max_length=128)#译者
    imprint = models.CharField(max_length=128)#出版年
    pages = models.IntegerField(default=0)#页数
    price = models.FloatField() #定价
    binding = models.CharField(max_length=32) #装帧
    series = models.CharField(max_length=128) #丛书
    isbn = models.CharField(max_length=128) #ISBN
    score = models.CharField(max_length=128) #评分
    number = models.IntegerField(default=0) #评论人数

    class Meta:
        db_table = "books"  # 更改表名