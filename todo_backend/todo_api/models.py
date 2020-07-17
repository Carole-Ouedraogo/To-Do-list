from django.conf import settings
from django.db import models


class TodoList(models.Model):
    todolist_name = models.CharField(max_length=255)
    todolist_category = models.CharField(max_length=255)

    def __str__(self):
        return f"List: {self.todolist_name} Category: {self.todolist_category}"


class Task(models.Model):
    todo_list = models.ForeignKey(
        TodoList, on_delete=models.CASCADE, related_name='tasks')
    task_name = models.CharField(max_length=255)
    task_description = models.TextField(null=True)
    due_date = models.DateField(blank=True, null=True)
    task_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Task: {self.task_name}"
