from django.shortcuts import render, HttpResponse
from hospital.models import Department
from accounts.models import User
from .models import Appointment

def doctor_list(request):
    context = {}
    depts = Department.objects.all()
    doctors = User.objects.filter(user_type='D')
    context = {'depts': depts, 'doctors': doctors}
    print(list(depts))
    return render(request, 'doc.html', context=context)


def test(request):
    context = {}
    id = request.POST['id']
    doctor = User.objects.get(id=id)
    return render(request, 'book-appointment.html')

def book_appointment_test(request):
    context = {}

    if request.method == 'POST':
        id = request.POST['id']
        doctor = User.objects.get(id=id)
        context = {'doctor': doctor}
        return render(request, 'book-appointment-test.html', context=context)

def appointment_test(request):
    #* Django model instances: https://docs.djangoproject.com/en/4.0/ref/models/instances/#django.db.models.Model.save
    context = {}
    if request.method == 'POST':
        slot = request.POST['slot']
        print(slot)
        # appointment = Appointment.objects.create(
        #     doctor = request.POST['doctor']
        #     patient = request.POST['user']
        #     date = request.POST['date']
        #     reason = request.POST['reason']
        # )
    return render(request, 'book-appointment-test.html', context=context)