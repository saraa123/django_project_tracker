from django.shortcuts import render
from django.db.models import Q
from products.models import Product
from to_do.models import Item, Feature

def search_product(request):
    products = Product.objects.filter(name__icontains=request.GET['q'])
    return render(request, 'products.html', {"products": products})

def search_issues_and_features(request):
    """ Function to search issues and features """

    # Create an instance of the search query 
    q = request.GET['q']

    # Query the database - filter issues and features based on what's searched on the site    
    search_issue = Item.objects.filter(Issue__icontains=request.GET['q']).values('Issue', 'done')
    search_feature = Feature.objects.filter(name__icontains=request.GET['q']).values('name', 'done')

    return render(request, 'search_results.html', {
                  "search_issue": search_issue, 
                  "search_feature": search_feature, 
                  "q": q})

