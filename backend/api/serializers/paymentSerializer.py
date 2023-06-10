from rest_framework import serializers
from ..models.paymentModel import Payment

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'user', 'amount', 'timestamp']
        read_only_fields = ['id', 'timestamp']