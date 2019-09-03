from django.shortcuts import render
from products.models import Product

def search_product(request):
    products = Product.objects.filter(name__icontains=request.GET['q'])
    return render(request, 'products.html', {"products": products})

