from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [

    #--STATIC
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),

    #-----AUTHENTICATION
    path('accounts/signup', views.signup, name='signup'),

    #---PRODUCERS
    path('producers/', views.producers_index, name='producers_index'),
    path('producers/<int:producer_id>', views.producers_details, name='producers_details'),
    path('producer/new/', views.add_producer, name='add_producer'),
    path('producers/<int:producer_id>/delete/', views.delete_producer, name='delete_producer'),
    path('producers/<int:producer_id>/edit/', views.edit_producer, name='edit_producer'),

    #---WINE
    path('producers/<int:producer_id>/add_wine/', views.add_wine, name='add_wine'),

    #----DISTRIBUTORS
    path('producers/<int:producer_id>/assoc_distributor/<int:distributor_id>/', views.assoc_distributor, name='assoc_distributor'),
    path('producers/<int:producer_id>/remove_distributor/<int:distributor_id>/', views.remove_distributor, name='remove_distributor')
]