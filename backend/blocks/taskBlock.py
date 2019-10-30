from django.http import HttpResponse
from rest_framework import renderers
from backend.models import Tasks, Workers
from django import db
from datetime import datetime


def createTask(data):
    task = Tasks(name=data['name'], id_worker=data['id_worker'], description=data['description'], deadline=data['deadline'],
                 longitude=data['longitude'], latitude=data['latitude'])
    try:
        task.save()
        return HttpResponse(renderers.JSONRenderer().render({'success': 'Task was created!'}))
    except db.IntegrityError:
        return HttpResponse('Conflict', status=409)


def getTask(data):
    task = Tasks.objects.filter(id=data['id'])
    for i in task:
        if i['deadline'] < datetime.now():
            task.filter(id=i['id']).update(status=True)



