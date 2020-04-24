from django.shortcuts import render
from django.db.models import Q
from products.models import Product
from to_do.models import Item, Feature

def search_product(request):
    products = Product.objects.filter(name__icontains=request.GET['q'])
    return render(request, 'products.html', {"products": products})

def search_issues_and_features(request):
    """ Function to search issues and features """
    
    search_query = (Q(Item.objects.filter(Issue__icontains=request.GET['q']).values('Issue')) | Q(Feature.objects.filter(name__icontains=request.GET['q']).values('name')))
    
    return render(request, 'search_results.html', {"search_results": search_query})

