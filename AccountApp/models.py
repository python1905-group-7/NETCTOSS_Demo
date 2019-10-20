from django.db import models


class Account(models.Model):
    recommender_id = models.IntegerField(null=True)
    login_name = models.CharField(max_length=32)
    login_passwd = models.CharField(max_length=256)
    status = models.BooleanField(default=True)
    create_date = models.DateTimeField(auto_now=True)
    pause_date = models.DateTimeField(null=True)
    close_date = models.DateTimeField(null=True)
    real_name = models.CharField(max_length=32)
    idcard_no = models.CharField(max_length=64)
    birthdate = models.DateTimeField(null=True)
    gender = models.CharField(max_length=8, null=True)
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