from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from .forms import UserCreateForm
from .models import User

def home(request):
    return render(request, 'home.html', context={'user': request.user})

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