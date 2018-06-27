"""seedboxtest URL Configuration

The `urlpatterns` list routes URLs to views. 
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include('serverInvent.urls')),
    path('admin/', admin.site.urls),
]
