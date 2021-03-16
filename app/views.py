from django.shortcuts import render
from .models import SellOrder, BuyOrder, Profile

# Create your views here.
def home(request):
    return render(request,'app/home.html', {})


def t_balance(request):
    profiles = Profile.objects.all()
    if request.GET.get('profile'):
        profile = request.GET.get('profile')
        revenues = 0
        costs = 0
        profit = 0
        sellorders = SellOrder.objects.filter(profile=profile)
        for sellorder in sellorders:
            revenues += ((sellorder.quantity * sellorder.price) - (sellorder.remaining * sellorder.price))
        buyorders = BuyOrder.objects.filter(profile=profile)
        for buyorder in buyorders:
            costs += ((buyorder.quantity * buyorder.price) - (buyorder.remaining * buyorder.price))
        profit = (revenues - costs)
    else:
        profit = 0
    return render(request, 'app/t_balance.html', {'profiles' : profiles, 'profit' : profit})




def activeOrders(request):
    sellorders  = SellOrder.objects.all().filter(matched = False).order_by('-datetime')
    buyorders = BuyOrder.objects.all().filter(matched = False).order_by('-datetime')
    return render(request, 'app/activeOrders.html', {'buyorders' : buyorders, 'sellorders' : sellorders})
