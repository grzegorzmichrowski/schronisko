from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic import UpdateView

from contact.models import Contact


class ContactUpdate(UpdateView):

    model = Contact
    template_name_suffix = '_update_form'
    fields = "__all__"


class ContactView(View):

    def get(self, request):
        contact = Contact.objects.all()
        return render(request, "contact/contact.html", {"contact": contact})
