from django.db import models

# Create your models here.
class Cost(models.Model):
    name=models.CharField(max_length=32)
    base_duration=models.CharField(max_length=32)
    base_cost=models.IntegerField()
    unit_cost=models.FloatField()
    status=models.BooleanField(default=False)
    descr=models.CharField(max_length=256)
    creatime=models.DateTimeField(auto_created_add=True)
    startime=models.DateTimeField(auto_now=True)
    cost_type=models.NullBooleanField()

    class Meta:
        db_table='cost'