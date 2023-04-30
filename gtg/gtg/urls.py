"""
URL configuration for gtg project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.contrib import admin
from cafe import views

urlpatterns = [
    # ... other URL patterns in your project ...
    path('cafe/', include('cafe.urls')),  # Include cafe app's URLs
    path('admin/', admin.site.urls),
    path('cart/', views.cart, name='cart'),
    path('confirm_order/', views.order_confirmation, name='confirm_order'),
    path('add_to_cart/<int:drink_id>/', views.add_to_cart, name='add_to_cart'),
]

