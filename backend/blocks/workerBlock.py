from backend.models import Workers
from django.http import HttpResponse
from rest_framework import renderers


def getWorkers(data):
    if (data['id'] == '*'):
        worker = Workers.objects.all().values()
    else:
        worker = Workers.objects.filter(id=data['id'])
    return HttpResponse(renderers.JSONRenderer().render(worker.values()))

