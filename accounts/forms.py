# from django.contrib.auth import get_user_model #? May be needed
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms


class UserCreateForm(UserCreationForm):
    class Meta:
        fields = ("first_name", "last_name", "username", "email", "password1", "password2", "user_type", "gender", "phone")

        model = User #? Might be or might not be needed. 
        #! IF NOT NEEDED BECAUSE AUTH_USER_MODEL SET IN SETTINGS.PY

        widgets = {
            'user_type': forms.RadioSelect(),
            'gender': forms.RadioSelect(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) #super calls the parent class. parent callses init is called first
        self.fields["username"].label = "Username" #.label is how it shows up in from as the input name ie. field name
        self.fields["email"].label = "Email address"
        self.fields["phone"].lable = "Phone number" #? WHY