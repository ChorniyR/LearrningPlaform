from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APIRequestFactory, APIClient
from rest_framework.test import force_authenticate
import requests

from django.test import TestCase
from model_bakery import baker

from .views import CoursesViewSet


class PermissionsTest(TestCase):
    def setUp(self):
        user = User.objects
        user = User.objects.create_user('user', 'user@mail.com', 'user')

    def test_has_basic_user_permissions_to_create_course(self):
        response = requests.post('http://127.0.0.1:8000/courses/', headers={
            'Authorization': 'Basic cm9tYTIwMTI1OnF3ZXJ0eTEyMzIyMw=='
        })
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
