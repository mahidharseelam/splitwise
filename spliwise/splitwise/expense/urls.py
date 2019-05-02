from django.contrib import admin
from django.conf.urls import include,url
from . import views

urlpatterns = [
    url('register/', views.register, name="register"),
    url('login/', views.login, name="login" ),
]
