from django.shortcuts import render
from hospital.models import Department
from accounts.models import User

def doctor_list(request):
    depts = Department.objects.all()
    doctors = User.objects.filter(user_type='D')
    context = {'depts': depts, 'doctors': doctors}
    return render(request, 'doc.html', context=context)