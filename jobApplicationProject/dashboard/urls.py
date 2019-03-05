from django.conf.urls import url, include
from . import views

urlpatterns = [
    url('application/', views.viewApplication, name="viewApplication"),
    url('positions/addNewPosition',views.addNewPosition,name="addNewPosition"),
    url('positions/', views.adminPositions, name="adminPositions"),
    url('feedback/', views.adminFeedback, name="adminFeedback"),
    url('adminAction/', views.adminAction, name= "adminAction"),
    url('', views.dashboard, name="dashboard"),
]
