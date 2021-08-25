import copy

from django.db import models
from lessons.models import Step


class Test(models.Model):
    description = models.CharField(max_length=1024)
    passed = models.BooleanField()
    step = models.OneToOneField(
        Step, on_delete=models.CASCADE, related_name='test')

    @staticmethod
    def is_passed(posted_tasks, posted_cases):
        """
        :returns True If all included task are passed,
        False if there are not passed tasks.
        """
        for task in posted_tasks:
            cases = TaskCase.get_by_task_id(task.id)
            task.passed = Task.is_passed(cases, posted_cases)

        for task in posted_tasks:
            if not task.passed:
                return False
        return True

    def passed_count(self, tasks):
        """
        :return: quantity of passed included in current test tasks.
        """
        count = 0
        for task in tasks:
            if task.passed:
                count += 1
        return count

    def __str__(self):
        return self.description


class Task(models.Model):
    definition = models.CharField(max_length=1024)
    test = models.ForeignKey(
        Test, on_delete=models.CASCADE, related_name='tasks')
    passed = models.BooleanField()

    @staticmethod
    def is_passed(cases, posted_cases):
        comparison = zip(cases, posted_cases)
        for case, posted_case in comparison:
            if case.is_required != posted_case.selected:
                return False
        return True

    def __str__(self):
        return self.definition


class TaskCase(models.Model):
    definition = models.CharField(max_length=1024)
    is_required = models.BooleanField()
    selected = models.BooleanField(default=False)
    task = models.ForeignKey(
        Task, on_delete=models.CASCADE, related_name='cases')

    def __str__(self):
        return self.definition

    @classmethod
    def get_by_task_id(cls, task_id):
        return cls.objects.filter(task_id=task_id)
