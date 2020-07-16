from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view
import json

from .forms import *
from .models import TodoList, Task
from .serializers import TodoListSerializer, TaskSerializer


@api_view(['GET'])
# Show all lists. Accepts only GET method
def all_todolists(request):
    todolists = TodoList.objects.all()
    serialized_todolists = TodoListSerializer(todolists, many=True)
    # return Response(data=serialized_todolists, status=200)
    return Response(serialized_todolists.data)


@api_view(['GET'])
# Show list of all tasks. Accepts only GET method
def all_tasks(request):
    tasks = Task.objects.all()
    serialized_tasks = TaskSerializer(tasks, many=True)
    # return TodoList.objects.all()
    return Response(serialized_tasks.data)


@api_view(['GET'])
# Detailed_view of one list
def todolist_detail(request, todolist_id):
    todolist = TodoList.objects.get(id=todolist_id)
    serialized_todolist = TodoListSerializer(todolist)
    return Response(serialized_todolist.data)


@api_view(['GET'])
# Detailed_view of one task
def task_detail(request, task_id):
    task = Task.objects.get(id=task_id)
    serialized_task = TaskSerializer(task)
    return Response(serialized_task.data)


@csrf_exempt
# Create a new todolist
def new_todolist(request):
    data = json.load(request)
    if request.method == "POST":
        form = TodoListForm(data)
        if form.is_valid():
            todolist = form.save(commit=True)
            serialized_todolist = TodoListSerializer(todolist).todolist_detail
            return JsonResponse(data=serialized_todolist, status=201)
        else:
            return JsonResponse(
                data={'error': 'TodoList not created'}, status=400)


@csrf_exempt
# Update a todolist
def edit_todolist(request, todolist_id):
    todolist = todolist.objects.get(id=todolist_id)
    if request.method == "PUT":
        data = json.load(request)
        form = todolistForm(data, instance=todolist)
        if form.is_valid():
            todolist = form.save(commit=True)
            serialized_todolist = TodolistSerializer(todolist).todolist_detail
            return JsonResponse(data=serialized_todolist, status=200)
        else:
            return JsonResponse(
                data={'error': 'todolist not updated'}, status=400)


@csrf_exempt
# Delete a todolist
def delete_todolist(request, todolist_id):
    if request.method == "DELETE":
        todolist = todolist.objects.get(id=todolist_id)
        todolist.delete()
        return JsonResponse(data={
            'status': 'Successfully deleted todolist.'}, status=200)
    else:
        return JsonResponse(data={'status': 'Not deleted'}, status=405)

# ////////////////////////////////if


@csrf_exempt
# Create a new task
def new_task(request):
    data = json.load(request)
    if request.method == "POST":
        form = TaskForm(data)
        if form.is_valid():
            task = form.save(commit=True)
            serialized_task = TaskSerializer(task).task_detail
            return JsonResponse(data=serialized_task, status=201)
        else:
            return JsonResponse(
                data={'error': 'task not created'}, status=400)


@csrf_exempt
# Update a task
def edit_task(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == "PUT":
        data = json.load(request)
        form = TaskForm(data, instance=task)
        if form.is_valid():
            task = form.save(commit=True)
            serialized_task = TaskSerializer(task).task_detail
            return JsonResponse(data=serialized_task, status=200)
        else:
            return JsonResponse(
                data={'error': 'Task not updated'}, status=400)


@csrf_exempt
# Delete a task
def delete_task(request, task_id):
    if request.method == "DELETE":
        task = Task.objects.get(id=task_id)
        task.delete()
        return JsonResponse(data={
            'status': 'Successfully deleted task.'}, status=200)
    else:
        return JsonResponse(data={'status': 'Not deleted'}, status=405)
