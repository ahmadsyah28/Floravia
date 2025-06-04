# produk/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Public URLs
    path('', views.homepage, name='homepage'),
    path('produk/', views.produk_list, name='produk_list'),
    path('produk/<int:produk_id>/', views.produk_detail, name='produk_detail'),
    path('kontak/', views.kontak, name='kontak'),
    
    # Authentication URLs
    path('login/', views.user_login, name='login'),
    path('register/', views.user_register, name='register'),
    path('logout/', views.user_logout, name='logout'),
    
    # Admin-only URLs (Product Management)
    path('produk/tambah/', views.produk_create, name='produk_create'),
    path('produk/<int:produk_id>/edit/', views.produk_update, name='produk_update'),
    path('produk/<int:produk_id>/hapus/', views.produk_delete, name='produk_delete'),
    
    # Cart URLs (User-only)
    path('cart/', views.cart_detail, name='cart_detail'),
    path('cart/add/<int:produk_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/update/<int:item_id>/', views.update_cart_item, name='update_cart_item'),
    path('cart/remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/clear/', views.clear_cart, name='clear_cart'),
]