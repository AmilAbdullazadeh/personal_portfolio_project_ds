from django.db import models


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=50, verbose_name="Bashliq")
    description = models.CharField(max_length=250, verbose_name="Haqqinda")
    image = models.ImageField(upload_to='portfolio/images/', verbose_name="Shekil", blank=True)
    url = models.URLField(verbose_name="Link", blank=True)

    def __str__(self):
        return self.title
