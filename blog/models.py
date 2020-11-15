import datetime

from django.db import models


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=50, verbose_name="Blog bashliq")
    description = models.TextField(verbose_name="Blog haqqinda")
    date = models.DateField(verbose_name="Yaradilma tarixi")

    def __str__(self):
        return self.title
