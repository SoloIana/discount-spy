import json

from django.shortcuts import render
from django.http import JsonResponse

from .models import Task


# Create your views here.
def add_task(request):
    if request.is_ajax():
        if request.method == 'POST':
            data = json.loads(request.body)

    new_task = Task()
    return JsonResponse({"message": "Task added!", "status": "ok"})