from django.shortcuts import render
from .models import Product

def all_products(request):
    """ Render the products page. It will be used to 
    display the tickets for new issues and features. """

    return render(request, 'products.html')
