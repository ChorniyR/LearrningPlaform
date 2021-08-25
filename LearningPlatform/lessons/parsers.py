import copy

from quizzes.models import Task, TaskCase, Test


def parse_cases(data):
    cases = []
    for task in data['test']['tasks']:
        for kwargs in task.get('cases'):
            del kwargs['task']
            cases.append(TaskCase(**kwargs))
    return cases


def parse_tasks(data):
    test = copy.deepcopy(data['test'])
    tasks = []
    for kwargs in test.get('tasks'):
        del kwargs['cases']
        tasks.append(Task(**kwargs))
    return tasks


def parse_test(data):
    kwargs = copy.deepcopy(data['test'])
    del kwargs['tasks']
    del kwargs['step']
    return Test(**kwargs)
