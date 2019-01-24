from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView

from employees.models import Employee


class EmployeeCreate(CreateView):

    model = Employee
    fields = "__all__"
    success_url = reverse_lazy("add_employee")