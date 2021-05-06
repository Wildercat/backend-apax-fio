from django.db import models

class User(models.Model):
    username = models.CharField(max_length=200)
    def __str__(self):
        return self.username

class Location(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location_name = models.CharField(max_length=200, blank=True, null=True)
    zip_code = models.CharField(max_length=5)
    weather_main = models.CharField(max_length=50, blank=True, null=True)
    weather_desc = models.CharField(max_length=50, blank=True, null=True)
    weather_icon = models.CharField(max_length=50, blank=True, null=True)

    main_temp = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    main_temp_min = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    main_temp_max = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    def __str__(self):
        return self.location_name
