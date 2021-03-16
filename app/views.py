from django.shortcuts import render
from .models import SellOrder, BuyOrder

# Create your views here.
def home(request):
    return render(request,'app/home.html', {})

def t_balance(request):
    return render(request, 'app/t_balance.html', {})

def activeOrders(request):
    sellorders  = SellOrder.objects.all().filter(matched = False).order_by('-datetime')
    buyorders = BuyOrder.objects.all().filter(matched = False).order_by('-datetime')
    return render(request, 'app/activeOrders.html', {'buyorders' : buyorders, 'sellorders' : sellorders})