from django.db import models


# Create your models here.
class Cost(models.Model):
    name = models.CharField(max_length=32)
    base_duration = models.CharField(max_length=32, null=True)
    base_cost = models.FloatField(null=True)
    unit_cost = models.FloatField(null=True)
    status = models.NullBooleanField(default=False)
    descr = models.CharField(max_length=256)
    creatime = models.DateTimeField(auto_now_add=True)
    startime = models.DateTimeField(auto_now=True, null=True)
    cost_type = models.CharField(max_length=16)

    class Meta:
        db_table = 'COST'
