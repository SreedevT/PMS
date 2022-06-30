from atexit import register
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# https://stackoverflow.com/questions/48011275/custom-user-model-fields-abstractuser-not-showing-in-django-admin
fields = list(UserAdmin.fieldsets)
fields.insert(2, ('Other Info', {'fields': ('user_type', 'gender', 'phone')}))
UserAdmin.fieldsets = tuple(fields)

admin.site.register(User, UserAdmin)