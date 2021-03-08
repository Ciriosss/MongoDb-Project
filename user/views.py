from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, NewBuyOrder
from app.models import Profile, BuyOrder, SellOrder
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,'Congratulations {}! your account has been created successfully, now you are able to log-in'.format(username))
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form})

def profile(request):
    return render(request, 'user/profile.html')

def trade(request):
    #profile = User.objects.get(username = request.user)
    if request.method == 'POST':
        form = NewBuyOrder(request.POST)
        if form.is_valid():
            newbuyorder = form.save(commit=False)
            price = request.POST.get('price')
            quantity = request.POST.get('quantity')
            BuyOrder.objects.create(profile = profile, price = price, quantity = quantity)
            return redirect('home')

    else:
        form = NewBuyOrder()
    return render(request, 'user/trade.html', {'form' : form})
