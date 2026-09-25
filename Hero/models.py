from django.db import models

# Create your models here.

class Superhero(models.Model):

    name = models.CharField(max_length=200)

    real_name = models.CharField(max_length=200)

    gender = models.CharField(max_length=200)

    powers = models.CharField(max_length=200)

    universe = models.CharField(max_length=200)

    def __str__(self):
        return self.name
