from django.urls import path

from . import api_views

urlpatterns = [
    path('list/', api_views.TodoList.as_view(), name='todo_list'),
    path('detail/<int:pk>', api_views.TodoDetail.as_view(), name='todo_detail'),
]