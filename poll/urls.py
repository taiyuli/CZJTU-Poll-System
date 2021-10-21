from django.urls import path

from . import views

app_name = 'poll'

urlpatterns = [
    path('index/', views.calResult, name='poll_index'),
    path('pollReason/', views.pollReason, name='poll_reason'),
    path('adminPollView/', views.adminResultView, name='admin_poll_view'),

]