#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import json

from django.conf import settings
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import DetailView

import stripe

from . import models
from . import forms

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

stripe.api_key = settings.STRIPE_API_KEY
# Create your views here.


def webhook(request):
    result = list(request.POST.items())
    logger.error("request.body is %s (%s)", request.body, type(request.body))
    event = json.loads(request.body)
    logger.error("event is %s (%s)", json.dumps(event, indent=4), type(event))
    logger.error("result is %s (%s)", result, type(result))
    return render(request, 'payments/webhook.html', {
        'request': request,
        'locals': locals(),
        'result': result,
        })


def list_customers(request):
    logger.info('View list_customers starts')
    customers = models.Customer.objects.all()
    return render(request, 'payments/list_customers.html', {
        'customers': customers,
        })


class CreateCustomerView(CreateView):

    model = models.Customer
    form_class = forms.NewCustomerForm
    context_object_name = 'customer'
    template_name = 'payments/customer_new.html'



class DetailCustomerView(DetailView):
    
    model = models.Customer


class DeleteCustomerView(DeleteView):
    
    model = models.Customer
    context_object_name = 'customer'
    success_url = reverse_lazy('payments:list_customers')


def single_payment(request):
    intent = stripe.PaymentIntent.create(
        amount=999,
        currency='eur',
        )
    models.StripIntent(
        intent_id=intent.id,
        amount=intent.amount,
        currency=intent.currency,
        status=intent.status,
        ).save()
    return render(request, 'payments/single.html', {
        'amount': intent.amount,
        'currency': intent.currency,
        'client_secret': intent.client_secret,
        'status': intent.status,
        'intent': intent,
        })


def charge_payment(request):
    
    return render(request, 'payments/charge.html', {
        'path_info': request.path_info,
        'keys': request.POST.keys(),
        'post': request.POST,
        })


