from django.urls import path
from .views import HistoricalDataView, SingleHistoricalDataView, datarequest, home
from django.conf.urls import url


app_name = "Charts"

urlpatterns = [path('HistoricalData/', HistoricalDataView.as_view()),
               path('HistoricalData/<int:pk>', SingleHistoricalDataView.as_view()),
               url(r'^datarequest/$', datarequest, name='datarequest'),
               path('', home, name='home'),
               ]