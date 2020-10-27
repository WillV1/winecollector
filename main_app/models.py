from django.db import models

# Create your models here.
class Producer(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    grape = models.CharField(max_length=100)
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.name


class Wine(models.Model):
    name = models.CharField(max_length=100)
    size = models.IntegerField()
    price = models.IntegerField()

    producer = models.ForeignKey(Producer, on_delete=models.CASCADE)

    def __str__(self):
        return self.name