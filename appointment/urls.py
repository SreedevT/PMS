from django.urls import path, include
from . import views

app_name = 'appointment'
urlpatterns = [
    path('appointment', views.doctor_list, name='doc-list'),
    path('test/', views.test, name='test'), #?TODO - remove this
    path('book-appointment', views.book_appointment, name='book-appointment'),
    path('booked-test', views.appointment_test, name='booked-test'),
    path('doctor/pending-appointments', views.pending_appointments, name='pending-appointment'),
    path('doctor/view-appointment', views.view_appointment, name='view-appointment')
]