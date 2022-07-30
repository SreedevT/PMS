from django.shortcuts import render, HttpResponse
from hospital.models import Department
from accounts.models import User

def doctor_list(request):
    context = {}
    depts = Department.objects.all()
    doctors = User.objects.filter(user_type='D')
    context = {'depts': depts, 'doctors': doctors}
    return render(request, 'doc.html', context=context)


def test(request):
    id = request.POST['id']
    doctor = User.objects.get(id=id)
    return HttpResponse(f'Test {doctor.get_full_name()}')