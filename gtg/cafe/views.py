from django.shortcuts import render, redirect
from .models import Drink, Order


def drink_catalog(request):
    drinks = Drink.objects.all()
    return render(request, 'drink_catalog.html', {'drinks': drinks})

def add_to_cart(request, drink_id):
    drink = Drink.objects.get(id=drink_id)
    order, created = Order.objects.get_or_create(user=request.user, drink=drink, status='cart')
    if created:
        order.quantity = 1
    else:
        order.quantity += 1
    order.save()
    return redirect('drink_catalog')

def cart(request):
    orders = Order.objects.filter(user=request.user, status__in=['pending', 'cart'])
    total_price = sum(order.quantity * order.drink.price for order in orders)
    context = {
        'orders': orders,
        'total_price': total_price
    }
    return render(request, 'cart.html', context)



def order_confirmation(request):
    orders = Order.objects.filter(user=request.user, status='cart')
    total_price = sum(order.quantity * order.drink.price for order in orders)
    for order in orders:
        order.status = 'confirmed'
        order.save()
    return render(request, 'order_confirmation.html', {'orders': orders, 'total_price': total_price})

