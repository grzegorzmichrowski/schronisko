from django.db import models

# Create your models here.


class Contact(models.Model):

    name = models.CharField(max_length=255, verbose_name="Nazwa")
    address = models.CharField(max_length=255, verbose_name="Adres")
    email = models.EmailField(verbose_name="E-mail")
    phone_number = models.IntegerField(verbose_name="Numer telefonu")
    bank_account_number = models.IntegerField(verbose_name="Numer konta bankowego")
