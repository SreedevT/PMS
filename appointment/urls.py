from django.urls import path, include
from . import views

app_name = 'appointment'
urlpatterns = [
    path('select-doctor', views.doctor_list, name='doc-list'),
    # path('test', views.test, name='test'), #?TODO - remove this
    path('appointment-form', views.appointment_form, name='appointment-form'),
    path('appointment-book', views.appointment_book, name='appointment-book'),
    path('doctor/pending-appointments', views.pending_appointments, name='pending-appointment'),
    path('doctor/view-appointment', views.view_appointment, name='view-appointment')
]