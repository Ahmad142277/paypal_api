from django.conf import settings
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.urls import reverse
from paypal.standard.forms import PayPalPaymentsForm
from rest_framework.views import APIView
from .serializers import PaymentSerializer


class PaymentAPI(APIView):
    def post(self, request):
        serializer = PaymentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        description = serializer.validated_data['description']
        amount = serializer.validated_data['amount']
        invoice = serializer.validated_data['invoice']

        paypal_dict = {
            "business": settings.BUS,
            "amount": str(amount),
            "currency_code": "USD",
            "invoice": str(invoice),
            "item_name": description,
            "notify_url": request.build_absolute_uri(reverse('paypal-ipn')),
            "return_url": "http://localhost:3000/",  # Redirect URL after payment success
            "cancel_url": "http://localhost:3000/",  # Redirect URL after payment cancellation
        }

        # Create the instance.
        form_html = render_to_string('Payment.html', {'form': PayPalPaymentsForm(initial=paypal_dict)})
        return JsonResponse({"form": form_html})