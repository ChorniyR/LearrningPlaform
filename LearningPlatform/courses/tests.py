import json
from itertools import islice

from django.contrib.auth.models import User
from django.test import TestCase
from model_bakery import baker
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from .models import Course, CourseUser
from .serializers import CoursesSerializer, CourseUserSerializer


class PermissionsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('user', 'user@mail.com', 'user')
        self.staff_user = User.objects.create_user('staff', 'staff@staff.com', 'staff', is_staff=True)

    def test_has_basic_user_permissions_to_create_course(self):
        """
        Ensure that basic user can't create new course.
        """
        client = APIClient()
        client.force_authenticate(user=self.user)
        response = client.post('/courses/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_has_staff_permissions_to_create_course(self):
        """
        Ensure that staff can create new course.
        """
        client = APIClient()
        client.force_authenticate(user=self.staff_user)
        response = client.post('/courses/', data={
            'name': 'name',
            'description': 'description',
            'details': 'details',
            'start_date': '2021-07-26',
            'end_date': '2021-08-28'
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_has_author_edit_permission(self):
        """
        Ensure that only author has permissions to edit course.
        """
        client = APIClient()
        client.force_authenticate(user=self.staff_user)
        baker.make(Course, author=self.staff_user)
        response = client.put('/courses/1/', data={
            "name": "name",
            "description": "description",
            "details": "details",
            "start_date": "2021-07-26",
            "end_date": "2021-08-28",
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_has_no_author_edit_permission(self):
        """
        Ensure that no author can't edit course
        """
        client = APIClient()
        client.force_authenticate(user=self.user)
        baker.make(Course, author=self.staff_user)
        response = client.put('/courses/1/', data={
            "name": "name",
            "description": "description",
            "details": "details",
            "start_date": "2021-07-26",
            "end_date": "2021-08-28",
        })
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class TestCoursesViewSet(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user('user', 'user@mail.com', 'user')
        self.client = APIClient()
        self.client.force_authenticate(self.user)
        Course.objects.create(
            name="first_course", description="description", details="details",
            start_date="2021-07-26", end_date="2021-08-28")
        Course.objects.create(
            name="second_course", description="description", details="details",
            start_date="2021-07-26", end_date="2021-08-28")

    def test_details_view(self):
        """
        Test to verify course list bundle
        """
        course = Course.objects.get(name='first_course')
        response = self.client.get('/courses/1/')
        serializer = CoursesSerializer(course)
        self.assertEqual(json.loads(response.content), serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_view(self):
        """
        Test to verify course object bundle
        """
        courses = Course.objects.all()
        response = self.client.get('/courses/')
        serializer = CoursesSerializer(courses, many=True)
        self.assertEqual(response.data['results'], serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_courses_bundle_authorization(self):
        """
        Test to verify auth in courses bundle
        """
        self.client.logout()
        response = self.client.get('/courses/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
