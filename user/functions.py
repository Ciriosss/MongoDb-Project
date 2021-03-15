from app.models import Profile, BuyOrder, SellOrder
from django.contrib.auth.models import User
import random

#function for create random BTC
def randombtc():
    return round(random.uniform(1,10),2)


#function for create a new profile at registration moment
def newProfile(username):
    user = User.objects.get(username=username)
    initial_btc = randombtc()
    BTC = initial_btc
    Profile.objects.create(user=user, initial_btc=initial_btc, BTC=BTC, balance=0)

def matchbuyOrder(order):
    sellorders = SellOrder.objects.filter(matched = False, price__lte = order.price).order_by('price')

    if len(sellorders) > 0:
        i = 0
        while  (order.matched == False) or (i <= ( len(sellorders) - 1)) :
            sellorder = sellorders[i]
            if order.remaining > sellorder.quantity :
                sellorder.matched = True
                sellorder.remaining = 0
                order.remaining = order.quantity - sellorder.quantity
                sellorder.save()
                order.save()
                i += 1
                break

            elif order.remaining == sellorder.quantity :
                sellorder.matched = True
                order.matched = True
                sellorder.remaining = 0
                order.remaining = 0
                sellorder.save()
                order.save()
                break

            elif order.remaining < sellorder.quantity :
                order.matched = True
                order.remaining = 0
                sellorder.remaining = sellorder.quantity - order.quantity
                sellorder.save()
                order.save()


def matchsellOrder(order):
    buyorders = BuyOrder.objects.filter(matched = False, price__gte = order.price).order_by('-price')

    if len(buyorders) > 0:
        i = 0
        while  (order.matched == False) or (i <= ( len(buyorders) - 1)) :
            buyorder = buyorders[i]
            if order.remaining > buyorder.quantity :
                buyorder.matched = True
                buyorder.remaining = 0
                order.remaining = order.quantity - buyorder.quantity
                buyorder.save()
                order.save()
                i += 1
                break

            elif order.remaining == buyorder.quantity:
                buyorder.matched = True
                order.matched = True
                buyorder.remaining = 0
                order.remaining = 0
                buyorder.save()
                order.save()
                break

            elif order.remaining < buyorder.quantity :
                order.matched = True
                order.remaining = 0
                buyorder.remaining = buyorder.quantity - order.quantity
                buyorder.save()
                order.save()


