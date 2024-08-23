from django.db import models
from django.contrib.auth.models import User

from phonenumber_field.modelfields import PhoneNumberField


class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.name}'


class Institution(models.Model):
    class Type(models.TextChoices):
        FUNDACJA = "FN",
        ORGANIZACJA_POZARZĄDOWA = "OP",
        ZBIÓRKA_LOKALNA = "ZL",

    name = models.CharField(max_length=64)
    description = models.TextField(null=True)
    type = models.CharField(choices=Type.choices, default=Type.FUNDACJA, max_length=2)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return f'{self.name}'


class Donation(models.Model):
    quantity = models.DecimalField(max_digits=4, decimal_places=0, null=True)
    categories = models.ManyToManyField(Category)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    address = models.CharField(max_length=64)
    phone_number = PhoneNumberField(null=True)
    city = models.CharField(max_length=30, null=True)
    zip_code = models.CharField(max_length=6, null=True)
    pick_up_date = models.DateField(null=True)
    pick_up_time = models.TimeField(null=True)
    pick_up_comment = models.TextField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    is_taken = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.institution.name} - {self.pick_up_date}'