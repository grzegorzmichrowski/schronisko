from django.db import models

# Create your models here.


PROFESSIONS = (
    (1, "Weterynarz"),
    (2, "Opiekun"),
    (3, "Recepcjonistka"),
    (4, "Ochroniarz"),
    (5, "Osoba sprzątająca")
)

CONTRACTS = (
    (1, "Umowa o pracę"),
    (2, "Umowa zlecenie"),
    (3, "Wolontariat")
)


class Employee(models.Model):
    first_name = models.CharField(max_length=64, verbose_name="Imię")
    last_name = models.CharField(max_length=64, verbose_name="Nazwisko")
    email = models.EmailField(verbose_name="E-mail")
    date_of_birth = models.CharField(max_length=64, verbose_name="Data urodzenia")
    contract = models.IntegerField(choices=CONTRACTS, verbose_name="Rodzaj umowy")
    profession = models.IntegerField(choices=PROFESSIONS, verbose_name="Stanowisko")
