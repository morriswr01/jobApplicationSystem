from django.conf.urls import url, include

from . import views

urlpatterns = [
    url('signup/', views.signUp, name='signup'),
    url('login/', views.loginUser, name='login'),
    url('logout/', views.logoutUser, name='logout'),
    url('submitApp/', views.submitApp, name='submitApp'),
    url('changePassword/', views.changePassword, name='changePassword')
]
