from django.db import models

# Create your models here.



class Place(models.Model):
    address = models.CharField(max_length=20)

class Club(Place):
    name = models.CharField(max_length=20)

class Resouce(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    res_name = models.CharField(max_length=20)