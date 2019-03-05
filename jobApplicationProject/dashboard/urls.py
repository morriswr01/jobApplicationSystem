from django.conf.urls import url, include
from . import views

urlpatterns = [
    url('application/', views.viewApplication, name="viewApplication"),
    url('positions/addNewPosition',views.addNewPosition,name="addNewPosition"),
    url('positions/deletePosition',views.deletePosition,name="deletePosition"),
    url('feedback/rejectWithFeedback',views.rejectWithFeedback,name="rejectWithFeedback"),
    url('feedback/hire',views.hireApplicant ,name="hire"),
    url('positions/', views.adminPositions, name="adminPositions"),
    url('feedback/', views.adminFeedback, name="adminFeedback"),
    url('adminAction/', views.adminAction, name= "adminAction"),
    url('', views.dashboard, name="dashboard"),
]
