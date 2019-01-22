from django.db import models

# Create your models here.
from employees.models import Employee

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


class Box(models.Model):
    section = models.CharField(max_length=1)
    number = models.IntegerField()


class Animal(models.Model):
    name = models.CharField(max_length=64)
    age = models.IntegerField()
    health_state = models.IntegerField(choices=HEALTH_STATES)
    size = models.IntegerField(choices=PET_SIZE)
    description = models.TextField()
    caretaker = models.ForeignKey(Employee, on_delete=models.CASCADE)
    box = models.ForeignKey(Box, on_delete=models.CASCADE)
