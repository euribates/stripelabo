from django.db import models

# Create your models here.


class StripIntent(models.Model):
    intent_id = models.CharField(max_length=27, primary_key=True)
    amount = models.IntegerField()
    currency = models.CharField(max_length=3, default='gbp')
    status = models.CharField(max_length=32)
    create_dttm = models.DateTimeField(auto_now_add=True)
    update_dttm = models.DateTimeField(auto_now=True)
    delete_dttm = models.DateTimeField(blank=True, null=True, default=None)
