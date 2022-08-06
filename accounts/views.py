from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from .forms import UserCreateForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from profiles.models import PatientProfile


class LoginFormView(SuccessMessageMixin, LoginView):
    success_message: str = 'You have been logged in successfully.'

class LogoutFormView(LogoutView): #* No idea how it works, but: https://stackoverflow.com/questions/59593854/display-messages-on-logoutview

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        messages.add_message(request, messages.SUCCESS, 'Successfully logged out.')
        return response

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
    # Restricted home page for admins, prompts to logout
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

    return render(request, 'sign-up.html', {'form': form})
