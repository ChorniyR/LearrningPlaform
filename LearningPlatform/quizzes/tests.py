import unittest
from model_bakery import baker
from django.test import TestCase

from .models import Task, Test, TaskCase


class TestModelTest(TestCase):
    def test_is_passed_Test_with_passed_tasks(self):
        test = baker.make(Test)
        passed_task = baker.make(Task, passed=True, test=test)
        self.assertIs(test.is_passed([passed_task]), True)

    def test_is_passed_Test_with_not_passed_tasks(self):
        test = baker.make(Test)
        passed_task = baker.make(Task, passed=True, test=test)
        not_passed_task = baker.make(Task, passed=False, test=test)
        self.assertIs(test.is_passed([passed_task, not_passed_task]), False)

    def test_count_of_included_tasks_in_test(self):
        test = baker.make(Test)
        passed_task = baker.make(Task, passed=True, test=test)
        not_passed_task = baker.make(Task, passed=False, test=test)
        self.assertEqual(len(test), 2)

    def test_count_of_passed_tasks_in_test(self):
        test = baker.make(Test)
        passed_task = baker.make(Task, passed=True, test=test)
        not_passed_task = baker.make(Task, passed=False, test=test)
        self.assertEqual(test.passed_count([passed_task, not_passed_task]), 1)


class TestModelTask(TestCase):
    def test_is_passed_with_all_selected(self):
        task = baker.make(Task)
        task_case = baker.make(TaskCase, task=task, selected=True, is_required=False)
        task_case2 = baker.make(TaskCase, task=task, selected=True, is_required=True)
        self.assertIs(task.is_passed([task_case, task_case2]), False)

    def test_is_passed_with_correct_answers(self):
        task = baker.make(Task)
        task_case = baker.make(TaskCase, task=task, selected=False, is_required=False)
        task_case2 = baker.make(TaskCase, task=task, selected=True, is_required=True)
        self.assertIs(task.is_passed([task_case, task_case2]), True)
