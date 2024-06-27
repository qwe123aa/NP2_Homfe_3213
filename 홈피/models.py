from django.contrib.auth.models import User
from django.db import models


class recipe(models.Model):
    name = models.CharField(max_length=50)
    pic = models.ImageField(upload_to='images/')
    material = models.CharField(max_length=200)
    process = models.TextField()

    def __str__(self):
        return f'{self.name}, {self.material}, {self.process}'

