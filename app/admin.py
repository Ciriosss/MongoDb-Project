from django.contrib import admin
from .models import Profile, BuyOrder, SellOrder

admin.site.register([Profile, BuyOrder, SellOrder])
