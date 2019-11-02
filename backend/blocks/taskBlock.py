from django.core import exceptions
from django.http import HttpResponse
from rest_framework import renderers
from backend.models import Tasks, Workers
from django import db
from datetime import datetime


def createTask(data):
    task = Tasks(taskName=data['taskName'], idWorker_id=data['idWorker'], description=data['description'], deadline=data['deadline'],
                 longitude=data['taskAddress']['coords'][0], latitude=data['taskAddress']['coords'][1],
                 address=data['taskAddress']['address'])
    try:
        task.save()
        return HttpResponse(renderers.JSONRenderer().render({'success': 'Task was created!'}))
    except db.IntegrityError:
        return HttpResponse('Conflict', status=409)


def getTasks(data):
    tasks = Tasks.objects.all()
    for i in tasks:
        if i['deadline'] < datetime.now():
            Tasks.objects.filter(id=i['id']).update(status=True)
    return HttpResponse(renderers.JSONRenderer().render(tasks.values()))


def getWorkersTasks(data):
    tasks = Tasks.objects.filter(idWorker=data['idWorker'])
    for i in tasks:
        if i['deadline'] < datetime.now():
            Tasks.objects.filter(id=i['id']).update(status=True)
    return HttpResponse(renderers.JSONRenderer().render(tasks))




