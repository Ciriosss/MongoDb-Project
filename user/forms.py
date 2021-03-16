from django import forms
from app.models import BuyOrder, SellOrder, Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

class NewBuyOrder(forms.ModelForm):
    price = forms.CharField(max_length=10)
    quantity = forms.CharField(max_length=10)

    class Meta:
        model = BuyOrder
        fields = ['price', 'quantity']

    def checkBalance(self, request):
        user = User.objects.get(username=request.user)
        profile = Profile.objects.get(user=user)
        balance = profile.balance
        price = self.cleaned_data.get('price')
        quantity = self.cleaned_data.get('quantity')
        total = float(price) * float(quantity)
        if (total > balance) :
            return None
        return price, quantity



class NewSellOrder(forms.ModelForm):
    price = forms.CharField(max_length=10)
    quantity = forms.CharField(max_length=10)

    class Meta:
        model = SellOrder
        fields = ['price', 'quantity']

    def checkBTC(self, request):
        user = User.objects.get(username=request.user)
        profile = Profile.objects.get(user=user)
        BTC = profile.BTC
        quantity = self.cleaned_data.get('quantity')
        price = self.cleaned_data.get('price')

        quantity = float(quantity)
        BTC = float(BTC)

        if (quantity > BTC) :
            return None
        return price, quantity