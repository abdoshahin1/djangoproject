from django.urls import path, include
from . import views
app_name = 'job'
urlpatterns = [
    path('', views.jobs),
    path('<str:slug>', views.job_details, name ='jobDetails'),
]
