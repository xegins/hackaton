from django import views
from rest_framework import parsers
from backend.blocks import workerBlock, taskBlock


class Task(views.View):
    def post(self, request):
        data = parsers.JSONParser().parse(request)
        return taskBlock.createTask(data)

    def get(self, request):
        data = request.GET
        return taskBlock.getTasks(data)


class Worker(views.View):
    def get(self, request):
        print(request.GET)
        return workerBlock.getWorkers(request.GET)
