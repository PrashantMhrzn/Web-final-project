from django.contrib.auth.models import User
from django.db import models


class Car(models.Model):
    img = models.ImageField(upload_to="cars", blank=True, null=True)
    model_name = models.CharField(max_length=200, null=False)
    make_name = models.CharField(max_length=200, null=False)
    make_year = models.PositiveIntegerField(null=False)
    mileage = models.PositiveIntegerField(null=False)
    price = models.PositiveIntegerField(null=False)
    seller_id = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=200, null=False, default="")

    def __str__(self):
        return self.model_name
