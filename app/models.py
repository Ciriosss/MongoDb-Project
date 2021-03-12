from django.db import models
from django.contrib.auth.models import User
from djongo.models.fields import ObjectIdField

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    initialBTC = models.FloatField()
    BTC = models.FloatField()
    balance = models.FloatField()

class BuyOrder(models.Model):

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)
    price = models.FloatField()
    quantity = models.FloatField()

class SellOrder(models.Model):

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)
    price = models.FloatField()
    quantity = models.FloatField()
