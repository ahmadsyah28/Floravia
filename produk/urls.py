# produk/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('produk/', views.produk_list, name='produk_list'),
    path('produk/<int:produk_id>/', views.produk_detail, name='produk_detail'),
    path('produk/tambah/', views.produk_create, name='produk_create'),
    path('produk/<int:produk_id>/edit/', views.produk_update, name='produk_update'),
    path('produk/<int:produk_id>/hapus/', views.produk_delete, name='produk_delete'),
    path('kontak/', views.kontak, name='kontak'),
]