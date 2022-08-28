from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from hospital.models import Department
from accounts.models import User
from .models import Appointment, Prescription, Report
from .forms import ReportForm
from hospital.models import Medicine
from django.db import connection
from django.contrib import messages

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
    messages.info(request, 'Please select a doctor!')
    return render(request, 'doc.html', context=context)


def test(request):
    context = {}
    options = request.POST.getlist('test')
    print(options)
    return render(request, 'test.html', context=context)

@login_required(login_url='accounts:login')
def appointment_form(request):
    context = {}

    if request.method != 'POST':
        #? Display select doctor message on 'doc.html'
        messages.add_message(request, messages.ERROR, 'Select a doctor first!')
        return redirect('appointment:doc-list')

    #if POST request
    id = request.POST['id']
    doctor = User.objects.get(id=id)
    context = {'doctor': doctor}
    return render(request, 'appointment-form.html', context=context)

def appointment_book(request, *args):
    #* Django model instances: https://docs.djangoproject.com/en/4.0/ref/models/instances/#django.db.models.Model.save
    context = {}
    if request.method != 'POST':
        messages.add_message(request, messages.ERROR, 'Select a doctor first!')
        return redirect('appointment:doc-list')

    # if POST request
    strslot = request.POST['slot']
    list_slot = strslot.split('-') #!['9:00', '10:00']
    
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
    return render(request, 'home.html', context=context)

def pending_appointments(request, status):
    context = {}
    user = request.user
    if not user.is_doctor():
        return HttpResponse("NOT ALLOWED")
        #! Display 403 Forbidden page

    appointments = Appointment.objects.filter(doctor=user, status=status)
    # print(connection.queries)
    context = {'appointments':appointments, 'status':status} #* Status passed in to change heading of page (Completed/Pending)

    return render(request, 'pending-appointment.html', context=context)

def view_appointment(request):
    context={}
    if request.method != 'POST':
        return redirect('appointment:pending-appointment')

    app_id = request.POST['id']
    appointment = Appointment.objects.get(pk=app_id)
    medicines = Medicine.objects.all()
    form = ReportForm()
    context = {'appointment':appointment, 'medicines':medicines, 'form':form}
    return render(request, 'view-appointment.html', context=context)


def result(request):
    if request.method == 'POST':
        report(request)
        prescription(request)

        # Set appointment status to true and *save* it
        # TODO on delete of presciption, set appointment status to false
        #* More info: https://docs.djangoproject.com/en/dev/topics/db/sql/#executing-custom-sql-directly
        cursor = connection.cursor()
        cursor.execute(''' UPDATE appointment 
                          SET status=1
                          WHERE id=%s ''', [request.POST['app_id']]
                        )
        cursor.close()
        
        messages.add_message(request, messages.SUCCESS, 'Report & Prescription added successfully!')
        return redirect('appointment:pending-appointment')



def report(request):
    report = Report.objects.create(appointment_id = request.POST['app_id'])
    form = ReportForm(request.POST, instance=report, files=request.FILES)
    if form.is_valid():
        form.save()


def prescription(request):
    context = {}

    if request.method == 'POST':
        app_id = request.POST['app_id']
        appointment = Appointment.objects.get(pk=app_id)
        medicines = request.POST.getlist('medicine')#* ['1', '2']
        instruction = request.POST['instruction']

        prescription = Prescription(
            appointment=appointment,
            instructions=instruction,       
        )
        prescription.save()
        prescription.medicine.add(*medicines) #* More info: https://stackoverflow.com/questions/6996176/how-to-create-an-object-for-a-django-model-with-a-many-to-many-field
       
        # print(connection.queries)

        follow = request.POST.get('follow', False)
        if follow:
            follow_book(request)


def follow_book(request):
    prev_appointment = Appointment.objects.get(id=request.POST['app_id'])
    doctor = prev_appointment.doctor
    patient = prev_appointment.patient
    reason = prev_appointment.reason
    #! IF timeslots are implemented for each doctor, use doctor_id to get timeslots
    start_time = "9:00"
    end_time = "10:00"
    Appointment.objects.create(
        doctor = doctor,
        patient = patient,
        date = request.POST['date'],
        reason = reason,
        start_time = start_time,
        end_time = end_time,
        status = False,
    )
    messages.success(request, 'Appointment booked successfully!')
    return redirect('appointment:view-appointment')

def past_history(request):
    context = {}
    patient_id = request.POST['pat_id']
    patient = User.objects.get(pk=patient_id)
    appointments = Appointment.objects.filter(patient=patient,status = True)
    context = {'appointments':appointments, 'patient':patient}
    return render(request, 'view-past-history.html', context=context)


def past_prescription(request):
    context = {}
    appointment_id = request.POST['app_id']
    appointment = Appointment.objects.get(pk=appointment_id)
    context = {'appointment':appointment}
    
    return render(request,'past-prescription.html',context=context)
