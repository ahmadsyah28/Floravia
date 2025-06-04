# produk/admin.py
from django.contrib import admin
from .models import Produk, Cart, CartItem

@admin.register(Produk)
class ProdukAdmin(admin.ModelAdmin):
    list_display = ('nama', 'kategori', 'harga', 'stok', 'created_at')
    list_filter = ('kategori', 'created_at')
    search_fields = ('nama', 'deskripsi')
    list_editable = ('stok',)
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Informasi Produk', {
            'fields': ('nama', 'kategori', 'harga', 'stok')
        }),
        ('Deskripsi & Perawatan', {
            'fields': ('deskripsi', 'perawatan')
        }),
        ('Gambar', {
            'fields': ('gambar', 'gambar_url')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 0
    readonly_fields = ('added_at',)

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_total_items', 'get_formatted_total_price', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('user__username', 'user__email')
    readonly_fields = ('created_at', 'updated_at', 'get_total_items', 'get_formatted_total_price')
    inlines = [CartItemInline]
    
    def get_total_items(self, obj):
        return obj.get_total_items()
    get_total_items.short_description = 'Total Items'
    
    def get_formatted_total_price(self, obj):
        return obj.get_formatted_total_price()
    get_formatted_total_price.short_description = 'Total Price'

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'produk', 'quantity', 'get_formatted_total_price', 'added_at')
    list_filter = ('added_at', 'produk__kategori')
    search_fields = ('cart__user__username', 'produk__nama')
    readonly_fields = ('added_at', 'get_formatted_total_price')
    
    def get_formatted_total_price(self, obj):
        return obj.get_formatted_total_price()
    get_formatted_total_price.short_description = 'Total Price'