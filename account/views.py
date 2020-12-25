from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.views.generic import CreateView
from django.urls import reverse_lazy


from .forms import RegisterForm

class Register(CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy('login')
    template_name = 'register.html'