from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from courses.models import Course


class Lesson(models.Model):
    number = models.IntegerField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title


class Step(models.Model):
    title = models.CharField(max_length=128)
    number = models.IntegerField()
    likes = models.IntegerField()
    dislikes = models.IntegerField()
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='steps')

    def __str__(self):
        return self.title


class StepUser(models.Model):
    passed = models.BooleanField()
    score = models.IntegerField()
    user = models.ManyToManyField(User, related_name='steps')
    step = models.ManyToManyField(Step)
    feedback = models.CharField(max_length=1024, default='no feedback')

