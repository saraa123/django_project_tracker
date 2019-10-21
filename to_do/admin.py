from django.contrib import admin
from .models import Item, Feature

class ItemModelAdmin(admin.ModelAdmin):
    list_display = ["__str__", "timestamp", "done"]
    list_filter = ["done", "timestamp"]
    class Meta:
        model = Item


# Register use of issues in admin
admin.site.register(Item, ItemModelAdmin)

# Register use of features in admin
admin.site.register(Feature)
