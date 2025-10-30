from django.shortcuts import render
from core.models.task import Task  # adjust import path if your app name is different
from core.serializers.task_serializer import TaskSerializer  # adjust import path if needed
from rest_framework import viewsets, permissions, filters

# Create your views here.

class TaskViewSet(viewsets.ModelViewSet):
    """
    Standard CRUD viewset for Task.
    - Read: list/retrieve
    - Write: create/update/partial_update/destroy
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # Basic filtering/search/ordering
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["title", "description"]
    ordering_fields = ["created_at", "updated_at", "priority"]
    ordering = ["-created_at"]

    # If you want field-based filtering with django-filter:
    # filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    # filterset_fields = ["status", "owner"]
