from django.http import HttpResponse
from backend.models import Files
from django import db
from django.core.files import File
import os


def upload_file(filename):
    try:
        module_dir = os.path.dirname(__file__)
        file_path = os.path.join(module_dir, filename)
        with open(file_path, 'rb') as f:
            data = File(f).read()
        try:
            Files(filename=filename, file=data).save()
            return HttpResponse('Success', status=200)
        except db.IntegrityError as db_e:
            return HttpResponse(db_e, status=409)
    except IOError as e:
        return HttpResponse(e, status=409)


def get_file(filename):
    try:
        files = Files.objects.all().values()
        for file in files:
            if file['filename'] == filename:
                try:
                    module_dir = os.path.dirname(__file__)
                    file_path = os.path.join(module_dir, filename)
                    with open(file_path, 'wb') as f:
                        File(f).write(file['file'])
                    return HttpResponse('Success', status=200)
                except IOError as e:
                    return HttpResponse(e, status=409)
    except db.IntegrityError as db_e:
        return HttpResponse(db_e, status=409)

