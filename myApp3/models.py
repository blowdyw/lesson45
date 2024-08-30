from django.db import models

# Create your models here.



class Blog(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()

    def __str__(self):
        return f'{self.id}- {self.title}'




class Area(models.Model):
    name = models.CharField(max_length=50)
    about = models.TextField()

    def __str__(self):
        return f'{self.id}-{self.name}'
