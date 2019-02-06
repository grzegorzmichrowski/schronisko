from django.forms import ModelForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
# Create your views here.
from django.views.generic import CreateView, UpdateView, DeleteView

from animals.filters import AnimalFilter
from animals.models import Animal, Box
from employees.models import Employee


class MainView(View):

    def get(self, request):
        return render(request, "main.html")


# class AnimalsListView(View):
#
#     def get(self, request):
#         animals = Animal.objects.all()
#         return render(request, "animals/animal_list.html", {"animals": animals})


class AnimalForm(ModelForm):
    class Meta:
        model = Animal
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(AnimalForm, self).__init__(*args, **kwargs)
        self.fields['caretaker'].queryset = Employee.objects.filter(profession=2)


class AnimalCreate(CreateView):

    form_class = AnimalForm
    success_url = reverse_lazy("add_animal")
    template_name = 'animals/animal_form.html'


class AnimalUpdate(UpdateView):

    form_class = AnimalForm
    model = Animal
    template_name_suffix = '_update_form'
    template_name = 'animals/animal_update_form.html'


class AnimalDelete(DeleteView):

    model = Animal
    success_url = '/animal_list'


class AnimalListWithFilterView(View):

    def get(self, request):
        animal_list = Animal.objects.all()
        animal_list = AnimalFilter(request.GET, queryset=animal_list)
        return render(request, 'animals/animal_list.html', {'filter': animal_list})


class BoxCreate(CreateView):

    model = Box
    fields = "__all__"
    success_url = reverse_lazy("add_box")
