from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('api/v1/task_list', TaskList.as_view()),
    path('api/v1/create_task', TaskCreate.as_view()),
    path('api/v1/detail_task/<int:id>',  TaskDetail.as_view()),
    path('api/v1/update_task/<int:id>', TaskUpdate.as_view()),
    path('api/v1/delete_task/<int:id>', TaskDelete.as_view()),
]