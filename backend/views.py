from django import views
from rest_framework import parsers, renderers
from backend.blocks import workerBlock, taskBlock, filesBlock


class Task(views.View):
    def post(self, request):
        data = parsers.JSONParser().parse(request)
        print(data)
        return taskBlock.createTask(data)

    def get(self, request):
        print(request.GET)
        return taskBlock.getTasks(request.GET)


class Worker(views.View):
    def get(self, request):
        print(request.GET)
        return workerBlock.getWorkers(request.GET)


class File(views.View):
    def post(self, request):
        # todo получение имени файла
        filename = "requirements.txt"
        return filesBlock.upload_file(filename)

    def get(self, request):
        # todo убрать этот костыль для проверки записи файла в бд
        filename = "requirements.txt"
        return filesBlock.upload_file(filename)

        # return filesBlock.get_file(request.GET)
