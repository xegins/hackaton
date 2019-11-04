from django.urls import path
from backend import views


urlpatterns = [
    path('task/', views.Task.as_view()),
    path('worker/', views.Worker.as_view()),
    path('files/', views.File.as_view()),
]