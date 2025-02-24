from django.contrib import admin
from django.urls import path
from .views import UserSignupView

urlpatterns = [
    path('/register', UserSignupView.as_view(), name='register'),
]
