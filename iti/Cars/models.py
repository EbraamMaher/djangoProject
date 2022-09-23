from django.db import models
from django.shortcuts import reverse

# Create your models here.


class Car(models.Model):
    model = models.CharField(max_length=100)
    price = models.IntegerField(default=200000)
    production_year = models.IntegerField(default=2000)

    def __str__(self):
        return f"{self.model}"

    @classmethod
    def get_all_cars(cls):
        return cls.objects.all()

    def get_show_url(self):
        return reverse("Cars.show", args=[self.id])

    def get_edit_url(self):
        return reverse("Cars.edit", args=[self.id])

    def get_delete_url(self):
        return reverse("Cars.delete", args=[self.id])
