# produk/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import Produk
from .forms import ProdukForm

def homepage(request):
    # Get featured products for homepage
    featured_products = Produk.objects.all()[:6]
    context = {
        'featured_products': featured_products
    }
    return render(request, 'produk/homepage.html', context)

def produk_list(request):
    # Get all products grouped by category
    indoor_products = Produk.objects.filter(kategori='indoor')
    outdoor_products = Produk.objects.filter(kategori='outdoor')
    kaktus_products = Produk.objects.filter(kategori='kaktus')
    
    context = {
        'indoor_products': indoor_products,
        'outdoor_products': outdoor_products,
        'kaktus_products': kaktus_products,
    }
    return render(request, 'produk/produk_list.html', context)

def produk_detail(request, produk_id):
    produk = get_object_or_404(Produk, pk=produk_id)
    # Get related products from same category
    related_products = Produk.objects.filter(kategori=produk.kategori).exclude(pk=produk_id)[:3]
    
    context = {
        'produk': produk,
        'related_products': related_products,
    }
    return render(request, 'produk/produk_detail.html', context)

def produk_create(request):
    if request.method == 'POST':
        form = ProdukForm(request.POST)
        if form.is_valid():
            produk = form.save()
            messages.success(request, f'Produk "{produk.nama}" berhasil ditambahkan!')
            return redirect('produk_detail', produk_id=produk.pk)
    else:
        form = ProdukForm()
    
    context = {
        'form': form,
        'title': 'Tambah Produk Baru'
    }
    return render(request, 'produk/produk_form.html', context)

def produk_update(request, produk_id):
    produk = get_object_or_404(Produk, pk=produk_id)
    
    if request.method == 'POST':
        form = ProdukForm(request.POST, instance=produk)
        if form.is_valid():
            produk = form.save()
            messages.success(request, f'Produk "{produk.nama}" berhasil diupdate!')
            return redirect('produk_detail', produk_id=produk.pk)
    else:
        form = ProdukForm(instance=produk)
    
    context = {
        'form': form,
        'produk': produk,
        'title': f'Edit Produk: {produk.nama}'
    }
    return render(request, 'produk/produk_form.html', context)

def produk_delete(request, produk_id):
    produk = get_object_or_404(Produk, pk=produk_id)
    
    if request.method == 'POST':
        nama_produk = produk.nama
        produk.delete()
        messages.success(request, f'Produk "{nama_produk}" berhasil dihapus!')
        return redirect('produk_list')
    
    context = {
        'produk': produk,
    }
    return render(request, 'produk/produk_delete.html', context)

def kontak(request):
    if request.method == 'POST':
        # Handle contact form submission
        nama = request.POST.get('nama')
        email = request.POST.get('email')
        subjek = request.POST.get('subjek')
        pesan = request.POST.get('pesan')
        
        # Here you would typically send email or save to database
        # For now, just show success message
        messages.success(request, f'Terima kasih {nama}! Pesan Anda telah dikirim.')
        return redirect('kontak')
    
    return render(request, 'produk/kontak.html')