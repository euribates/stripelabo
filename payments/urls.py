#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.urls import path

from . import views

app_name = 'payments'

urlpatterns = [
    path('single', views.single_payment, name="single"),
]
