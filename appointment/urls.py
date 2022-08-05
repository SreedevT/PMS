from django.urls import path, include
from . import views

app_name = 'appointment'
urlpatterns = [
    path('appointment', views.doctor_list, name='doc-list'),
    path('test/', views.test, name='test'), #?TODO - remove this
    path('book-appointment-test', views.book_appointment_test, name='book-appointment-test'),
    path('booked-test', views.appointment_test, name='booked-test'),
    path('pending-appointments', views.pending_appointments, name='pending-appointment'),
    path('view-details', views.view_details, name='view-details')
]