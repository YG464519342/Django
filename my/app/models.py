from django.db import models



class UserInfo(models.Model):
    name = models.CharField(verbose_name='用户名', max_length=16)  #varchar
    pwd = models.CharField(verbose_name='密码', max_length=64)  #varchar
    age = models.IntegerField(verbose_name='年龄')  #int
    email=models.CharField(verbose_name='邮箱',max_length=16)  #varchar
    # 第一种 设置新增字段 设置可以为空
    city=models.CharField(verbose_name='城市',max_length=32,null=True,blank=True)
    #第二种 设置默认值
    #city=models.CharField(verbose_name='城市',max_length=32,default='上海')
    #终端提供默认值
    #city=models.CharField(verbose_name='城市',max_length=64)


class Department(models.Model):
    title = models.CharField(verbose_name='标题', max_length=32)
    count = models.IntegerField(verbose_name='人数')
