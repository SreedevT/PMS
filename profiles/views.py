from django.shortcuts import render, redirect
from django.http import HttpResponse
from accounts.models import User
from .models import *
from .forms import *

def test(request):
    return HttpResponse("THIS TEST")

def profile(request, pk):
    user = User.objects.get(pk=pk)

    if PatientProfile.objects.filter(user=user).exists():
        profile = PatientProfile.objects.get(user=user)
    else:
        profile = PatientProfile.objects.create(user=user)

    if request.method == 'POST':
        form = PatientProfileUpdateForm(request.POST, instance=profile, files=request.FILES) #* files is used to upload files
        if form.is_valid():
            form.save()
            return redirect('accounts:home')
    else:
        form = PatientProfileUpdateForm(instance=profile)
    return render(request, 'profile.html', {'form': form})
