from django.contrib import admin
from .models import Product 

# Enable admin panel to add procuts to site 
admin.site.register(Product)