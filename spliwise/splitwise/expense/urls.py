from django.contrib import admin
from django.conf.urls import include,url
from . import views

urlpatterns = [
    url('register/', views.register, name="register"),
    url('login/', views.login, name="login" ),
    #url('', views.login, name="login" ),
    url('dashboard/', views.dashboard, name="dashboard" ),
    url('expense/', views.expense, name="expenses" ),
    url('split/', views.split, name="split" ),
    url('buddys/', views.buddy, name="buddy" ),
    url('logout/', views.logout, name="logout" ),
]
