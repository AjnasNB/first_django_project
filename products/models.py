from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField( max_length=255)
    price=models.FloatField()
    stock=models.IntegerField()
    image=models.CharField( max_length=2550)
  
class Offer(models.Model):
    code=models.CharField( max_length=50)
    description=models.CharField( max_length=50)  
    discount=models.FloatField()
    