from django.db import models
from django.urls import reverse

# Create your models here.


class Hairpun(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  exists = models.BooleanField(default=False)
  link = models.URLField(max_length=200, blank=True)

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse('details', kwargs={'pun_id': self.id})


class Visit(models.Model):
  date = models.DateField()
  thoughts = models.CharField(max_length=250)
  hairpun = models.ForeignKey(Hairpun, on_delete=models.CASCADE)

  def __str__(self):
    return self.date
  
  class Meta:
    ordering = ['-date']