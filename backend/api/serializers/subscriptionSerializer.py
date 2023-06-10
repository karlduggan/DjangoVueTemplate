from rest_framework import serializers
from ..models.subscriptionModel import Subscription

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ['id', 'name', 'price', 'description', 'duration']
        read_only_fields = ['id']