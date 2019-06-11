import logging

from django.conf import settings
import stripe

stripe.api_key = settings.STRIPE_API_KEY

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def list_all_customers(limit=25):
    customers = stripe.Customer.list(limit=25)
    return customers


def delete_customer(customer):
    logger.info('Delete stripe customer {}'.format(customer['id']))
    customer_id = customer['id']
    stripe.Customer.delete(customer_id)


def create_stripe_for_customer(customer):
    description = "Customer for {} <{}>".format(
        customer.full_name,
        customer.email,
        )
    stripe_costumer = stripe.Customer.create(
        name=customer.full_name,
        email=customer.email,
        description=description,
        )
    return stripe_costumer.id
