from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('producers/', views.producers_index, name='producers_index'),
    path('producers/<int:producer_id>', views.producers_details, name='producers_details'),
    path('producers/<int:producer_id>/add_wine/', views.add_wine, name='add_wine'),
    path('producers/<int:producer_id>/assoc_distributor/<int:distributor_id>/', views.assoc_distributor, name='assoc_distributor')
]