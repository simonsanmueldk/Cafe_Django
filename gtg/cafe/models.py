from django.shortcuts import render, redirect
from django.db import models
from django.contrib.auth.models import User

class Drink(models.Model):
    CATEGORY_CHOICES = (
        ('coffee', 'Coffee'),
        ('tea', 'Tea'),
        ('juice', 'Juice')
    )
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)

    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

class Order(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
   

def add_to_cart(request, drink_id):
    drink = Drink.objects.get(id=drink_id)
    order, created = Order.objects.get_or_create(user=request.user, drink=drink, status='pending')
    if created:
        order.quantity = 1
    else:
        order.quantity += 1
    order.save()
    return redirect('cart')

