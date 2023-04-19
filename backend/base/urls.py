from django.urls import path 
from . import views

urlpatterns = [

    path('risk_index/items/', views.get_risk_index_items, name='items_RIM'),
    path('risk_index/items/<str:pk>/', views.get_risk_index_item, name='item_RIM'),
    path('country_risk_premium/items/', views.get_country_risk_premium_items, name='items_CRPM'),
    path('country_risk_premium/items/<str:pk>/', views.get_country_risk_premium_item, name='item_CRPM'),
    path('risk_index/items/update', views.update_rim, name='update_RIM'),
    path('country_risk_premium/items/update', views.update_crpm, name='update_CRPM'),

]