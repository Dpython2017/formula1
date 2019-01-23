from django.db import models

# Create your models here.


class Fastest_laps(models.Model):
    driver_name = models.CharField(max_length=25, null=True)
    grand_prix = models.CharField(max_length=15, blank=True)
    car_model = models.CharField(max_length=50)
    time_taken = models.CharField(blank=True, max_length=8)

    def __str__(self):
        return self.driver_name


class Driver(models.Model):

    place_of_birth = models.CharField(max_length=25)
    driver = models.ForeignKey(Fastest_laps, db_column='driver_name')
    picture = models.ImageField(blank=True, null=True)

    def __str__(self):
        return str(self.driver)