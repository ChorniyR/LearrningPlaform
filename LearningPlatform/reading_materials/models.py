from lessons.models import Step
from django.db import models

# Create your models here.



class ReadingMaterial(models.Model):
    title = models.CharField(max_length=1024)
    text = models.TextField()
    step = models.OneToOneField(Step, on_delete=models.CASCADE, related_name='reading_material')

    def __str__(self):
        return self.title