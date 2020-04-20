from django.contrib import admin
from .models import Order, OrderLineItem

# Register your models here.
class OrderLineAdminInline(admin.TabularInline):
    model = OrderLineItem

class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineAdminInline, )
    list_display = ["__str__", "user", "date"]

admin.site.register(Order, OrderAdmin)