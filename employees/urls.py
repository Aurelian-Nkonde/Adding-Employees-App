from django.urls import path
from . views import (
    Home,
    EmployeeList, 
    EmployeeDetail, 
    EmployeeDelete,
    EmployeeCreate
)
urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('dashbord/', EmployeeList.as_view(), name='list'),
    path('dashbord/<int:pk>/', EmployeeDetail.as_view(), name='detail'),
    path('dashbord/<int:pk>/delete/', EmployeeDelete.as_view(), name="delete"),
    path('dashbord/create/', EmployeeCreate.as_view(), name="create")
]