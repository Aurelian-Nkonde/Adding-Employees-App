from django.contrib import admin

from .models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','empl_gender','email','phone']
    list_filter = ['first_name','email']