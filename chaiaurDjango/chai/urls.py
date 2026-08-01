"""
URL configuration for chaiaurDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/

Examples:
Function views
    1. Add an import: from my_app import views
    2. Add a URL to urlpatterns: path('', views.home, name='home')
"""

#from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.all_chai, name='all_chai'),
    path('<int:chai_id>/', views.chai_detail, name='chai_detail'),
    #path('order/', views.order, name='order'),
] 