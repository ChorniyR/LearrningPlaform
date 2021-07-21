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
