from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('add/', views.add_product, name='add_product'),
    path('product/<int:pk>/', views.product_details, name='product_details'),
    path('category/<slug:category_slug>/', views.product_list, name='product_list_by_category'),
]