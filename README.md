# 🌱 Floravia - Setup Guide untuk CRUD Produk

## 👥 Anggota Tim
- **Muhammad Bintang Indra Hidayat** - NPM: 2208107010023
- **Ahmad Syah Ramadhan** - NPM: 2208107010033
- **Indriani Miza Alfiyanti** - NPM: 2208107010026

# 📽️ Presentasi dan Dokumentasi

Berikut ini adalah link video dan file presentasi dari proyek online shop tanaman hias.

## 🎥 Link Video Presentasi
[Tonton Video](https://youtu.be/rDWdCjN1PAM)

## 📊 Link PPT Presentasi
[Liat PPT](https://drive.google.com/drive/folders/1HwVH97N1aBW4GDWmuAfV4KSc8BC_0DQI?usp=sharing)

## Langkah 1: Persiapan File Structure

Pastikan struktur direktori template seperti ini:
```
floravia/
├── floravia/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── produk/
│   ├── __init__.py
│   ├── admin.py          # ✅ Update
│   ├── apps.py
│   ├── models.py         # ✅ Update
│   ├── forms.py          # ✅ Buat baru
│   ├── views.py          # ✅ Update
│   ├── urls.py           # ✅ Update
│   ├── migrations/
│   └── templates/        # ✅ Buat direktori baru
│       └── produk/       # ✅ Buat direktori baru
│           ├── base.html
│           ├── homepage.html
│           ├── produk_list.html
│           ├── produk_detail.html
│           ├── produk_form.html
│           ├── produk_delete.html
│           └── kontak.html
└── manage.py
```

## Langkah 2: Update Settings

Pastikan di `floravia/settings.py`:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'produk',  # ✅ Pastikan app produk terdaftar
]

# Database (SQLite default)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Template settings
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,  # ✅ Pastikan True untuk template di app
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Internationalization
LANGUAGE_CODE = 'id'  # Bahasa Indonesia
TIME_ZONE = 'Asia/Jakarta'
USE_I18N = True
USE_TZ = True
```

## Langkah 3: URL Configuration

Update `floravia/urls.py`:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('produk.urls')),
]
```

## Langkah 4: Migration dan Setup Database

Jalankan command berikut di terminal:

```bash
# 1. Buat migration untuk model baru
python manage.py makemigrations produk

# 2. Terapkan migration ke database
python manage.py migrate

# 3. Buat superuser untuk akses admin
python manage.py createsuperuser
```

Ikuti instruksi untuk membuat superuser:
- Username: admin (atau sesuai keinginan)
- Email: admin@floravia.id (opsional)
- Password: (pilih password yang aman)

## Langkah 5: Populate Data Sample (Opsional)

Buat file `produk/management/commands/populate_products.py`:

```python
from django.core.management.base import BaseCommand
from produk.models import Produk

class Command(BaseCommand):
    help = 'Populate database with sample products'
    
    def handle(self, *args, **options):
        sample_products = [
            {
                'nama': 'Monstera Deliciosa',
                'kategori': 'indoor',
                'harga': 250000,
                'stok': 15,
                'deskripsi': 'Tanaman hias indoor populer dengan daun besar berlubang yang cantik. Cocok untuk ruang tamu atau workspace.',
                'perawatan': 'Letakkan di tempat dengan cahaya tidak langsung. Siram ketika tanah kering. Bersihkan daun secara berkala.',
                'gambar_url': 'https://source.unsplash.com/random/400x300/?monstera'
            },
            {
                'nama': 'Snake Plant (Sansevieria)',
                'kategori': 'indoor',
                'harga': 150000,
                'stok': 25,
                'deskripsi': 'Tanaman yang mudah perawatannya dan bisa menyerap polutan udara. Ideal untuk pemula.',
                'perawatan': 'Tahan kekeringan. Siram setiap 2-3 minggu sekali. Hindari air berlebihan.',
                'gambar_url': 'https://source.unsplash.com/random/400x300/?snake+plant'
            },
            {
                'nama': 'Aglaonema Red Ruby',
                'kategori': 'outdoor',
                'harga': 200000,
                'stok': 10,
                'deskripsi': 'Tanaman hias dengan daun berwarna merah menarik yang cocok untuk taman.',
                'perawatan': 'Letakkan di tempat dengan cahaya sedang. Siram saat tanah mulai kering.',
                'gambar_url': 'https://source.unsplash.com/random/400x300/?aglaonema+red'
            },
            {
                'nama': 'Kaktus Golden Barrel',
                'kategori': 'kaktus',
                'harga': 125000,
                'stok': 20,
                'deskripsi': 'Kaktus berbentuk bulat dengan duri emas yang cantik. Mudah dirawat dan tahan panas.',
                'perawatan': 'Butuh sinar matahari langsung. Siram sangat jarang, hanya ketika tanah benar-benar kering.',
                'gambar_url': 'https://source.unsplash.com/random/400x300/?golden+barrel+cactus'
            },
            {
                'nama': 'Succulent Mix',
                'kategori': 'kaktus',
                'harga': 75000,
                'stok': 30,
                'deskripsi': 'Campuran berbagai jenis succulent dalam pot kecil. Perfect untuk meja kerja.',
                'perawatan': 'Tempatkan di area terang. Siram sedikit setiap minggu. Hindari genangan air.',
                'gambar_url': 'https://source.unsplash.com/random/400x300/?succulent+mix'
            }
        ]
        
        for product_data in sample_products:
            produk, created = Produk.objects.get_or_create(
                nama=product_data['nama'],
                defaults=product_data
            )
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'Successfully created product: {produk.nama}')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'Product already exists: {produk.nama}')
                )
        
        self.stdout.write(
            self.style.SUCCESS('Finished populating products!')
        )
```

Untuk menggunakan command ini:
```bash
# Buat direktori management
mkdir -p produk/management/commands
touch produk/management/__init__.py
touch produk/management/commands/__init__.py

# Jalankan populate command
python manage.py populate_products
```

## Langkah 6: Testing Website

Jalankan development server:
```bash
python manage.py runserver
```

### Test URLs:
- **Homepage**: http://127.0.0.1:8000/
- **Katalog Produk**: http://127.0.0.1:8000/produk/
- **Tambah Produk**: http://127.0.0.1:8000/produk/tambah/
- **Admin Panel**: http://127.0.0.1:8000/admin/
- **Kontak**: http://127.0.0.1:8000/kontak/

## 🚀 Fitur yang Tersedia:

### ✅ CRUD Operations:
- **Create**: Form tambah produk dengan validasi
- **Read**: List produk dan detail produk
- **Update**: Edit produk existing
- **Delete**: Hapus produk dengan konfirmasi

### ✅ Admin Panel:
- Dashboard admin untuk manage produk
- Filter dan search produk
- Bulk actions untuk update stok

### ✅ User Interface:
- Responsive design
- Success/error messages
- Preview gambar
- Kategori produk terorganisir

### ✅ Database:
- SQLite database
- Model relationships
- Auto-generated images dari Unsplash

## 🛠 Teknologi yang Digunakan:
- **Django** - Python web framework
- **SQLite** - Database default untuk development
- **HTML/CSS** - Frontend templating
- **Bootstrap** - CSS framework untuk responsive design

## 🎯 Tentang Proyek:
Floravia adalah aplikasi web e-commerce yang khusus menjual tanaman hias. Proyek ini dikembangkan menggunakan Django framework dengan fitur lengkap CRUD (Create, Read, Update, Delete) untuk manajemen produk tanaman. Aplikasi ini dilengkapi dengan kategori tanaman (indoor, outdoor, kaktus), informasi perawatan, dan interface yang user-friendly.

## Troubleshooting:

1. **Template not found**: Pastikan struktur direktori template benar
2. **No reverse match**: Cek nama URL di urls.py
3. **Database error**: Jalankan `python manage.py migrate`
4. **Static files**: Untuk production, setup static files dengan `python manage.py collectstatic`

## 📈 Pengembangan Selanjutnya:

- Tambah authentication untuk protect CRUD operations
- Upload gambar ke server instead of URL
- Implementasi shopping cart
- Review dan rating system
- Email notifications untuk order
- Payment gateway integration

## 📞 Kontak:
Jika ada pertanyaan atau masalah dalam setup, silakan hubungi anggota tim pengembang atau buat issue di repository ini.
