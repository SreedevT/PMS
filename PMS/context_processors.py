from hospital.models import Department

def get_departments(request):
    departments = Department.objects.all()
    return {'departments': departments}