from django.urls import path
from . import views

urlpatterns = [
    path('helloword/', views.helloword),
    path('', views.tasklist, name='task-list'),
    path('task/<int:id>', views.taskView, name='task-view'),
    path('yourname/<str:name>', views.yourName, name='your-name')
]