from django.urls import path
from . import views

# app_name = 'canteen'

urlpatterns = [
    path('', views.b_product_list, name='b_product_list'),
    path('product/<int:pk>/', views.b_product_detail, name='b_product_detail'),
]