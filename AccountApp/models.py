from django.db import models


# Create your models here.
class Account(models.Model):
    #推荐人
    recommender_id = models.IntegerField(null=True)
    #登陆名
    login_name = models.CharField(max_length=32)
    # 登陆密码
    login_passwd = models.CharField(max_length=256)
    # 状态
    status = models.CharField(max_length=4, default=1)
    # 创建时间
    create_date = models.DateTimeField(auto_now=True)
    #暂停时间
    pause_date = models.DateTimeField(null=True)
    # 关闭时间
    close_date = models.DateTimeField(null=True)
    # 真实名字？
    real_name = models.CharField(max_length=32)
    # 身份证
    idcard_no = models.CharField(max_length=64)
    # 出生日期
    birthdate = models.DateTimeField(null=True)
    # 性别
    gender = models.CharField(max_length=8, null=True)
    #职业
    occupation = models.CharField(max_length=32, null=True)
    telephone = models.CharField(max_length=32)
    email = models.CharField(max_length=64, null=True)
    mailaddress = models.CharField(max_length=128, null=True)
    zipcode = models.CharField(max_length=128, null=True)
    qq = models.CharField(max_length=32, null=True)
    last_login_time = models.DateTimeField(null=True)
    last_login_ip = models.CharField(max_length=64, null=True)

    class Meta:
        db_table = 'ACCOUNT'

    def get(self):
        return [self.id, self.real_name, self.idcard_no, self.login_name, self.status, self.create_date,
                self.last_login_time]

