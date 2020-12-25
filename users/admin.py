from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser
from .forms import CustomChange, CustomCreation

class CustomAdmin(UserAdmin):
    add_form = CustomCreation
    form = CustomChange
    model = CustomUser
    list_display = ['username','email','is_staff']

admin.site.register(CustomUser, CustomAdmin)