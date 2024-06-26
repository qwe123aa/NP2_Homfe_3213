from django.db import models

class user_info(models.Model):
    id = models.CharField(max_length=12, primary_key=True)
    password = models.CharField(max_length=12)

    def __str__(self):
        return f'{self.id}, {self.password}'

class recipe(models.Model):
    name = models.CharField(max_length=50);
    pic = models.ImageField(upload_to='images/')
    material = models.CharField(max_length=200);
    process = models.TextField();

    def __str__(self):
        return f'{self.name}, {self.material}, {self.process}'
