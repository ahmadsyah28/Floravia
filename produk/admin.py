# produk/admin.py
from django.contrib import admin
from .models import Produk

@admin.register(Produk)
class ProdukAdmin(admin.ModelAdmin):
    list_display = ['nama', 'kategori', 'get_formatted_harga', 'stok', 'created_at']
    list_filter = ['kategori', 'created_at']
    search_fields = ['nama', 'deskripsi']
    list_editable = ['stok']
    list_per_page = 20
    
    fieldsets = (
        ('Informasi Dasar', {
            'fields': ('nama', 'kategori', 'harga', 'stok')
        }),
        ('Detail Produk', {
            'fields': ('deskripsi', 'perawatan', 'gambar_url')
        }),
        ('Tanggal', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        })
    )
    
    readonly_fields = ['created_at', 'updated_at']
    
    def get_formatted_harga(self, obj):
        return obj.get_formatted_harga()
    get_formatted_harga.short_description = 'Harga'