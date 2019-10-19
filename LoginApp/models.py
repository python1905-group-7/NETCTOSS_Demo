from django.db import models


# Create your models here.
class AdminInfo(models.Model):
    # 管理员用户名
    admin_code = models.CharField(max_length=32)

    # 管理员密码
    password = models.CharField(max_length=32)

    # 管理员姓名
    name = models.CharField(max_length=32)

    # 管理员手机号码
    telephone = models.CharField(max_length=32)

    # 管理员邮箱
    email = models.CharField(max_length=32)

    # 账号注册时间
    enrolldate = models.DateField()

    class Meta:
        db_table = 'ADMIN_INFO'
