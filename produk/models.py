# produk/models.py
from django.db import models
from django.contrib.auth.models import User
import os

def produk_image_path(instance, filename):
    """Generate path for uploaded product images"""
    # Get file extension
    ext = filename.split('.')[-1]
    # Generate filename: produk_<id>_<nama>.<ext>
    filename = f"produk_{instance.nama.replace(' ', '_').lower()}.{ext}"
    return os.path.join('produk_images', filename)

class Produk(models.Model):
    KATEGORI_CHOICES = [
        ('indoor', 'Tanaman Indoor'),
        ('outdoor', 'Tanaman Outdoor'),
        ('kaktus', 'Kaktus & Sukulen'),
    ]
    
    nama = models.CharField(max_length=200, verbose_name="Nama Produk")
    deskripsi = models.TextField(verbose_name="Deskripsi")
    harga = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Harga")
    kategori = models.CharField(max_length=20, choices=KATEGORI_CHOICES, verbose_name="Kategori")
    perawatan = models.TextField(verbose_name="Cara Perawatan")
    stok = models.PositiveIntegerField(default=0, verbose_name="Stok")
    
    # Image fields
    gambar = models.ImageField(
        upload_to=produk_image_path, 
        blank=True, 
        null=True, 
        verbose_name="Upload Gambar",
        help_text="Upload gambar produk (opsional)"
    )
    
    gambar_url = models.URLField(
        blank=True, 
        null=True, 
        verbose_name="URL Gambar", 
        help_text="Link gambar dari Unsplash atau sumber lain (opsional)"
    )
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Dibuat pada")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Diupdate pada")
    
    class Meta:
        verbose_name = "Produk"
        verbose_name_plural = "Produk"
        ordering = ['-created_at']
    
    def __str__(self):
        return self.nama
    
    def get_formatted_harga(self):
        """Return formatted price in Rupiah"""
        return f"Rp {self.harga:,.0f}".replace(',', '.')
    
    def get_image_url(self):
        """Return image URL - prioritize uploaded image over URL"""
        if self.gambar:
            return self.gambar.url
        elif self.gambar_url:
            return self.gambar_url
        else:
            # Generate default image URL based on product name
            search_term = self.nama.lower().replace(' ', '+')
            return f"https://source.unsplash.com/400x300/?{search_term}"
    
    def get_default_image(self):
        """Alias for get_image_url for backward compatibility"""
        return self.get_image_url()

# ✅ NEW: Cart System
class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="User")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Dibuat pada")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Diupdate pada")
    
    class Meta:
        verbose_name = "Keranjang"
        verbose_name_plural = "Keranjang"
    
    def __str__(self):
        return f"Keranjang {self.user.username}"
    
    def get_total_items(self):
        """Get total quantity of items in cart"""
        return sum(item.quantity for item in self.cartitem_set.all())
    
    def get_total_price(self):
        """Get total price of all items in cart"""
        return sum(item.get_total_price() for item in self.cartitem_set.all())
    
    def get_formatted_total_price(self):
        """Get formatted total price in Rupiah"""
        total = self.get_total_price()
        return f"Rp {total:,.0f}".replace(',', '.')

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, verbose_name="Keranjang")
    produk = models.ForeignKey(Produk, on_delete=models.CASCADE, verbose_name="Produk")
    quantity = models.PositiveIntegerField(default=1, verbose_name="Jumlah")
    added_at = models.DateTimeField(auto_now_add=True, verbose_name="Ditambahkan pada")
    
    class Meta:
        verbose_name = "Item Keranjang"
        verbose_name_plural = "Item Keranjang"
        unique_together = ('cart', 'produk')  # Prevent duplicate items
    
    def __str__(self):
        return f"{self.quantity}x {self.produk.nama}"
    
    def get_total_price(self):
        """Get total price for this cart item"""
        return self.quantity * self.produk.harga
    
    def get_formatted_total_price(self):
        """Get formatted total price in Rupiah"""
        total = self.get_total_price()
        return f"Rp {total:,.0f}".replace(',', '.')