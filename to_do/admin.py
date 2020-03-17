from django.contrib import admin
from .models import Item, Feature, Feedback

class ItemModelAdmin(admin.ModelAdmin):
    list_display = ["__str__", "done", "date_created"]
    list_filter = ["done", "date_created"]
    class Meta:
        model = Item


# Register use of issues in admin
admin.site.register(Item, ItemModelAdmin)

# Register use of features in admin
admin.site.register(Feature)

# Register use of feedback in admin
admin.site.register(Feedback)
