from . import views
from django.urls import path, include
from .views import all_todolists, all_tasks

# wines/urls.py

urlpatterns = [
    path('', views.all_todolists, name='all_todolists'),
    path('lists/new/', views.new_todolist, name='new_todolist'),
    path('lists/<int:todolist_id>', views.todolist_detail, name='todolist_detail'),
    path('lists/<int:todolist_id>/edit',
         views.edit_todolist, name='edit_todolist'),
    path('lists/<int:todolist_id>/delete',
         views.delete_todolist, name='delete_todolist'),

    path('tasks/', views.all_tasks, name='all_tasks'),
    path('tasks/new/', views.new_task, name='new_task'),
    path('tasks/<int:task_id>', views.task_detail, name='task_detail'),
    path('tasks/<int:task_id>/edit', views.edit_task, name='edit_task'),
    path('tasks/<int:task_id>/delete', views.delete_task, name='delete_task'),

]
