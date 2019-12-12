from django.db import models

# Create your models here.

class Stu(models.Model):
    ''' 自定义 Stu 表对应的 Model 类 '''
    # 定义属性：默认主键自增 id 字段可不写
    id = models.AutoField(primary_key=True)
    name = models.CharField('姓名', max_length=16)
    age = models.SmallIntegerField('年龄')
    sex = models.CharField('性别', max_length=1)
    classid = models.CharField('班级', max_length=8)

    # 定义默认输出格式
    def __str__(self):
        return "%d:%s:%d:%s:%s"%(self.id, self.name, self.age, self.sex, self.classid)

    # 自定义对应的表名，默认表名：myapp_stu
    class Meta:
        db_table="stu"
        verbose_name = '浏览学生信息'
        verbose_name_plural = '学生信息管理'
