from django.db import models

from courses.models import Course


class Test(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='tests')
    description = models.CharField(max_length=1024)
    passed = models.BooleanField()

    @property
    def is_passed(self):
        """
        :returns True If all included task are passed,
        also False if one task is not passed and if tasks queryset is empty.
        """
        if self.tasks.all():
            for task in self.tasks.all():
                if not task.passed:
                    return False
            return True
        return False

    @property
    def passed_count(self):
        """
        :return: quantity of passed included tasks.
        """
        count = 0
        for task in self.tasks.all():
            if task.passed:
                count += 1
        return count

    def __len__(self):
        """
        :return: quantity of included tasks.
        """
        return len(self.tasks.all())

    def __str__(self):
        return self.description


class Task(models.Model):
    definition = models.CharField(max_length=1024)
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='tasks')
    passed = models.BooleanField()

    @property
    def is_passed(self):
        for case in self.cases.all():
            if case.is_required != case.selected:
                return False
        return True

    def __str__(self):
        return self.definition


class TaskCase(models.Model):
    definition = models.CharField(max_length=1024)
    is_required = models.BooleanField()
    selected = models.BooleanField()
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='cases')

    def __str__(self):
        return self.definition
