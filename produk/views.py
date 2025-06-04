# produk/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Produk, Cart, CartItem
from .forms import ProdukForm

# Helper function to check if user is admin
def is_admin(user):
    return user.is_superuser or user.is_staff

# Public Views (accessible to everyone)
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

# ✅ ADMIN ONLY VIEWS (Product Management)
@user_passes_test(is_admin, login_url='login')
def produk_create(request):
    if request.method == 'POST':
        form = ProdukForm(request.POST, request.FILES)
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

@user_passes_test(is_admin, login_url='login')
def produk_update(request, produk_id):
    produk = get_object_or_404(Produk, pk=produk_id)
    
    if request.method == 'POST':
        form = ProdukForm(request.POST, request.FILES, instance=produk)
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

@user_passes_test(is_admin, login_url='login')
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

# ✅ AUTHENTICATION VIEWS
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Selamat datang, {username}!')
                # Redirect to next page or homepage
                next_page = request.GET.get('next', 'homepage')
                return redirect(next_page)
        else:
            messages.error(request, 'Username atau password salah.')
    else:
        form = AuthenticationForm()
    
    return render(request, 'registration/login.html', {'form': form})

def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Akun {username} berhasil dibuat!')
            login(request, user)
            return redirect('homepage')
    else:
        form = UserCreationForm()
    
    return render(request, 'registration/register.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    messages.success(request, 'Anda telah logout.')
    return redirect('homepage')

# ✅ CART VIEWS (For logged-in users)
@login_required
def add_to_cart(request, produk_id):
    produk = get_object_or_404(Produk, pk=produk_id)
    
    # Check stock
    if produk.stok <= 0:
        messages.error(request, f'Maaf, {produk.nama} sedang habis stok.')
        return redirect('produk_detail', produk_id=produk_id)
    
    # Get or create cart for user
    cart, created = Cart.objects.get_or_create(user=request.user)
    
    # Get or create cart item
    cart_item, created = CartItem.objects.get_or_create(
        cart=cart, 
        produk=produk,
        defaults={'quantity': 1}
    )
    
    if not created:
        # Item already exists, increase quantity
        if cart_item.quantity < produk.stok:
            cart_item.quantity += 1
            cart_item.save()
            messages.success(request, f'{produk.nama} ditambahkan ke keranjang!')
        else:
            messages.error(request, f'Tidak bisa menambah lagi. Stok {produk.nama} hanya {produk.stok}.')
    else:
        messages.success(request, f'{produk.nama} ditambahkan ke keranjang!')
    
    return redirect('produk_detail', produk_id=produk_id)

@login_required
def cart_detail(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart).select_related('produk')
    
    context = {
        'cart': cart,
        'cart_items': cart_items,
    }
    return render(request, 'produk/cart_detail.html', context)

@login_required
def update_cart_item(request, item_id):
    cart_item = get_object_or_404(CartItem, pk=item_id, cart__user=request.user)
    
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        
        if quantity <= 0:
            cart_item.delete()
            messages.success(request, f'{cart_item.produk.nama} dihapus dari keranjang.')
        elif quantity <= cart_item.produk.stok:
            cart_item.quantity = quantity
            cart_item.save()
            messages.success(request, f'Jumlah {cart_item.produk.nama} diupdate.')
        else:
            messages.error(request, f'Stok {cart_item.produk.nama} hanya {cart_item.produk.stok}.')
    
    return redirect('cart_detail')

@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, pk=item_id, cart__user=request.user)
    produk_nama = cart_item.produk.nama
    cart_item.delete()
    messages.success(request, f'{produk_nama} dihapus dari keranjang.')
    return redirect('cart_detail')

@login_required
def clear_cart(request):
    cart = get_object_or_404(Cart, user=request.user)
    cart.cartitem_set.all().delete()
    messages.success(request, 'Keranjang berhasil dikosongkan.')
    return redirect('cart_detail')

# Contact page
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