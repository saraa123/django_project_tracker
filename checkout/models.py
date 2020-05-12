from django.db import models
from products.models import Product
from django.contrib.auth import get_user_model

User = get_user_model()

class Order(models.Model):
    full_name = models.CharField(max_length=50, blank=False)
    street_address1 = models.CharField(max_length=50, blank=False)
    country = models.CharField(max_length=40, blank=False)
    postcode = models.CharField(max_length=20, blank=True)
    phone_number = models.CharField(max_length=20, blank=False)
    date = models.DateField()

    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='orders', default=1)

    # Summary of the order
    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.date, self.full_name)

class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False)
    product = models.ForeignKey(Product, null=False)
    quantity = models.IntegerField(blank=False)

    def __str__(self):
        return "{0}-{1}-{2}".format(self.quantity, self.product.name, self.product.price)
