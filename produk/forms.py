# produk/forms.py
from django import forms
from .models import Produk

class ProdukForm(forms.ModelForm):
    class Meta:
        model = Produk
        fields = ['nama', 'kategori', 'harga', 'stok', 'deskripsi', 'perawatan', 'gambar_url']
        widgets = {
            'nama': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Masukkan nama produk'
            }),
            'kategori': forms.Select(attrs={
                'class': 'form-control'
            }),
            'harga': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Masukkan harga dalam Rupiah',
                'step': '0.01'
            }),
            'stok': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Masukkan jumlah stok'
            }),
            'deskripsi': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Deskripsi singkat tentang produk'
            }),
            'perawatan': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Cara merawat tanaman ini'
            }),
            'gambar_url': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://example.com/gambar.jpg (opsional)'
            })
        }
    
    def clean_harga(self):
        harga = self.cleaned_data.get('harga')
        if harga and harga <= 0:
            raise forms.ValidationError('Harga harus lebih dari 0')
        return harga
    
    def clean_stok(self):
        stok = self.cleaned_data.get('stok')
        if stok is not None and stok < 0:
            raise forms.ValidationError('Stok tidak boleh negatif')
        return stok