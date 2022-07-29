from django.urls import path, include
from . import views

app_name = 'appointment'
urlpatterns = [
    path('appointment', views.doctor_list, name='doc-list'),
]