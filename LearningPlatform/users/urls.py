from django.urls import path
from rest_framework import routers

from .views import RegisterView, PasswordResetView

app_name = 'users'
urlpatterns = [
    path('registration/', RegisterView.as_view()),
    path('rest_password/', PasswordResetView.as_view())
]
