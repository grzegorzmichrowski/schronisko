from django.forms import ModelForm
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView

from adoption.models import UserDetails


class UserDetailsForm(ModelForm):

    class Meta:
        model = UserDetails
        exclude = ["user"]


class UserDetailsCreate(CreateView):

    form_class = UserDetailsForm
    success_url = reverse_lazy("form_confirmation")
    template_name = 'adoption/userdetails_form.html'


class FormConfirmationView(View):

    def get(self, request):
        return render(request, "adoption/form_confirmation.html")
