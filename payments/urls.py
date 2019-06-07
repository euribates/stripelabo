#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.urls import path

from . import views

app_name = 'payments'

urlpatterns = [
    path('customers', views.list_customers, name='list_customers'),
    path('webhook', views.webhook),
    path('single', views.single_payment, name="single"),
    path('single/charge', views.charge_payment, name="charge"),
]
