import django_filters

from animals.models import Animal


class AnimalFilter(django_filters.FilterSet):

    class Meta:
        model = Animal
        fields = ["sex", "health_state", "size"]
