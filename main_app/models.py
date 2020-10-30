from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Distributor(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    website = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Producer(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    grape = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    distributors = models.ManyToManyField(Distributor)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Wine(models.Model):
    name = models.CharField(max_length=100)
    size = models.IntegerField()
    price = models.IntegerField()

    producer = models.ForeignKey(Producer, on_delete=models.CASCADE)

    def __str__(self):
        return self.name