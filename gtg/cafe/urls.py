from django.urls import path
from . import views

urlpatterns = [
    path('', views.drink_catalog, name='drink_catalog'),
    path('cart/', views.cart, name='cart'),
    path('confirm_order/', views.order_confirmation, name='confirm_order'),
    path('add_to_cart/<int:drink_id>/', views.add_to_cart, name='add_to_cart'),

]

