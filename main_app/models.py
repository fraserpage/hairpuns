from django.db import models

# Create your models here.

class Hairpun(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  exists = models.BooleanField(default=False)
  link = models.URLField(max_length=200, blank=True)

  def __str__(self):
    return self.name