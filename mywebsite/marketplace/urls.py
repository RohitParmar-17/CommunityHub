from django.urls import path
from . import views


urlpatterns = [
    path('', views.product_list_view, name='product_list'),
    path('product/<int:pk>/', views.product_detail_view, name='product_detail'),
    path('product/<int:product_id>/add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('update-cart/<int:product_id>/', views.update_cart, name='update_cart'),
    path('cart/', views.view_cart, name='view_cart'),
]

