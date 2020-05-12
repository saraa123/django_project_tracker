
from django.conf.urls import url, include
from django.contrib import admin

# urls for to_do app
from to_do.views import todo_list, closed_issues_and_features, new_item, add_feedback, toggle_status

# urls for accounts app
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
from checkout.views import upvote_checkout

# urls for charts app
from charts import urls as charts_urls

# imports for media
from django.views import static
from .settings import MEDIA_ROOT

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', todo_list, name='home'), # home refers to to_do view from to_do app
    url(r'^add$', new_item, name='new_issue'),
    url(r'^closed_issues_and_features$',
        closed_issues_and_features, name='closed_issues_and_features'),
    url(r'^add_feedback$', add_feedback, name='add_feedback'),
    url(r'^toggle/(?P<id>\d+)$', toggle_status),
    url(r'^accounts/', include(accounts_urls)),
    url(r'^products/', include(products_urls)),
    url(r'^cart/', include(cart_urls)),
    url(r'^search/', include(search_urls)),
    url(r'^checkout/', include(checkout_urls)),
    url(r'^charts/', include(charts_urls)),
    url(r'^upvote_checkout/(?P<id>\d+)$',
        upvote_checkout, name='upvote_checkout'),
    url(r'^media/(?P<path>.*)$', static.serve, {'document_root': MEDIA_ROOT})
]
