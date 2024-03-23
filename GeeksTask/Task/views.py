from django.shortcuts import render
from rest_framework import generics
from .models import Task
from.serializers import TaskSerializer


class TaskList(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskCreate(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDetail(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    lookup_field = 'id'
    serializer_class = TaskSerializer


class TaskUpdate(generics.RetrieveUpdateAPIView):
    queryset = Task.objects.all()
    lookup_field = 'id'
    serializer_class = TaskSerializer


class TaskDelete(generics.RetrieveDestroyAPIView):
    queryset = Task.objects.all()
    lookup_field = 'id'
    serializer_class = TaskSerializer
