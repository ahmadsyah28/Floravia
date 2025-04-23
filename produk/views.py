from django.http import HttpResponse

def homepage(request):
    html_content = """
    <html>
        <head><title>Floravia - Homepage</title></head>
        <body>
            <h1>Selamat Datang di Floravia</h1>
            <p>Toko tanaman hias terlengkap untuk mempercantik rumah Anda</p>
            <ul>
                <li><a href="/">Home</a></li>
                <li><a href="/produk/">Daftar Produk</a></li>
                <li><a href="/kontak/">Kontak</a></li>
            </ul>
            <p>Floravia menyediakan berbagai pilihan tanaman hias berkualitas untuk mempercantik ruangan dan taman Anda.</p>
            <p>Jelajahi koleksi tanaman hias kami yang lengkap, mulai dari tanaman indoor, outdoor, hingga kaktus dan sukulen!</p>
        </body>
    </html>
    """
    return HttpResponse(html_content)

def produk_list(request):
    html_content = """
    <html>
        <head><title>Floravia - Daftar Produk</title></head>
        <body>
            <h1>Daftar Produk Tanaman Hias</h1>
            <ul>
                <li><a href="/">Home</a></li>
                <li><a href="/produk/">Daftar Produk</a></li>
                <li><a href="/kontak/">Kontak</a></li>
            </ul>
            <h2>Tanaman Indoor</h2>
            <ul>
                <li><a href="/produk/1/">Monstera Deliciosa</a></li>
                <li><a href="/produk/2/">Fiddle Leaf Fig</a></li>
                <li><a href="/produk/3/">Snake Plant</a></li>
            </ul>
            <h2>Tanaman Outdoor</h2>
            <ul>
                <li><a href="/produk/4/">Aglaonema</a></li>
                <li><a href="/produk/5/">Anthurium</a></li>
            </ul>
        </body>
    </html>
    """
    return HttpResponse(html_content)

def produk_detail(request, produk_id):
    # Dictionary berisi detail produk berdasarkan ID
    produk_details = {
        1: {
            'nama': 'Monstera Deliciosa',
            'harga': 'Rp 250.000',
            'deskripsi': 'Tanaman hias indoor populer dengan daun besar berlubang yang cantik.'
        },
        2: {
            'nama': 'Fiddle Leaf Fig',
            'harga': 'Rp 350.000',
            'deskripsi': 'Tanaman indoor dengan daun berbentuk biola yang elegan.'
        },
        3: {
            'nama': 'Snake Plant',
            'harga': 'Rp 150.000',
            'deskripsi': 'Tanaman hias yang mudah perawatannya dan bisa menyerap polutan.'
        },
        4: {
            'nama': 'Aglaonema',
            'harga': 'Rp 200.000',
            'deskripsi': 'Tanaman hias dengan daun berwarna-warni yang indah.'
        },
        5: {
            'nama': 'Anthurium',
            'harga': 'Rp 275.000',
            'deskripsi': 'Tanaman dengan bunga berbentuk hati yang menarik.'
        }
    }
    
    if produk_id in produk_details:
        produk = produk_details[produk_id]
        html_content = f"""
        <html>
            <head><title>Floravia - {produk['nama']}</title></head>
            <body>
                <h1>Detail Produk: {produk['nama']}</h1>
                <ul>
                    <li><a href="/">Home</a></li>
                    <li><a href="/produk/">Daftar Produk</a></li>
                    <li><a href="/kontak/">Kontak</a></li>
                </ul>
                <div>
                    <h2>{produk['nama']}</h2>
                    <p><strong>Harga:</strong> {produk['harga']}</p>
                    <p><strong>Deskripsi:</strong> {produk['deskripsi']}</p>
                </div>
                <p><a href="/produk/">Kembali ke Daftar Produk</a></p>
            </body>
        </html>
        """
    else:
        html_content = """
        <html>
            <head><title>Floravia - Produk Tidak Ditemukan</title></head>
            <body>
                <h1>Produk Tidak Ditemukan</h1>
                <ul>
                    <li><a href="/">Home</a></li>
                    <li><a href="/produk/">Daftar Produk</a></li>
                    <li><a href="/kontak/">Kontak</a></li>
                </ul>
                <p>Maaf, produk yang Anda cari tidak ditemukan.</p>
                <p><a href="/produk/">Kembali ke Daftar Produk</a></p>
            </body>
        </html>
        """
    
    return HttpResponse(html_content)

def kontak(request):
    html_content = """
    <html>
        <head><title>Floravia - Kontak</title></head>
        <body>
            <h1>Kontak Floravia</h1>
            <ul>
                <li><a href="/">Home</a></li>
                <li><a href="/produk/">Daftar Produk</a></li>
                <li><a href="/kontak/">Kontak</a></li>
            </ul>
            <h2>Informasi Kontak</h2>
            <p><strong>Alamat:</strong> Jl. Tanaman Hias No. 123, Jakarta</p>
            <p><strong>Telepon:</strong> (021) 1234-5678</p>
            <p><strong>Email:</strong> info@floravia.id</p>
            <h2>Jam Operasional</h2>
            <p>Senin - Jumat: 08.00 - 17.00</p>
            <p>Sabtu - Minggu: 09.00 - 15.00</p>
        </body>
    </html>
    """
    return HttpResponse(html_content)