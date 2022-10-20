from django.db import models

# Create your models here.

class Vuelo(models.Model):
    name= models.CharField(max_length=255)
    fligth_status = models.CharField(max_length=100, choices=(('on time', 'on time'), ('delayed', 'delayed'), ('cancelled', 'cancelled'), ('diverted', 'diverted'), ('unknown', 'unknown'), ('shceduled', 'shceduled')), null=True, blank=True, default='on time')

    def __str__(self):
        return 'flight:' + self.vuelo + ' status: ' +  self.fligth_status