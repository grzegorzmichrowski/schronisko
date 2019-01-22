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
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField()
    date_of_birth = models.DateField()
    contract = models.IntegerField(choices=CONTRACTS)
    profession = models.IntegerField(choices=PROFESSIONS)
