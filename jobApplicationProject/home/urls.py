from django.conf.urls import url
from . import views

urlpatterns = [
    url('careers/', views.careers, name='careers-index'),
    url('', views.home, name='home-index'),
]
