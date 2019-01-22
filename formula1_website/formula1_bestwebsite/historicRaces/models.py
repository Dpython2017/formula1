from django.db import models

# Create your models here.


class Fastest_laps(models.Model):

    grand_prix = models.CharField(max_length=15)
    driver = models.CharField(max_length=25)
    car_model = models.CharField(max_length=50)
    time_taken = models.CharField(blank=True, max_length=8)

    def __str__(self):
        return self.grand_prix
