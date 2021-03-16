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
    profile = Profile.objects.create(user=user, initial_btc=initial_btc, BTC=BTC, balance=0)
    profile.save()

def matchbuyOrder(order, request):
    sellorders = SellOrder.objects.filter(matched = False, price__lte = order.price).order_by('price')
    user = User.objects.get(username = request.user)
    buyer = Profile.objects.get(user = user)
    if len(sellorders) > 0:
        i = 0
        while  (order.matched == False) and (i <= ( len(sellorders) - 1)) :
            sellorder = sellorders[i]
            profile = sellorder.profile
            seller = Profile.objects.get(id=profile.id)
            if order.remaining > sellorder.remaining :
                buyer.balance -= float(order.price) * float(sellorder.remaining)
                seller.balance += float(order.price) * float(sellorder.remaining)
                buyer.BTC += sellorder.remaining
                seller.BTC -= sellorder.remaining
                order.remaining -= sellorder.remaining
                sellorder.remaining = 0
                sellorder.matched = True
                sellorder.save()
                order.save()
                buyer.save()
                seller.save()
                i += 1

            elif order.remaining == sellorder.remaining :
                buyer.balance -= float(order.price) * float(order.remaining)
                seller.balance += float(order.price) * float(order.remaining)
                buyer.BTC += sellorder.remaining
                seller.BTC -= sellorder.remaining
                sellorder.remaining = 0
                order.remaining = 0
                sellorder.matched = True
                order.matched = True
                sellorder.save()
                order.save()
                buyer.save()
                seller.save()
                break

            elif order.remaining < sellorder.remaining :
                buyer.balance -= float(order.price) * float(order.remaining)
                seller.balance += float(order.price) * float(order.remaining)
                buyer.BTC += order.remaining
                seller.BTC -= order.remaining
                sellorder.remaining -= order.remaining
                order.remaining = 0
                order.matched = True
                sellorder.save()
                order.save()
                buyer.save()
                seller.save()
                break

def matchsellOrder(order, request):
    buyorders = BuyOrder.objects.filter(matched = False, price__gte = order.price).order_by('-price')
    user = User.objects.get(username=request.user)
    seller = Profile.objects.get(user=user)
    if len(buyorders) > 0:
        i = 0
        while  (order.matched == False) and (i <= ( len(buyorders) - 1 )) :
            buyorder = buyorders[i]
            profile = buyorder.profile
            buyer = Profile.objects.get(id=profile.id)
            if order.remaining > buyorder.remaining :
                seller.balance += float(buyorder.price) * float(buyorder.remaining)
                buyer.balance -= float(buyorder.price) * float(buyorder.remaining)
                seller.BTC -= buyorder.remaining
                buyer.BTC += buyorder.remaining
                order.remaining -= buyorder.remaining
                buyorder.remaining = 0
                buyorder.matched = True
                buyer.save()
                seller.save()
                buyorder.save()
                order.save()
                i += 1

            elif order.remaining == buyorder.remaining:
                seller.balance += float(buyorder.price) * float(buyorder.remaining)
                buyer.balance -= float(buyorder.price) * float(buyorder.remaining)
                buyer.BTC += buyorder.remaining
                seller.BTC -= buyorder.remaining
                buyorder.matched = True
                order.matched = True
                buyorder.remaining = 0
                order.remaining = 0
                buyorder.save()
                order.save()
                buyer.save()
                seller.save()
                break

            elif order.remaining < buyorder.remaining :
                seller.balance += float(buyorder.price) * float(order.remaining)
                buyer.balance -= float(buyorder.price) * float(buyorder.remaining)
                buyer.BTC += order.remaining
                seller.BTC -= order.remaining
                buyorder.remaining -= order.remaining
                order.remaining = 0
                order.matched = True
                buyorder.save()
                order.save()
                break


