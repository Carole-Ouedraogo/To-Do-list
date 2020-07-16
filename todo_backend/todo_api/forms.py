from django import forms
from .models import Task, TodoList


class TodoListForm(forms.ModelForm):
    class Meta:
        model = TodoList
        fields = ('todolist_name', 'todolist_category')


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('task_name', 'task_description',
                  'due_date', 'task_completed')
