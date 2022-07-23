# from django.contrib.auth import get_user_model #? May be needed
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User
from django import forms


class UserCreateForm(UserCreationForm):
    class Meta:
        fields = ("username", "first_name", "last_name", "email", "password1", "password2", "user_type", "gender", "phone")

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
        self.fields['username'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Username'}
        )
        self.fields['password1'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Password'}
        )
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Confirm Password'}
        )
        self.fields['first_name'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'First Name'}
        )
        self.fields['last_name'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Last Name'}
        )
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Email'}
        )
        self.fields['phone'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Phone'}
        )
        # self.fields['user_type'].widget.attrs.update(
        #     {'class': 'form-control', 'placeholder': 'User Type'}
        # )
        # self.fields['gender'].widget.attr.update(
        #     {'class': 'form-control', 'placeholder': 'Gender'}
        # )



class CustomLoginForm(AuthenticationForm):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

    self.fields['username'].widget.attrs.update(
        {'class': 'form-control', 'placeholder': 'Username'}
    )
    self.fields['password'].widget.attrs.update(
        {'class': 'form-control', 'placeholder': 'Password'}
    )
