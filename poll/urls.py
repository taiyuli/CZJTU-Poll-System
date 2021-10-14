from django.urls import path

from . import views

app_name = 'poll'

urlpatterns = [
    path('index/', views.calResult, name='poll_index'),
]