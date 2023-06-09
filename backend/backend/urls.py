"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import api.views.generalView as views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import routers, serializers, viewsets
from rest_framework.permissions import IsAuthenticated
from api.views.postView import PostAPIView, PostDetailAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    # Account
    path('api/v1/create-account/', views.CreateUserView.as_view(), name='create-account'),
    path('api/v1/login/', views.LoginUserView.as_view(), name='login'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('posts/', PostAPIView.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetailAPIView.as_view(), name='post-detail')
]
