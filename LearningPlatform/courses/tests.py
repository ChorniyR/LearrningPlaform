from django.contrib.auth.models import User
from django.test import TestCase
from model_bakery import baker
from rest_framework import status
from rest_framework.test import APIClient

from .models import Course


class PermissionsTest(TestCase):
    def setUp(self):
        user = User.objects
        user = User.objects.create_user('user', 'user@mail.com', 'user')

    @staticmethod
    def get_staff_user():
        user = User.objects.create_user(is_staff=True, username='staff', password='staff', email='staff@staff.com')
        return user

    def test_has_basic_user_permissions_to_create_course(self):
        user = User.objects.get(username='user')
        client = APIClient()
        client.force_authenticate(user=user)
        response = client.post('/courses/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_has_staff_permissions_to_create_course(self):
        user = self.get_staff_user()
        client = APIClient()
        client.force_authenticate(user=user)
        response = client.post('/courses/', data={
            'name': 'name',
            'description': 'description',
            'details': 'details',
            'start_date': '2021-07-26',
            'end_date': '2021-08-28'
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_has_author_edit_permission(self):
        user = self.get_staff_user()
        client = APIClient()
        client.force_authenticate(user=user)
        baker.make(Course, author=user)
        response = client.put('/courses/1/', data={
                "name": "name",
                "description": "description",
                "details": "details",
                "start_date": "2021-07-26",
                "end_date": "2021-08-28",
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_has_no_author_edit_permission(self):
        user = User.objects.get(id=1)
        client = APIClient()
        client.force_authenticate(user=user)
        baker.make(Course, author=self.get_staff_user())
        response = client.put('/courses/1/', data={
                "name": "name",
                "description": "description",
                "details": "details",
                "start_date": "2021-07-26",
                "end_date": "2021-08-28",
        })
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


