from django.conf.urls import url
from .views import checkout, upvote_checkout, invoice

urlpatterns = [
    url(r'^$', checkout, name='checkout'),
    url(r'^checkout/upvote_checkout/(?P<id>\d+)$', upvote_checkout, name='upvote_checkout'),
    url(r'^invoice$', invoice, name='invoice')
]
