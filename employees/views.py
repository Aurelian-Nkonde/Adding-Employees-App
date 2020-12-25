from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import EmployeeForm


from .models import Employee

class Home(LoginRequiredMixin ,TemplateView):
    template_name = 'home.html'
    context_object_name = 'home'
    login_url = 'login'

class EmployeeList(LoginRequiredMixin ,ListView):
    model = Employee
    template_name = 'list.html'
    context_object_name = 'list'
    login_url = 'login'

class EmployeeDetail(LoginRequiredMixin ,DetailView):
    model = Employee
    template_name = 'detail.html'
    context_object_name = "detail"
    login_url = 'login'

class EmployeeDelete(LoginRequiredMixin ,DeleteView):
    model = Employee
    template_name = 'delete.html'
    context_object_name = "delete"
    success_url = reverse_lazy('list')
    login_url = 'login'

class EmployeeCreate(LoginRequiredMixin,CreateView):
    model = Employee
    template_name = 'create.html'
    context_object_name = "create"
 
    form_class = EmployeeForm
    login_url = "login"