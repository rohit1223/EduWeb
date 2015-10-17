from django.conf.urls import url, include
from django.contrib import admin
from portal import views

urlpatterns = [
    url(r'verify/$', views.verify, name='verify'),
    url(r'dashboard/', views.dashboard, name='dashboard'),
    url(r'signin/', views.signin, name='signin'),
    url(r'registeruser/', views.registeruser, name='registeruser'),
    url(r'signup/', views.signup, name='signup'),
    url(r'postquestion/', views.postquestion, name='postquestion'),
    url(r'verifyAnswer/', views.verifyAnswer, name='verifyAnswer'),
    url(r'user_logout/$', views.user_logout, name='user_logout'),
    url(r'$', views.index, name='index'),
]
