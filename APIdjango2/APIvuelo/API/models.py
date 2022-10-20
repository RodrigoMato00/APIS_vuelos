from django.db import models

# Create your models here.

class Vuelo(models.Model):
    date = models.DateField(null=True , blank=True)
    flight_hour = models.TimeField(null=True, blank=True)
    flight_status = models.CharField(max_length=100, choices=(('on time', 'on time'), ('delayed', 'delayed'), ('cancelled', 'cancelled'), ('diverted', 'diverted'), ('unknown', 'unknown'), ('shceduled', 'shceduled')), null=True, blank=True, default='on time')
    airline = models.CharField(max_length=100, choices=(('OTHER', 'OTHER'), ('AIRLINE', 'AIRLINE')), null=True, blank=True, default='AIRLINE')
    airline_name = models.CharField(max_length=100, null=True, blank=True)
    airline_IATA = models.CharField(max_length=100, null=True, blank=True)
    airline_ICAO = models.CharField(max_length=100, null=True, blank=True)
    flight = models.CharField(max_length=100, choices=(('OTHER', 'OTHER'), ('FLIGHT', 'FLIGHT')), null=True, blank=True, default='FLIGHT')
    number = models.IntegerField(null=True, blank=True)
    IATA = models.CharField(max_length=100, null=True, blank=True)
    ICAO = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return 'flight:' + self.ICAO + str(self.date) + str(self.flight_hour) + self.flight_status
