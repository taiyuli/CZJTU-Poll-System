from django.urls import path

from . import views

app_name = 'independentPoll'

urlpatterns = [
    path('leaderPoll/', views.leaderPollIdpd, name='leader_poll'),
    path('leaderPollCount/', views.leaderPollIdpdCount, name='leader_poll_count'),
    path('departmentPoll/', views.departmentPollIdpd, name='department_poll'),
    path('departmentPollCount/', views.departmentPollIdpdCount, name='department_poll_count'),
]