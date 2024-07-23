
from django import views
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    #path('admin/', admin.site.urls), #this is not needed in homeapp
    path("", views.home, name="home"),
]
