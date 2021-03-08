from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name = 'home'),
    path('t_balance/', views.t_balance, name = 't_balance'),
    path('activeOrders/', views.activeOrders, name = 'activeOrders')
]
