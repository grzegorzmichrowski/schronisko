from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView

from adoption.forms import AdoptionFormForm


class AdoptionFormCreate(CreateView):

    form_class = AdoptionFormForm
    success_url = reverse_lazy("form_confirmation")
    template_name = 'adoption/adoptionform_form.html'


class FormConfirmationView(View):

    def get(self, request):
        return render(request, "adoption/form_confirmation.html")
