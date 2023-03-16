from django.urls import path 
from . import views

urlpatterns = [

    path('items/', views.getItems, name='Items'),
    path('items/<str:pk>/', views.getItem, name='Item'),
    path('items/update', views.update, name='update'),

]