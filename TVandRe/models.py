from django.db import models

class TV(models.Model):
    title = models.CharField(max_length=12, unique=True)
    img_url = models.CharField(max_length = 25)
    count_of_views = models.IntegerField()
    
    def __str__(self):
        return self.title

class Refrigerator(models.Model):
    title = models.CharField(max_length=12, unique=True)
    img_url = models.CharField(max_length = 25)
    count_of_views = models.IntegerField()

    def __str__(self):
        return self.title
