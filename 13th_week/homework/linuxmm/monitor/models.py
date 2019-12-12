from django.db import models
from datetime import datetime

# Create your models here.

class User(models.Model):

    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    email = models.CharField(max_length=32)
    cdate = models.DateTimeField(default=datetime.now)

    class Meta:
        db_table = 'user' # 指定表名


class Host(models.Model):
    ''' Host 数据表模型 '''

    #id = models.IntegerField()
    tag = models.CharField(max_length=32)
    ip = models.CharField(max_length=32)
    cpu = models.IntegerField()
    mem = models.IntegerField()
    disk = models.IntegerField()
    stat = models.IntegerField(default=0)
    cdate = models.DateTimeField(default=datetime.now)

    def toDict(self):
        ob = {
            'id'   : self.id,
            'tag'  : self.tag,
            'ip'   : self.ip,
            'cpu'  : self.cpu,
            'mem'  : self.mem,
            'disk' : self.disk,
            'stat' : self.stat,
            'cdate': self.cdate
        }
        return ob

    class Meta:
        db_table = 'host' # 指定表名