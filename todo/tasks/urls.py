from django.urls import path
from . import views
urlpatterns = [
    path('helloword/', views.helloword),
]