from . import views
from django.urls import path, include
from .views import all_todolists, all_tasks

# wines/urls.py

urlpatterns = [
    # list all todolists
    path('', views.all_todolists, name='all_todolists'),
    # form page for creating a new todolist
    path('new', views.new_todolist, name='new_todolist'),
    # view details about a existing todolist
    path('<int:todolist_id>', views.todolist_detail,
         name='todolist_detail'),
    # form page for editing a todolist
    path('<int:todolist_id>/edit',
         views.edit_todolist, name='edit_todolist'),
    # delete a todolist
    path('<int:todolist_id>/delete',
         views.delete_todolist, name='delete_todolist'),

    #     /////////////////////////////////////////////

    path('<int:todolist_id>/tasks', views.all_tasks,
         name='all_tasks'),  # list all tasks in a todolist
    path('<int:todolist_id>/tasks/new', views.new_task,
         name='new_task'),  # form page for creating a new task for a todolist
    path('<int:todolist_id>/tasks/<int:task_id>',
         views.task_detail, name='task_detail'),  # view details about a task
    path('<int:todolist_id>/tasks/<int:task_id>/edit',
         views.edit_task, name='edit_task'),  # form page for editing
    path('<int:todolist_id>/tasks/<int:task_id>/delete',
         views.delete_task, name='delete_task'),  # delete a task from todolist

]
