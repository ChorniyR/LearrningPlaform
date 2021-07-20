from django.db import models

# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    details = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    creating_date = models.DateTimeField(auto_now_add=True)
    teacher = models.ForeignKey('Teacher', on_delete=models.SET_NULL, null=True)
    
