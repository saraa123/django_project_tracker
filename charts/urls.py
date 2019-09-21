from django.conf.urls import url
from charts.views import charts_home, pie_chart, ChartData

urlpatterns = [
    url(r'^charts$', charts_home, name="charts"),
    url(r'^api-data/$', pie_chart, name="api-data"),
    url(r'^api-chart-data/$', ChartData.as_view()),
    
]
