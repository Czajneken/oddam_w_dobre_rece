from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=64)


class Institution(models.Model):
    TYPES = (
        (1, "Fundacja"),
        (2, "Organizacja pozarządowa"),
        (3, "Zbiórka lokalna")
    )

    name = models.CharField(max_length=64)
    description = models.TextField
    type = models.IntegerField(choices=TYPES, default=1)
    categories = models.ManyToManyField(Category)


class Donation(models.Model):
    quantity = models.DecimalField(max_digits=4, decimal_places=0, null=True)
    categories = models.ManyToManyField(Category)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    address = models.CharField(max_length=64)
    phone_number = models.SmallIntegerField
    city = models.CharField(max_length=30, null=True)
    zip_code = models.CharField(max_length=6, null=True)
    pick_up_date = models.DateField
    pick_up_time = models.TimeField
    pick_up_comment = models.TextField
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
