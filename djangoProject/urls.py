"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

# urls for to_do app
from to_do.views import todo_list, new_item, toggle_status

# urls for accounts app
# from accounts.views import index, logout, login, profile
from accounts.views import index 
from accounts import urls as accounts_urls

# urls for products app
from products import urls as products_urls
from products.views import all_products

# urls for cart app
from cart import urls as cart_urls

# urls for search app
from search import urls as search_urls

# urls for checkout app
from checkout import urls as checkout_urls

# urls for charts app
from charts import urls as charts_urls

# imports for media
from django.views import static
from .settings import MEDIA_ROOT

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', todo_list, name='home'), # home refers to to_do view from to_do app
    url(r'^add$', new_item),
    url(r'^toggle/(?P<id>\d+)$', toggle_status),
    url(r'^accounts/', include(accounts_urls)),
    url(r'^products/', include(products_urls)),
    url(r'^cart/', include(cart_urls)),
    url(r'^search/', include(search_urls)),
    url(r'^checkout/', include(checkout_urls)),
    url(r'^charts/', include(charts_urls)),
    url(r'^media/(?P<path>.*)$', static.serve, {'document_root': MEDIA_ROOT})
]
