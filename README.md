# Floravia - Website Katalog Tanaman Hias

![Floravia Banner](https://source.unsplash.com/random/1200x400/?plants)

## Deskripsi Proyek

Floravia adalah website katalog tanaman hias sederhana yang dibuat menggunakan Django. Website ini menampilkan berbagai jenis tanaman hias indoor dan outdoor, lengkap dengan deskripsi dan informasi perawatannya. Proyek ini dikembangkan sebagai mini proyek untuk pembelajaran Django.

## Fitur

- **Homepage** - Menampilkan halaman utama dengan informasi tentang Floravia
- **Katalog Produk** - Halaman daftar produk tanaman hias yang tersedia
- **Detail Produk** - Informasi lengkap mengenai tanaman hias tertentu
- **Halaman Kontak** - Informasi kontak dan form untuk menghubungi Floravia

## Demo

![Screenshot Home](https://source.unsplash.com/random/800x450/?plants,homepage)

## Persyaratan Sistem

- Python 3.8 atau lebih baru
- Django 4.0 atau lebih baru

## Instalasi

Berikut langkah-langkah untuk menginstal dan menjalankan proyek Floravia di komputer lokal Anda:

1. **Clone repositori ini**

```bash
git clone https://github.com/username/floravia.git
cd floravia
```

2. **Buat virtual environment**

```bash
python -m venv venv
```

3. **Aktifkan virtual environment**

- Di Windows:
```bash
venv\Scripts\activate
```

- Di Linux/Mac:
```bash
source venv/bin/activate
```

4. **Instal dependensi**

```bash
pip install django
```

5. **Jalankan server pengembangan**

```bash
python manage.py runserver
```

6. **Buka browser dan akses website**

```
http://127.0.0.1:8000/
```

## Struktur Proyek

```
floravia/
├── floravia/           # Direktori proyek utama
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py     # Pengaturan proyek
│   ├── urls.py         # URL utama
│   └── wsgi.py
├── produk/             # Aplikasi produk
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   ├── models.py
│   ├── tests.py
│   ├── urls.py         # URL aplikasi
│   └── views.py        # Function-based views
├── manage.py           # Script manajemen Django
└── venv/               # Virtual environment (tidak dicommit ke git)
```

## Routes (URLs)

| URL                     | Fungsi             | Deskripsi                          |
|-------------------------|--------------------|------------------------------------|
| `/`                     | `homepage`         | Halaman utama website              |
| `/produk/`              | `produk_list`      | Menampilkan daftar semua produk    |
| `/produk/<int:produk_id>/` | `produk_detail` | Menampilkan detail produk tertentu |
| `/kontak/`              | `kontak`           | Halaman informasi kontak           |

## Pengembangan Selanjutnya

Beberapa fitur yang bisa ditambahkan untuk pengembangan selanjutnya:
- Menggunakan database untuk menyimpan data produk
- Implementasi sistem template Django
- Menambahkan sistem autentikasi pengguna
- Fitur keranjang belanja dan checkout
- Panel admin untuk mengelola produk

## Kontribusi

Kontribusi dan saran sangat diterima. Silakan buat issue atau pull request untuk perbaikan atau penambahan fitur.

## Lisensi

[MIT License](LICENSE)

## Kontak

Untuk pertanyaan atau informasi lebih lanjut, silakan hubungi:
- Email: info@floravia.id
- Website: [floravia.id](https://floravia.id)