from django.urls import path
from .views import CheckoutSessionView, StripeWebhook

urlpatterns = [
    path('checkout_session', CheckoutSessionView.as_view(), name='checkout_session'),
    path('webhook', StripeWebhook.as_view(), name='stripe_webhook'),
]
