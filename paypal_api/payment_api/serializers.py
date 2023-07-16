from rest_framework import serializers

class PaymentSerializer(serializers.Serializer):
    description = serializers.CharField()
    invoice=serializers.CharField()
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)
