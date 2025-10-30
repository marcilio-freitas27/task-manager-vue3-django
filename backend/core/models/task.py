from rest_framework import viewsets, permissions, filters, serializers
from rest_framework.routers import DefaultRouter
from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    priority = models.IntegerField(default=0)
    status = models.CharField(max_length=50)
    owner = models.ForeignKey('auth.User', related_name='tasks', on_delete=models.CASCADE)

# If you use django-filter, uncomment the next line and add 'django_filters' to DRF settings.
# from django_filters.rest_framework import DjangoFilterBackend

# Router snippet for urls.py (copy into your app's urls)
