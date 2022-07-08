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
    user = request.user
    if user.is_superuser:
        return render(request, 'home_no_entry.html')
        
    return render(request, 'home.html')

def register(request):
    if request.method != 'POST':
        form = UserCreateForm()
    
    form = UserCreateForm(request.POST)
    if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('accounts:home')

    return render(request, 'register.html', {'form': form})
