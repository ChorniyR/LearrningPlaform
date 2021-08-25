from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIClient, APITestCase
import json


class TestStepDetailView(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user('user', 'user@mail.com', 'user')
        self.client = APIClient()
        self.client.force_authenticate(self.user)
