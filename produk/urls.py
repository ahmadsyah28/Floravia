from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('produk/', views.produk_list, name='produk_list'),
    path('produk/<int:produk_id>/', views.produk_detail, name='produk_detail'),
    path('kontak/', views.kontak, name='kontak'),
]