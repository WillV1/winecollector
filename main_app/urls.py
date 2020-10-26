from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('wines/', views.wines_index, name='wines_index'),
    # path('wine_about', views.wines_about, name='wines_about')
]