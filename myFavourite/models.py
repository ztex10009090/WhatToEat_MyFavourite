from django.db import models


# Create your models here.
class MyFavourite(models.Model):
    MyFavouriteID = models.AutoField(primary_key=True)
    StoreName = models.CharField(max_length=30)
    Latitude = models.CharField(max_length=30)
    Longitude = models.CharField(max_length=30)
    Introduction = models.TextField()

    def __str__(self):
        return self.StoreName
