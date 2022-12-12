from enum import Enum
import json


class Status(Enum):
    Open = 'Open'
    Close = 'Closed'
    In_Progress = 'In Progress'


class Todolist:
    counter = 0
    instances = []

    def __init__(self, number: int, task: str, task_date: str, status: str):
        self.number = number
        self.task = task
        self.task_date = task_date
        self.status = status
        Todolist.counter += 1
        instance = {'TASK': self.number,
                    'SUBJECT:': self.task,
                    'TASK DATE': self.task_date,
                    'STATUS': self.status
                    }

        Todolist.instances.append(instance)

    def change_task_status(self, status_change):
        self.status = status_change

        Todolist.instances[self.number - 1] = \
            {'TASK': self.number,
             'SUBJECT:': self.task,
             'TASK DATE': self.task_date,
             'STATUS': status_change}
        return self.status

    @classmethod
    def print(cls):
        print(json.dumps(Todolist.instances, indent=2))

    @classmethod
    def save(cls):
        json_object = json.dumps(Todolist.instances, indent=2)
        with open('file.json', 'w') as f:
            f.write(json_object)


l1 = Todolist(1, 'Clean your room', '2022-12-19', 'Open')
l2 = Todolist(2, 'Cook dinner for Family', '2022-12-24', 'Open')

Todolist.print()
Todolist.save()
