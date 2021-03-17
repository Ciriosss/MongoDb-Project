from django.shortcuts import render
from .models import SellOrder, BuyOrder, Profile

# Create your views here.
def home(request):
    return render(request,'app/home.html', {})


def profit(request):
    profiles = Profile.objects.all()
    id = 0
    if request.GET.get('profile'):
        id = request.GET.get('profile')
        profile = Profile.objects.get(id = id)
        revenues = 0
        costs = 0
        profit = 0
        message = ''

        buyorders = BuyOrder.objects.filter(profile=profile)
        sellorders = SellOrder.objects.filter(profile=profile)

        if (len(sellorders) == 0 )and (len(buyorders) == 0):
            profit = 0
            message = 'This user has not performed any transactions yet '

        elif (len(sellorders) > 0) and  (len(buyorders) == 0):
            for sellorder in sellorders:
                revenues += ((sellorder.quantity - sellorder.remaining) * (sellorder.price))
            profit = revenues
            message = 'This user has only placed sales orders'

        elif (len(sellorders) == 0) and  (len(buyorders) > 0):
            for buyorder in buyorders:
                costs += ((buyorder.quantity * buyorder.price) - (buyorder.remaining * buyorder.price))
            profit -= costs
            message = 'This user has only placed buy orders, he never sold'

        else:
            for sellorder in sellorders:
                revenues += ((sellorder.quantity - sellorder.remaining) * (sellorder.price))

            for buyorder in buyorders:
                costs += ((buyorder.quantity * buyorder.price) - (buyorder.remaining * buyorder.price))
            profit = revenues - costs
        return render(request, 'app/profit.html',{'profiles': profiles, 'profit': profit, 'id': id, 'message': message})

    return render(request, 'app/profit.html', {'profiles' : profiles})




def orderBook(request):
    sellorders  = SellOrder.objects.all().filter(matched = False).order_by('-datetime')
    buyorders = BuyOrder.objects.all().filter(matched = False).order_by('-datetime')
    return render(request, 'app/orderBook.html', {'buyorders' : buyorders, 'sellorders' : sellorders})
