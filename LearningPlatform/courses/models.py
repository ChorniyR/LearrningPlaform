from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    details = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    creating_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class CourseUser(models.Model):
    course = models.ManyToManyField(Course, related_name='courses')
    user = models.ManyToManyField(User, related_name='users')
    passed = models.BooleanField(default=False)

    @classmethod
    def get_courses_by_user(cls, user):
        return cls.objects.filter(user=user)

    @classmethod
    def add_course_to_user(cls, user, course):
        """
        If user had already enrolled on any course, method will just add the course in CourseUser table,
        but if user have never been enrolled on any courses, 
        it will create new instance in CourseUser table.
        return: CourseUser instance
        """
        try:
            course_user = cls.objects.get(user=user)
        except cls.DoesNotExist:
            course_user = cls.objects.create()
            course_user.user.add(user)
            course_user.course.add(course)
        else:
            course_user.course.add(course)
        return course_user

    def enroll_on_course(self, user, course):
        object_ = self.objects.create(user=user, course=course)
        return object_

    def __str__(self):
        return f"{self.user.username}'s subscribed on: {self.course.name}"
