from django.db import models
from django.contrib.auth.models import AbstractUser

class Resource(models.Model):
    objects = None
    RESOURCE_TYPES = [
        ('book', 'Книга'),
        ('journal', 'Журнал'),
        ('article', 'Стаття'),
        ('internet', 'Інтернет-ресурс'),
    ]

    title = models.CharField(max_length=255)
    authors = models.CharField(max_length=255)
    resource_type = models.CharField(max_length=20, choices=RESOURCE_TYPES)
    page_count = models.PositiveIntegerField()
    publication_year = models.PositiveIntegerField()
    isbn = models.CharField(max_length=13)

class CustomUser(AbstractUser):
    def __str__(self):
        return self.username

    pass

class MyModel(models.Model):
    name = models.CharField(max_length=100)

class Material(models.Model):
    objects = None
    title = models.CharField(max_length=100)
    description = models.TextField()
    author = models.CharField(max_length=100)
    publication_date = models.DateField()

    def __str__(self):
        return self.title