from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from hospital.models import Department
from accounts.models import User
from .models import Appointment
from hospital.models import Medicine
from django.contrib import messages
from .forms import PrescriptionForm

def doctor_list(request):
    context = {}
    depts = Department.objects.all()
    doctors = User.objects.filter(user_type='D')
    # doctors = User.objects.raw('''
    #             SELECT id 
    #             FROM accounts_user
    #             WHERE user_type="D"
    # ''')
    context = {'depts': depts, 'doctors': doctors}
    print(list(depts))
    return render(request, 'doc.html', context=context)


# def test(request):
#     context = {}
#     id = request.POST['id']
#     doctor = User.objects.get(id=id)
#     return render(request, 'book-appointment.html')

@login_required(login_url='accounts:login')
def appointment_form(request):
    context = {}

    if request.method == 'POST':
        id = request.POST['id']
        doctor = User.objects.get(id=id)
        context = {'doctor': doctor}
        return render(request, 'appointment-form.html', context=context)

def appointment_book(request):
    #* Django model instances: https://docs.djangoproject.com/en/4.0/ref/models/instances/#django.db.models.Model.save
    context = {}
    if request.method != 'POST':
        #! Display slect doctor message on 'doc.html'
        return redirect('appointment:doc-list')
    if request.method == 'POST':
        strslot = request.POST['slot']
        # print(strslot)
        list_slot = strslot.split('-')
        # print(list_slot)
        
        doctor_id = request.POST['doctor']

        appointment = Appointment.objects.create(
            doctor = User.objects.get(pk=doctor_id),
            patient = request.user,
            date = request.POST['date'],
            reason = request.POST['reason'],
            start_time=list_slot[0],
            end_time=list_slot[1],
            status=False,
        )
        context={'appointment':appointment}
        messages.success(request, 'Appointment booked successfully!')
    # return render(request, 'book-appointment-test.html', context=context)
    return render(request, 'home.html', context=context)

def pending_appointments(request):
    context = {}
    user = request.user
    if not user.is_doctor():
        return HttpResponse("NOT ALLOWED")
        #! Display 403 Forbidden page

    appointments = Appointment.objects.filter(doctor=user, status=False)
    print(list(appointments))
    # print(list(appointments)[0].patient)
    context = {'appointments':appointments}

    return render(request, 'pending-appointment.html', context=context)

def view_appointment(request):
    context={}
    if request.method != 'POST':
        return redirect('appointment:pending-appointment')

    app_id = request.POST['id']
    appointment = Appointment.objects.get(pk=app_id)
    form = PrescriptionForm()
    print(form)
    context = {'appointment':appointment, 'form':form}
    return render(request, 'view-appointment.html', context=context)