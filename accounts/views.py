from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from .forms import UserCreateForm
from profiles.models import PatientProfile

def home(request):
    #* user context is passed by default to all templates, need not specify
    #! Not needed
    # context = {'user': request.user} #? context may not be needed for authenticated users, see: 
    #? https://stackoverflow.com/questions/13713077/get-user-information-in-django-templates

    #* since profile is a child of user (one to one relationship)
    #* we can access the profile object by using the user object
    #! Not needed 
    # profile = PatientProfile.objects.get(user=request.user)
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('success')
    else:
        form = UserCreateForm()
    return render(request, 'register.html', {'form': form})

def success(request):
    return HttpResponse('Success!')