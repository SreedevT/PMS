from django.urls import path, include
from . import views

app_name = 'appointment'
urlpatterns = [
    path('select-doctor', views.doctor_list, name='doc-list'),
    path('test', views.test, name='test'), #?TODO - remove this
    path('appointment-form', views.appointment_form, name='appointment-form'),
    path('appointment-book', views.appointment_book, name='appointment-book'),
    path('doctor/pending-appointments', views.pending_appointments, {'status': False}, name='pending-appointment'), #* Pass extra option to function as dictionary
    path('doctor/completed-appointments', views.pending_appointments, {'status': True}, name='completed-appointment'),#* More info : https://django-book.readthedocs.io/en/latest/chapter08.html#passing-extra-options-to-view-functions
    path('doctor/view-appointment', views.view_appointment, name='view-appointment'),
    path('doctor/prescription', views.prescription, name='prescription'),
]