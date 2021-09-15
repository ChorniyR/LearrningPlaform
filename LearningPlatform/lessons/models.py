from django.contrib.auth.models import User
from django.db import models

from courses.models import Course


class Lesson(models.Model):
    number = models.IntegerField()
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title


class Step(models.Model):
    title = models.CharField(max_length=128)
    number = models.IntegerField()
    likes = models.IntegerField()
    dislikes = models.IntegerField()
    lesson = models.ForeignKey(
        Lesson, on_delete=models.CASCADE, related_name='steps')

    @classmethod
    def get_by_lesson_id_and_number(cls, lesson_id, number):
        return cls.objects.filter(lesson=lesson_id).filter(number=number).first()

    def __str__(self):
        return f'id {self.id}: {self.title}'


class StepUser(models.Model):
    passed = models.BooleanField()
    user = models.ManyToManyField(User, related_name='steps')
    step = models.ManyToManyField(Step)
    score = models.FloatField(default=0)
    feedback = models.CharField(max_length=1024, default='no feedback')

    @classmethod
    def create_stepuser(cls, user, step, passed, score):
        """
        Create a new stepuser if not already exists and return it.
        else returns existed.
        """
        if cls.exists(user, step):
            return cls.objects.filter(user=user, step=step).first()

        instance = cls.objects.create(
            feedback=cls._get_feedback(passed),
            passed=passed,
            score=score
        )

        instance.user.add(user)
        instance.step.add(step.id)
        return instance

    @classmethod
    def find_by_step(cls, step):
        return cls.objects.filter(step=step).first()

    @staticmethod
    def _get_feedback(passed):
        if passed:
            return "You are good!! Keep going!"
        return "Not bad! Keep work on it!"

    @classmethod
    def exists(cls, user, step):
        """Returns True if object already exists"""
        return cls.objects.filter(user=user, step=step).exists()

    def __str__(self):
        return f'id {self.step}: {self.user}'
