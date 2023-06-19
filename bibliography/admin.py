from django.contrib import admin

from . import models
from .models import MyModel

@admin.register(MyModel)
class MyModel(models.Model):
    field1 = models.CharField(max_length=50)
    field2 = models.IntegerField()
    field3 = models.DateField()

    def __str__(self):
        return self.field1

class MyModelAdmin(admin.ModelAdmin):
    list_display = ('field1', 'field2', 'field3')
    search_fields = ('field1', 'field2')
    list_filter = ('field3',)

