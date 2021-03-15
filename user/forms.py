from django import forms
from app.models import BuyOrder, SellOrder
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

class NewSellOrder(forms.ModelForm):
    price = forms.CharField(max_length=10)
    quantity = forms.CharField(max_length=10)

    class Meta:
        model = SellOrder
        fields = ['price', 'quantity']