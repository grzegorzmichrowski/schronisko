from django.db import models

# Create your models here.
from Projekt_koncowy import settings
from employees.models import Employee
from PIL import Image


def get_display(key, list):
    d = dict(list)
    if key in d:
        return d[key]
    return None


HEALTH_STATES = (
    (1, "Zdrowy"),
    (2, "Choruje przewlekle"),
    (3, "Niepełnosprawny")
)

PET_SIZE = (
    (1, "Mały"),
    (2, "Średni"),
    (3, "Duży")
)

SEX = (
    (1, "Samiec"),
    (2, "Samica")
)


BOX_SECTIONS = (
    (1, "A"),
    (2, "B"),
    (3, "C"),
    (4, "D"),
    (5, "E"),
    (6, "F"),
    (7, "G"),
    (8, "H"),
)


class Box(models.Model):
    section = models.IntegerField(choices=BOX_SECTIONS, verbose_name="Sekcja")
    number = models.IntegerField(verbose_name="Numer")

    def __str__(self):
        return f"{BOX_SECTIONS[self.section - 1][1]}{self.number}"


class Animal(models.Model):
    name = models.CharField(max_length=64, verbose_name="Imię")
    age = models.IntegerField(verbose_name="Wiek")
    sex = models.IntegerField(choices=SEX, verbose_name="Płeć")
    health_state = models.IntegerField(choices=HEALTH_STATES, verbose_name="Stan zdrowia")
    size = models.IntegerField(choices=PET_SIZE, verbose_name="Wielkość")
    description = models.TextField(verbose_name="Opis")
    caretaker = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name="Opiekun")
    box = models.ForeignKey(Box, on_delete=models.CASCADE, verbose_name="Boks")
    img = models.ImageField(verbose_name="Zdjęcie", blank=True, null=True)

    def display_sex(self):
        return get_display(self.sex, SEX)

    def display_health_state(self):
        return get_display(self.health_state, HEALTH_STATES)

    def display_size(self):
        return get_display(self.size, PET_SIZE)
