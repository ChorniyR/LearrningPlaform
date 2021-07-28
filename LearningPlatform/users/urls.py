from django.urls import path
from rest_framework import routers

from .views import RegisterView

app_name = 'users'
urlpatterns = [
    path('registration/', RegisterView.as_view()),
]
