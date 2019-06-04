from django.shortcuts import render
from django.conf import settings

import stripe
from . import models

# Create your views here.

def single_payment(request):
    stripe.api_key = settings.STRIPE_API_KEY
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
