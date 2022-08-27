from django.shortcuts import render, redirect
from django.db import connection
from django.http import HttpResponse
from django.contrib.auth import login
from .forms import UserCreateForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages


class LoginFormView(SuccessMessageMixin, LoginView):
    success_message: str = 'You have been logged in successfully.'

class LogoutFormView(LogoutView): #* No idea how it works, but: https://stackoverflow.com/questions/59593854/display-messages-on-logoutview

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        messages.add_message(request, messages.SUCCESS, 'Logged out Successfully!')
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

    if user.is_doctor:
        cursor = connection.cursor()
        cursor.execute('''
                            SELECT appointment.status,  COUNT(*)
                            FROM appointment
                            WHERE appointment.doctor_id = %s
                            GROUP BY appointment.status''', [user.id])
        row = cursor.fetchall() #* fetchall() returns a list of tuples [(False, 4), (True, 2)]
        pending_count = row[False][1]
        completed_count = row[True][1]
        context = {'pending_count': pending_count, 'completed_count': completed_count}
        return render(request, 'home.html', context=context)
        
    return render(request, 'home.html')

def register(request):
    if request.method != 'POST':
        form = UserCreateForm()
    
    form = UserCreateForm(request.POST)
    if form.is_valid():
        #* If the registered user is a doctor, make them inactive
        #* Inactive users cannot login, has to be approved by admin
        user_type = form.cleaned_data['user_type']
        if user_type == 'D':
            form.instance.is_active = False
            form.save()
            messages.add_message(request, messages.WARNING, 'Your account has been created. Please wait for admin approval.')
            return redirect('accounts:home')

        user = form.save()
        login(request, user)
        messages.add_message(request, messages.INFO, f'Welcome {user.get_full_name()}!!!Your account has been registered successfully.')
        return redirect('accounts:home')

    return render(request, 'sign-up.html', {'form': form})
