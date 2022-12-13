import json
from enum import Enum


class Status(Enum):
    Open = 'Open'
    Close = 'Closed'
    In_Progress = 'In Progress'
    Create = 'create'
    Read = 'read'
    Update = 'update'
    Delete = 'delete'
    Exit = 'exit'


class Todolist:
    counter = 0
    instance = {}

    def __init__(self, number: int, task: str, task_date: str, status: str):
        self.number = number
        self.task = task
        self.task_date = task_date
        self.status = status
        Todolist.counter += 1
        self.instance = {'TASK': self.number,
                         'SUBJECT:': self.task,
                         'TASK DATE': self.task_date,
                         'STATUS': self.status
                         }
        Todolist.instance.update(self.instance)

    @classmethod
    def print(cls):
        print(json.dumps(Todolist.instance, indent=2))
        print('\n')

    @classmethod
    def save(cls):
        try:
            with open('file.json', 'r+') as file:
                f_data = json.load(file)
                f_data['Tasks'].append(Todolist.instance)
                file.seek(0)
                json.dump(f_data, file, indent=2)

        except FileNotFoundError as e:
            print(e)
        else:
            print(f'\nData successfully added to File.\n')
            Todolist.print()

    @classmethod
    def update(cls, number, subj, date, status):
        try:
            with open('file.json', 'r+') as file:
                f_data = json.load(file)
                f_data['Tasks'][number - 1].update(
                    {'TASK': number,
                     'SUBJECT:': subj,
                     'TASK DATE': date,
                     'STATUS': status
                     })
                file.seek(0)
                json.dump(f_data, file, indent=2)

        except FileNotFoundError as e:
            print(e)
        else:
            print(f'\nData successfully updated to File.\n')

    @classmethod
    def read(cls):
        try:
            with open('file.json', 'r') as file:
                content = file.read()
        except FileNotFoundError as e:
            print(e)
        else:
            print(f'\nReading data from File.\n\n{content}')

    @classmethod
    def delete(cls, number):
        try:
            with open('file.json', 'r') as file:
                f_data = json.load(file)
                f_data['Tasks'].pop(number - 1)

            new_file = 'file.json'

            with open(new_file, 'w') as f:
                f.write(json.dumps(f_data, indent=2))
        except FileNotFoundError as e:
            print(e)
        else:
            print(f'\nData successfully deleted to File.\n\n{f_data}')
