from django.db import models

# Create your models here.
# class Wine:
#     def __init__(self, name, region, year):
#         self.name = name
#         self.region = region
#         self.year = year

# wines = [
#     Wine('Chateau Chevel Blanc', 'Chateau Cheval Blanc', 2010),
#     Wine("Chateau d'Yquem", "Chateau d'Yquem", 2011),
#     Wine('Louis Roederer Cristal', 'Louis Roederer', 2007)
# ]

class Wine(models.Model):
    name = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    year = models.IntegerField()