from django.shortcuts import HttpResponse
from django.shortcuts import render
from .models import Product

def home(request):
    search = request.GET.get('search')

    if search:
        products = Product.objects.filter(name__contains=search).all()
    else:
        products = Product.objects.all()

    return render(request, "index.html", {
        'products': products,
        'products_found': len(products) > 0,
        'search': search if search else '',
    })


def view_product(request, id):
    product = Product.objects.filter(id=id).first()
    return render(request,'product.html', {'product': product})