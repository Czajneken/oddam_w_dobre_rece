from django.db import models


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
    type = models.IntegerField(choices=TYPES)
    categories = models.ManyToManyField(Category, default=1)


