from django.urls import path
from backend import views


urlpatterns = [
    path('task/', views.Task.as_view()),
]