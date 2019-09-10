from django.contrib import admin
from .models import Product

# Enable admin panel to add products to site
admin.site.register(Product)