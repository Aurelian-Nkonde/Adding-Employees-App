from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import CustomUser

class CustomCreation(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email',)

class CustomChange(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email',)