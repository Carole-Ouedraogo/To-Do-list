from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view
import json

from .forms import TodoListForm, TaskForm
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
def all_tasks(request, todolist_id):
    todolist = TodoList.objects.get(id=todolist_id)
    tasks = todolist.tasks.all()
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
def task_detail(request, todolist_id, task_id):
    todolist = TodoList.objects.get(id=todolist_id)
    task = Task.objects.get(id=task_id)
    serialized_task = TaskSerializer(task)
    return Response(serialized_task.data)


@csrf_exempt
# Create a new todolist
def new_todolist(request):
    data = json.loads(request.body)
    if request.method == "POST":
        form = TodoListForm(data)
        if form.is_valid():
            todolist = form.save(commit=False)
            serialized_todolist = TodoListSerializer(todolist)
            return JsonResponse(data=serialized_todolist.data, status=201)
        else:
            return JsonResponse(
                data={'error': 'TodoList not created', 'formError': form.errors}, status=400)


@csrf_exempt
# Create a new task
def new_task(request, todolist_id):
    todolist = TodoList.objects.get(id=todolist_id)
    data = json.loads(request.body)
    print(data)
    if request.method == "POST":
        form = TaskForm(data)
        if form.is_valid():

            # commit=False ie don't save it to db until it is attached to the parent list
            task = form.save(commit=False)
# model form (TaskForm) field is refering to the todolist referred to (line 66)
# task model object
            task.todo_list = todolist
            task.save()
            serialized_task = TaskSerializer(task)
            return JsonResponse(data=serialized_task.data, status=201)
        else:
            # print(form.errors)
            return JsonResponse(
                data={'error': 'task not created', 'form': dict(form.errors)}, status=400)


@csrf_exempt
# Update a todolist
def edit_todolist(request, todolist_id):
    todolist = TodoList.objects.get(id=todolist_id)
    if request.method == "PUT":
        data = json.load(request)
        form = TodoListForm(data, instance=todolist)
        if form.is_valid():
            todolist = form.save(commit=True)
            serialized_todolist = TodoListSerializer(todolist)
            # print(serialized_todolist.data)
            return JsonResponse(data=serialized_todolist.data, status=200)
        else:
            return JsonResponse(
                data={'error': 'todolist not updated'}, status=400)


@csrf_exempt
# Update a task
def edit_task(request, todolist_id, task_id):
    todolist = TodoList.objects.get(id=todolist_id)
    if request.method == "PUT":
        task = Task.objects.get(id=task_id)
        data = json.load(request)
        form = TaskForm(data, instance=task)
        if form.is_valid():
            task = form.save(commit=True)
            serialized_task = TaskSerializer(task)
            # print(serialized_task.data)
            return JsonResponse(data=serialized_task.data, status=200)
        else:
            return JsonResponse(
                data={'error': 'task not updated'}, status=400)


@csrf_exempt
# Delete a todolist
def delete_todolist(request, todolist_id):
    if request.method == "DELETE":
        todolist = TodoList.objects.get(id=todolist_id)
        todolist.delete()
        return JsonResponse(data={
            'status': 'Successfully deleted todolist.'}, status=200)
    else:
        return JsonResponse(data={'status': 'Not deleted'}, status=405)


@csrf_exempt
# Delete a task
def delete_task(request, todolist_id, task_id):
    todolist = TodoList.objects.get(id=todolist_id)
    if request.method == "DELETE":
        task = Task.objects.get(id=task_id)
        task.delete()
        return JsonResponse(data={
            'status': 'Successfully deleted task.'}, status=200)
    else:
        return JsonResponse(data={'status': 'Not deleted'}, status=405)
