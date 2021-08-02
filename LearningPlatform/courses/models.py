from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    details = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    creating_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class CourseUser(models.Model):
    course = models.ManyToManyField(Course, related_name='courses')
    user = models.ManyToManyField(User, related_name='users')
    passed = models.BooleanField(default=False)

    def get_courses_by_user(self, user):
        return self.objects.filter(user=user)

    def enroll_on_course(self, user, course):
        object_ = self.objects.create(user=user, course=course)
        return object_

    def __str__(self):
        return f"{self.user.username}'s subscribed on: {self.course.name}"
