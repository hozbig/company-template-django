from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True)
    position = models.IntegerField()

    def __str__(self):
        return self.title