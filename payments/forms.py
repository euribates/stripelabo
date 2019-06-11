#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms

from . import models


class NewCustomerForm(forms.ModelForm):

    class Meta:
        model = models.Customer
        fields = [
            'first_name',
            'last_name',
            'email',
            'stripe_id',
            ]


    email = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Email'})
        )
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'First name'})
        )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Last name'})
        )
    stripe_id = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Stripe ID.'})
        )

