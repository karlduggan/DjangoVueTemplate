from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
