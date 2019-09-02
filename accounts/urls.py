from django.conf.urls import url, include
from accounts.views import index, logout, login, profile
from accounts import url_reset

urlpatterns = [
    url(r'^register/$', index, name='register'),
    url(r'^account/logout/$', logout, name='logout'),
    url(r'^account/login/$', login, name='login'),
    url(r'^account/profile/$', profile, name='profile'),
    url(r'^password-reset/', include(url_reset)),
]
