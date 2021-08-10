import json

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Task


# Create your views here.
@csrf_exempt
def add_task(request):
    data = None
    # if request.is_ajax():
    if request.method == 'POST':
        data = json.loads(request.body)
        new_task = Task(
            name=data['name'],
            target_price=data['target_price'],
            email=data['email'],
            url=data['url']
        )
        new_task.save()
    if data is None:
        return JsonResponse({"error": "We don't have data!"})
    return JsonResponse({"message": "Task added!", "status": "ok"})