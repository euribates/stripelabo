from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save 
from django.urls import reverse_lazy

from . import stripe_utils
# Create your models here.


class StripIntent(models.Model):
    intent_id = models.CharField(max_length=27, primary_key=True)
    amount = models.IntegerField()
    currency = models.CharField(max_length=3, default='gbp')
    status = models.CharField(max_length=32)
    create_dttm = models.DateTimeField(auto_now_add=True)
    update_dttm = models.DateTimeField(auto_now=True)
    delete_dttm = models.DateTimeField(blank=True, null=True, default=None)


class Customer(models.Model):
    customer_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    email = models.EmailField(max_length=80)
    stripe_id = models.CharField(max_length=20)

    @property
    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def get_absolute_url(self):
        return reverse_lazy('payments:view_customer', kwargs={'pk': self.customer_id})

    def description(self):
        return 'Customer[{}] {} <{}>'.format(
            self.pk,
            self.full_name,
            self.email,
            )

    def save(self, *args, **kwargs):
        if not self.stripe_id:
            self.stripe_id = stripe_utils.create_stripe_for_customer(self)
        return super().save(*args, **kwargs)
