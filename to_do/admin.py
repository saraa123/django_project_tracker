from django.contrib import admin
from .models import Item, Feature

# Register use of issues in admin 
admin.site.register(Item)

# Register use of features in admin
admin.site.register(Feature)