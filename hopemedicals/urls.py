"""hopemedicals URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from home.views import home
from products.views import productslist,addpro
from orders.views import orderslist
from home.views import login
from home.views import signup
from home.views import contactus
from orders.views import addorders

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
    path('index.html',home),
    path('products/',productslist),
    path('orders/',orderslist),
    path('login.html/',login),
    path('signup.html/',signup),
    path('contactus.html/',contactus),
    path('addproducts.html/',addpro),
    path('addproducts.html/products/',productslist),
    path('products/addorders.html/',addorders),
    path('products/addorders.html/orders/',orderslist),
]