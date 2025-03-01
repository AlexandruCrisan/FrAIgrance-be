from django.urls import path
from .views import UserSignupView, CurrentUserView

urlpatterns = [
    path('register', UserSignupView.as_view(), name='register_user'),
    path('current', CurrentUserView.as_view(), name='current_user'),
]
