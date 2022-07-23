from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from .forms import CustomLoginForm
from django.contrib.auth import get_user_model

app_name = 'accounts' #* Add app_name for namespace

urlpatterns = [
    path('', views.home, name='home'),
    path('login', auth_views.LoginView.as_view(
            template_name='login.html', 
            next_page='accounts:home',
            # authentication_form=CustomLoginForm
            ), 
        name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('register', views.register, name='register'),
]