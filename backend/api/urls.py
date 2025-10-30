from django.urls import path
from api.views.task_view import TaskListView

urlpatterns = [
    path('tasks/', TaskListView, name='task-list'),
]
