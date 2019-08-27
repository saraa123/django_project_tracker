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
from django.conf.urls import url
from django.contrib import admin
from to_do.views import todo_list, new_item, edit_an_item, toggle_status
from accounts.views import index, logout, login, profile

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', todo_list, name='home'), # home refers to to_do view from to_do app
    url(r'^add$', new_item),
    url(r'^edit/(?P<id>\d+)$', edit_an_item),
    url(r'^toggle/(?P<id>\d+)$', toggle_status),
    url(r'^register/$', index, name='register'),
    url(r'^account/logout/$', logout, name='logout'),
    url(r'^account/login/$', login, name='login'),
    url(r'^account/profile/$', profile, name='profile')
]
