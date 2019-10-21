from django.db import models

# Create your models here.
from AccountApp.models import Account
from FeeApp.models import Cost


class Service(models.Model):
    # account
    account = models.ForeignKey(Account)
    # cost
    cost = models.ForeignKey(Cost)
    # ip地址
    unix_host = models.CharField(max_length=32)
    # os账号
    os_username = models.CharField(max_length=32)
    # 密码
    login_passwd = models.CharField(max_length=512)
    # 状态
    status = models.NullBooleanField(default=True)
    # 开通时间
    create_date = models.DateTimeField(auto_now_add=True)
    # 暂停时间
    pause_date = models.DateTimeField(null=True)
    # 停止时间
    close_date = models.DateTimeField(null=True)


    class Meta:
        db_table = 'SERVICE'

