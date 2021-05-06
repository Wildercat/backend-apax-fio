from django.db import models

class User(models.Model):
    username = models.CharField(max_length=200)
    def __str__(self):
        return self.username

class Location(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location_name = models.CharField(max_length=200)
    def __str__(self):
        return self.location_name

