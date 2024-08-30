from django.db import models

# Create your models here.



class Region(models.Model):

    name = models.CharField(max_length=255)
    about = models.TextField()

    def __str__(self):
        return f'{self.id}-{self.name}'


class Bout(models.Model):
    name = models.CharField(max_length=20)
    about = models.TextField()
    def __str__(self):
        return f'{self.id}-{self.name}'