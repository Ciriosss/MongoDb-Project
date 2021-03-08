from django.shortcuts import render
from .models import SellOrder, BuyOrder

# Create your views here.
def home(request):
    return render(request,'app/home.html', {})

def t_balance(request):
    return render(request, 'app/t_balance.html', {})

def activeOrders(request):
    sellOrders  = SellOrder.objects.all()
    buyOrders = BuyOrder.objects.all()
    return render(request, 'app/activeOrders.html', {'buyOrders' : buyOrders, 'sellOrders':sellOrders})