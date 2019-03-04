from django.conf.urls import url, include
from . import views

urlpatterns = [
    url('application', views.viewApplication, name="viewApplication"),
    url('', views.dashboard, name="dashboard"),
]
