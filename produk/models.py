# produk/models.py
from django.db import models

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
    gambar_url = models.URLField(blank=True, null=True, verbose_name="URL Gambar", 
                                help_text="Link gambar dari Unsplash atau sumber lain")
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
    
    def get_default_image(self):
        """Return default image URL based on product name"""
        if self.gambar_url:
            return self.gambar_url
        # Generate image URL based on product name
        search_term = self.nama.lower().replace(' ', '+')
        return f"https://source.unsplash.com/random/400x300/?{search_term}"