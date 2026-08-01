"""
URL configuration for chaiaurDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/

Examples:
Function views
    1. Add an import: from my_app import views
    2. Add a URL to urlpatterns: path('', views.home, name='home')
"""

from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static

#from chaiaurDjango.chaiaurDjango import settings (error de rha tha)

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('chai/', include('chai.urls')),  # Include the URLs from the 'chai' app

    path('__reload__/', include('django_browser_reload.urls')),  # Add the URL pattern for django-browser-reload
] + static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Serve media files during development