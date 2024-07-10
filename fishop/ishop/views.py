from django.shortcuts import HttpResponse
from django.shortcuts import render
from .models import Product

def home(request):
    products = Product.objects.all()

    return render(request, 'index.html', {'products': products})

def view_product(request, id):
    product = Product.objects.filter(id=id).first()
    return render(request,'product.html', {'product': product})