from django.conf.urls import url 
from .views import search_product, search_issues_and_features

urlpatterns = [
    url(r'^$', search_product, name='search'),
    url(r'^search_issues_features$', search_issues_and_features, name='search_issues_and_features')
]