from django.urls import path, include
from .views import *
urlpatterns = [
    path('api/paypal/', PaymentAPI.as_view()),
    path('paypal/', include("paypal.standard.ipn.urls")),
]
