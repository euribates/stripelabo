#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

app_name = 'payments'


urlpatterns = [
    path('customers/', views.list_customers, name='list_customers'),
    path('webhook', csrf_exempt(views.webhook)),
    path(
        'customer/create/',
        views.CreateCustomerView.as_view(),
        name="new_customer",
        ),
    path(
        'customer/<int:pk>/',
        views.DetailCustomerView.as_view(),
        name="view_customer",
        ),
    path(
        'customer/<int:pk>/delete/',
        views.DeleteCustomerView.as_view(),
        name="delete_customer",
        ),
    path('single', views.single_payment, name="single"),
    path('single/charge', views.charge_payment, name="charge"),
]
