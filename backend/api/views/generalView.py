from django.middleware.csrf import get_token
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authtoken.models import Token
from ..serializers.generalSerializer import UserSerializer, LoginSerializer
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


# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.permissions import AllowAny
# from django.contrib.auth import authenticate
# from serializer import LoginSerializer


# class LoginView(APIView):
#     permission_classes = [AllowAny]

#     def post(self, request):
#         serializer = LoginSerializer(data=request.data)
#         if serializer.is_valid():
#             username = serializer.validated_data['username']
#             password = serializer.validated_data['password']
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 # User is authenticated
#                 # You can generate tokens, set cookies, or return any other relevant data
#                 return Response({'message': 'Login successful'})
#             else:
#                 # Authentication failed
#                 return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
#         else:
#             # Serializer validation failed
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
