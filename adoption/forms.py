from django.forms import ModelForm
from adoption.models import AdoptionForm


class AdoptionFormForm(ModelForm):

    class Meta:
        model = AdoptionForm
        fields = "__all__"
