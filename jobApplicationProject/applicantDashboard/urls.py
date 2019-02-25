from django.conf.urls import url
from . import views

urlpatterns = [
    url('dashboard', views.index, name='applicantDashboard-index'),
    url('reviewApplication', views.reviewApplication, name='reviewApplication-index'),
]