from django.db import models
from datetime import datetime

# Create your models here.

class Photos(models.Model):
	""" 相册模型，对应 photos 数据表 """
	title = models.CharField(max_length=32)
	filename = models.CharField(max_length=32)
	comment = models.CharField(max_length=128)
	# “喜欢”标记
	like = models.IntegerField(default=0)
	addtime = models.DateTimeField(default=datetime.now)

	class Meta:
		db_table = "photos"