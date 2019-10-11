from django.conf.urls import url
from charts.views import charts_home, ChartData

urlpatterns = [
    url(r'^charts$', charts_home, name="charts"),
    url(r'^api-chart-data/$', ChartData.as_view()),
    
]
