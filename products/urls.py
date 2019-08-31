from django.conf.urls import url, include
from .views import all_products

urlpatterns = [
    # Shows us the all_products view
    url(r'^$', all_products, name='products')
]