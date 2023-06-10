
from django.middleware.csrf import get_token
from django.http import HttpResponse
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import AllowAny
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework import generics, permissions
from rest_framework import status
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer, LoginSerializer
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password


def set_csrf_token(request):
    response = HttpResponse()
    cookie = get_token(request)
    response.set_cookie('csrftoken', cookie)
    print("Cookie: {}".format(cookie))
    return response


def set_token(request):
    response = HttpResponse()
    response.set_cookie('csrftoken', get_token(request))
    return response


class CreateUserView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            password = make_password(serializer.validated_data['password'])
            user = serializer.save(password=password)
            if user:
                token = Token.objects.create(user=user)
                json = serializer.data
                json['token'] = token.key
                return Response(json, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginUserView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # User is authenticated
            token, _ = Token.objects.get_or_create(user=user)
            response = Response({'token': token.key})
            csrf_token = get_token(request)
            response['X-CSRFToken'] = csrf_token

            return response
            # return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({'error': 'Invalid email or password'}, status=status.HTTP_401_UNAUTHORIZED)


from .serializers import PaymentSerializer
from .models import Payment

class PaymentView(APIView):
    def get(self, request):
        payments = Payment.objects.all()
        serializer = PaymentSerializer(payments, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


from .serializers import PermissionSerializer
from .models import Permission

class PermissionView(APIView):
    def get(self, request):
        permissions = Permission.objects.all()
        serializer = PermissionSerializer(permissions, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PermissionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


from .serializers import ProfileSerializer
from .models import Profile

class ProfileView(APIView):
    def get(self, request):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

from .serializers import SubscriptionSerializer
from .models import Subscription

class SubscriptionView(APIView):
    def get(self, request):
        subscriptions = Subscription.objects.all()
        serializer = SubscriptionSerializer(subscriptions, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SubscriptionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
