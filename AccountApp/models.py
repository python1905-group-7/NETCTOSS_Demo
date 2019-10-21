from django.db import models


class Recommender(models.Model):
    # 推荐人身份证
    idcard_no = models.CharField(max_length=32)

    class Meta:
        db_table = 'recommender'


class Account(models.Model):
    # 推荐人ID
    recommender_id = models.IntegerField(null=True)
    # 账号名
    login_name = models.CharField(max_length=32)
    # 密码
    login_passwd = models.CharField(max_length=256)
    # 账号状态
    status = models.CharField(max_length=4, default='1')
    # 账号创建时间
    create_date = models.DateTimeField(auto_now_add=True)
    # 账号暂停时间
    pause_date = models.DateTimeField(null=True)
    # 账号关闭时间
    close_date = models.DateTimeField(null=True)
    # 真实姓名
    real_name = models.CharField(max_length=32)
    # 身份证
    idcard_no = models.CharField(max_length=64)
    # 出生时间
    birthdate = models.DateTimeField()
    # 性别
    gender = models.CharField(max_length=8, null=True)
    # 职业
    occupation = models.CharField(max_length=32, null=True)
    # 电话号码
    telephone = models.CharField(max_length=32)
    # 邮箱
    email = models.CharField(max_length=64, null=True)
    # 邮箱地址
    mailaddress = models.CharField(max_length=128, null=True)
    # 邮编
    zipcode = models.CharField(max_length=128, null=True)
    qq = models.CharField(max_length=32, null=True)
    # 上一次登录时间
    last_login_time = models.DateTimeField(null=True)
    # 上一次登录IP
    last_login_ip = models.CharField(max_length=64, null=True)

    class Meta:
        db_table = 'ACCOUNT'

    def get(self):
        return [self.id, self.real_name, self.idcard_no, self.login_name, self.status, self.create_date,
                self.last_login_time]
