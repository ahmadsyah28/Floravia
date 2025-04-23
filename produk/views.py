from django.http import HttpResponse

def homepage(request):
    html_content = """
    <!DOCTYPE html>
    <html>
        <head>
            <title>Floravia - Homepage</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <style>
                body {
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    margin: 0;
                    padding: 0;
                    background-color: #f8f9fa;
                    color: #333;
                    line-height: 1.6;
                }
                header {
                    background-color: #2c6e49;
                    color: white;
                    padding: 1rem 0;
                    text-align: center;
                }
                .container {
                    width: 80%;
                    margin: 0 auto;
                    padding: 2rem 0;
                }
                nav {
                    background-color: #4c956c;
                    padding: 1rem 0;
                }
                nav ul {
                    list-style-type: none;
                    margin: 0;
                    padding: 0;
                    text-align: center;
                }
                nav ul li {
                    display: inline;
                    margin: 0 15px;
                }
                nav ul li a {
                    color: white;
                    text-decoration: none;
                    font-weight: bold;
                    transition: color 0.3s;
                }
                nav ul li a:hover {
                    color: #d8f3dc;
                }
                .hero {
                    background-image: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url('https://source.unsplash.com/random/1200x700/?plants');
                    height: 60vh;
                    background-position: center;
                    background-repeat: no-repeat;
                    background-size: cover;
                    position: relative;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    text-align: center;
                    color: white;
                }
                .hero-content {
                    max-width: 800px;
                    padding: 2rem;
                }
                .hero h1 {
                    font-size: 3rem;
                    margin-bottom: 1rem;
                }
                .hero p {
                    font-size: 1.2rem;
                    margin-bottom: 2rem;
                }
                .btn {
                    display: inline-block;
                    background-color: #4c956c;
                    color: white;
                    padding: 0.8rem 1.5rem;
                    text-decoration: none;
                    border-radius: 5px;
                    transition: background-color 0.3s;
                    font-weight: bold;
                }
                .btn:hover {
                    background-color: #2c6e49;
                }
                .features {
                    display: flex;
                    flex-wrap: wrap;
                    justify-content: space-between;
                    margin-top: 3rem;
                }
                .feature {
                    flex: 0 0 30%;
                    background-color: white;
                    padding: 1.5rem;
                    margin-bottom: 2rem;
                    border-radius: 10px;
                    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
                }
                .feature h3 {
                    color: #2c6e49;
                }
                footer {
                    background-color: #2c6e49;
                    color: white;
                    text-align: center;
                    padding: 2rem 0;
                    margin-top: 2rem;
                }
            </style>
        </head>
        <body>
            <header>
                <h1>Floravia</h1>
                <p>Temukan Keindahan Alam di Rumah Anda</p>
            </header>
            <nav>
                <ul>
                    <li><a href="/">Home</a></li>
                    <li><a href="/produk/">Daftar Produk</a></li>
                    <li><a href="/kontak/">Kontak</a></li>
                </ul>
            </nav>
            <div class="hero">
                <div class="hero-content">
                    <h1>Selamat Datang di Floravia</h1>
                    <p>Toko tanaman hias terlengkap untuk mempercantik rumah dan taman Anda</p>
                    <a href="/produk/" class="btn">Lihat Koleksi Kami</a>
                </div>
            </div>
            <div class="container">
                <h2>Tentang Floravia</h2>
                <p>Floravia menyediakan berbagai pilihan tanaman hias berkualitas untuk mempercantik ruangan dan taman Anda. Kami berkomitmen untuk menyediakan tanaman terbaik dengan perawatan yang mudah dan harga yang terjangkau.</p>
                
                <div class="features">
                    <div class="feature">
                        <h3>Tanaman Indoor</h3>
                        <p>Koleksi tanaman indoor kami akan membuat ruangan Anda lebih segar, indah, dan menyehatkan.</p>
                    </div>
                    <div class="feature">
                        <h3>Tanaman Outdoor</h3>
                        <p>Percantik taman Anda dengan berbagai pilihan tanaman outdoor yang menawan.</p>
                    </div>
                    <div class="feature">
                        <h3>Kaktus & Sukulen</h3>
                        <p>Tanaman dekoratif yang mudah dirawat dan tahan lama untuk mempercantik sudut rumah Anda.</p>
                    </div>
                </div>
            </div>
            <footer>
                <p>&copy; 2025 Floravia. Semua Hak Dilindungi.</p>
            </footer>
        </body>
    </html>
    """
    return HttpResponse(html_content)

def produk_list(request):
    html_content = """
    <!DOCTYPE html>
    <html>
        <head>
            <title>Floravia - Daftar Produk</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <style>
                body {
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    margin: 0;
                    padding: 0;
                    background-color: #f8f9fa;
                    color: #333;
                    line-height: 1.6;
                }
                header {
                    background-color: #2c6e49;
                    color: white;
                    padding: 1rem 0;
                    text-align: center;
                }
                .container {
                    width: 80%;
                    margin: 0 auto;
                    padding: 2rem 0;
                }
                nav {
                    background-color: #4c956c;
                    padding: 1rem 0;
                }
                nav ul {
                    list-style-type: none;
                    margin: 0;
                    padding: 0;
                    text-align: center;
                }
                nav ul li {
                    display: inline;
                    margin: 0 15px;
                }
                nav ul li a {
                    color: white;
                    text-decoration: none;
                    font-weight: bold;
                    transition: color 0.3s;
                }
                nav ul li a:hover {
                    color: #d8f3dc;
                }
                .category {
                    margin-bottom: 2rem;
                }
                .category h2 {
                    color: #2c6e49;
                    border-bottom: 2px solid #4c956c;
                    padding-bottom: 0.5rem;
                    margin-bottom: 1rem;
                }
                .product-list {
                    display: grid;
                    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
                    gap: 2rem;
                }
                .product-card {
                    background-color: white;
                    border-radius: 10px;
                    overflow: hidden;
                    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
                    transition: transform 0.3s;
                }
                .product-card:hover {
                    transform: translateY(-5px);
                }
                .product-image {
                    height: 200px;
                    background-position: center;
                    background-size: cover;
                }
                .product-info {
                    padding: 1rem;
                }
                .product-info h3 {
                    margin-top: 0;
                    color: #2c6e49;
                }
                .product-info a {
                    display: inline-block;
                    background-color: #4c956c;
                    color: white;
                    padding: 0.5rem 1rem;
                    text-decoration: none;
                    border-radius: 5px;
                    transition: background-color 0.3s;
                    font-weight: bold;
                }
                .product-info a:hover {
                    background-color: #2c6e49;
                }
                footer {
                    background-color: #2c6e49;
                    color: white;
                    text-align: center;
                    padding: 2rem 0;
                    margin-top: 2rem;
                }
            </style>
        </head>
        <body>
            <header>
                <h1>Floravia</h1>
                <p>Temukan Keindahan Alam di Rumah Anda</p>
            </header>
            <nav>
                <ul>
                    <li><a href="/">Home</a></li>
                    <li><a href="/produk/">Daftar Produk</a></li>
                    <li><a href="/kontak/">Kontak</a></li>
                </ul>
            </nav>
            <div class="container">
                <h1>Katalog Produk Tanaman Hias</h1>
                
                <div class="category">
                    <h2>Tanaman Indoor</h2>
                    <div class="product-list">
                        <div class="product-card">
                            <div class="product-image" style="background-image: url('https://source.unsplash.com/random/400x300/?monstera');"></div>
                            <div class="product-info">
                                <h3>Monstera Deliciosa</h3>
                                <p>Tanaman populer dengan daun berlubang yang eksotis</p>
                                <a href="/produk/1/">Lihat Detail</a>
                            </div>
                        </div>
                        <div class="product-card">
                            <div class="product-image" style="background-image: url('https://source.unsplash.com/random/400x300/?fiddle+leaf+fig');"></div>
                            <div class="product-info">
                                <h3>Fiddle Leaf Fig</h3>
                                <p>Tanaman dengan daun berbentuk biola yang elegan</p>
                                <a href="/produk/2/">Lihat Detail</a>
                            </div>
                        </div>
                        <div class="product-card">
                            <div class="product-image" style="background-image: url('https://source.unsplash.com/random/400x300/?snake+plant');"></div>
                            <div class="product-info">
                                <h3>Snake Plant</h3>
                                <p>Tanaman yang mudah perawatan dan menyerap polutan</p>
                                <a href="/produk/3/">Lihat Detail</a>
                            </div>
                        </div>
                    </div>
                </div>
                
                <div class="category">
                    <h2>Tanaman Outdoor</h2>
                    <div class="product-list">
                        <div class="product-card">
                            <div class="product-image" style="background-image: url('https://source.unsplash.com/random/400x300/?aglaonema');"></div>
                            <div class="product-info">
                                <h3>Aglaonema</h3>
                                <p>Tanaman dengan daun berwarna-warni yang indah</p>
                                <a href="/produk/4/">Lihat Detail</a>
                            </div>
                        </div>
                        <div class="product-card">
                            <div class="product-image" style="background-image: url('https://source.unsplash.com/random/400x300/?anthurium');"></div>
                            <div class="product-info">
                                <h3>Anthurium</h3>
                                <p>Tanaman dengan bunga berbentuk hati yang menarik</p>
                                <a href="/produk/5/">Lihat Detail</a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <footer>
                <p>&copy; 2025 Floravia. Semua Hak Dilindungi.</p>
            </footer>
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
            'deskripsi': 'Tanaman hias indoor populer dengan daun besar berlubang yang cantik.',
            'perawatan': 'Letakkan di tempat dengan cahaya tidak langsung. Siram ketika tanah kering.',
            'img_keyword': 'monstera'
        },
        2: {
            'nama': 'Fiddle Leaf Fig',
            'harga': 'Rp 350.000',
            'deskripsi': 'Tanaman indoor dengan daun berbentuk biola yang elegan.',
            'perawatan': 'Butuh cahaya terang tidak langsung. Siram saat lapisan atas tanah kering.',
            'img_keyword': 'fiddle+leaf+fig'
        },
        3: {
            'nama': 'Snake Plant',
            'harga': 'Rp 150.000',
            'deskripsi': 'Tanaman hias yang mudah perawatannya dan bisa menyerap polutan.',
            'perawatan': 'Tahan kekeringan. Siram setiap 2-3 minggu sekali.',
            'img_keyword': 'snake+plant'
        },
        4: {
            'nama': 'Aglaonema',
            'harga': 'Rp 200.000',
            'deskripsi': 'Tanaman hias dengan daun berwarna-warni yang indah.',
            'perawatan': 'Letakkan di tempat dengan cahaya sedang. Siram saat tanah mulai kering.',
            'img_keyword': 'aglaonema'
        },
        5: {
            'nama': 'Anthurium',
            'harga': 'Rp 275.000',
            'deskripsi': 'Tanaman dengan bunga berbentuk hati yang menarik.',
            'perawatan': 'Suka tempat lembab dengan cahaya terang tidak langsung. Siram secukupnya, jangan sampai tergenang.',
            'img_keyword': 'anthurium'
        }
    }
    
    if produk_id in produk_details:
        produk = produk_details[produk_id]
        html_content = f"""
        <!DOCTYPE html>
        <html>
            <head>
                <title>Floravia - {produk['nama']}</title>
                <meta name="viewport" content="width=device-width, initial-scale=1">
                <style>
                    body {{
                        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                        margin: 0;
                        padding: 0;
                        background-color: #f8f9fa;
                        color: #333;
                        line-height: 1.6;
                    }}
                    header {{
                        background-color: #2c6e49;
                        color: white;
                        padding: 1rem 0;
                        text-align: center;
                    }}
                    .container {{
                        width: 80%;
                        margin: 0 auto;
                        padding: 2rem 0;
                    }}
                    nav {{
                        background-color: #4c956c;
                        padding: 1rem 0;
                    }}
                    nav ul {{
                        list-style-type: none;
                        margin: 0;
                        padding: 0;
                        text-align: center;
                    }}
                    nav ul li {{
                        display: inline;
                        margin: 0 15px;
                    }}
                    nav ul li a {{
                        color: white;
                        text-decoration: none;
                        font-weight: bold;
                        transition: color 0.3s;
                    }}
                    nav ul li a:hover {{
                        color: #d8f3dc;
                    }}
                    .product-detail {{
                        display: flex;
                        flex-wrap: wrap;
                        background-color: white;
                        border-radius: 10px;
                        overflow: hidden;
                        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
                        margin-top: 2rem;
                    }}
                    .product-image {{
                        flex: 1;
                        min-width: 300px;
                        background-image: url('https://source.unsplash.com/random/600x800/?{produk['img_keyword']}');
                        background-size: cover;
                        background-position: center;
                    }}
                    .product-info {{
                        flex: 1;
                        min-width: 300px;
                        padding: 2rem;
                    }}
                    .price {{
                        font-size: 1.5rem;
                        color: #2c6e49;
                        font-weight: bold;
                        margin: 1rem 0;
                    }}
                    .btn {{
                        display: inline-block;
                        background-color: #4c956c;
                        color: white;
                        padding: 0.8rem 1.5rem;
                        text-decoration: none;
                        border-radius: 5px;
                        transition: background-color 0.3s;
                        font-weight: bold;
                        margin-top: 1rem;
                    }}
                    .btn:hover {{
                        background-color: #2c6e49;
                    }}
                    .section {{
                        margin-top: 1.5rem;
                    }}
                    .section h3 {{
                        color: #2c6e49;
                        margin-bottom: 0.5rem;
                    }}
                    footer {{
                        background-color: #2c6e49;
                        color: white;
                        text-align: center;
                        padding: 2rem 0;
                        margin-top: 2rem;
                    }}
                </style>
            </head>
            <body>
                <header>
                    <h1>Floravia</h1>
                    <p>Temukan Keindahan Alam di Rumah Anda</p>
                </header>
                <nav>
                    <ul>
                        <li><a href="/">Home</a></li>
                        <li><a href="/produk/">Daftar Produk</a></li>
                        <li><a href="/kontak/">Kontak</a></li>
                    </ul>
                </nav>
                <div class="container">
                    <h1>Detail Produk</h1>
                    
                    <div class="product-detail">
                        <div class="product-image"></div>
                        <div class="product-info">
                            <h2>{produk['nama']}</h2>
                            <div class="price">{produk['harga']}</div>
                            
                            <div class="section">
                                <h3>Deskripsi</h3>
                                <p>{produk['deskripsi']}</p>
                            </div>
                            
                            <div class="section">
                                <h3>Perawatan</h3>
                                <p>{produk['perawatan']}</p>
                            </div>
                            
                            <a href="/produk/" class="btn">Kembali ke Katalog</a>
                        </div>
                    </div>
                </div>
                <footer>
                    <p>&copy; 2025 Floravia. Semua Hak Dilindungi.</p>
                </footer>
            </body>
        </html>
        """
    else:
        html_content = """
        <!DOCTYPE html>
        <html>
            <head>
                <title>Floravia - Produk Tidak Ditemukan</title>
                <meta name="viewport" content="width=device-width, initial-scale=1">
                <style>
                    body {
                        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                        margin: 0;
                        padding: 0;
                        background-color: #f8f9fa;
                        color: #333;
                        line-height: 1.6;
                    }
                    header {
                        background-color: #2c6e49;
                        color: white;
                        padding: 1rem 0;
                        text-align: center;
                    }
                    .container {
                        width: 80%;
                        margin: 0 auto;
                        padding: 2rem 0;
                        text-align: center;
                    }
                    nav {
                        background-color: #4c956c;
                        padding: 1rem 0;
                    }
                    nav ul {
                        list-style-type: none;
                        margin: 0;
                        padding: 0;
                        text-align: center;
                    }
                    nav ul li {
                        display: inline;
                        margin: 0 15px;
                    }
                    nav ul li a {
                        color: white;
                        text-decoration: none;
                        font-weight: bold;
                        transition: color 0.3s;
                    }
                    nav ul li a:hover {
                        color: #d8f3dc;
                    }
                    .error-container {
                        margin-top: 4rem;
                    }
                    .error-icon {
                        font-size: 5rem;
                        color: #ccc;
                        margin-bottom: 1rem;
                    }
                    .btn {
                        display: inline-block;
                        background-color: #4c956c;
                        color: white;
                        padding: 0.8rem 1.5rem;
                        text-decoration: none;
                        border-radius: 5px;
                        transition: background-color 0.3s;
                        font-weight: bold;
                        margin-top: 2rem;
                    }
                    .btn:hover {
                        background-color: #2c6e49;
                    }
                    footer {
                        background-color: #2c6e49;
                        color: white;
                        text-align: center;
                        padding: 2rem 0;
                        margin-top: 2rem;
                        position: absolute;
                        bottom: 0;
                        width: 100%;
                    }
                </style>
            </head>
            <body>
                <header>
                    <h1>Floravia</h1>
                    <p>Temukan Keindahan Alam di Rumah Anda</p>
                </header>
                <nav>
                    <ul>
                        <li><a href="/">Home</a></li>
                        <li><a href="/produk/">Daftar Produk</a></li>
                        <li><a href="/kontak/">Kontak</a></li>
                    </ul>
                </nav>
                <div class="container">
                    <div class="error-container">
                        <div class="error-icon">🌵</div>
                        <h1>Oops! Produk Tidak Ditemukan</h1>
                        <p>Maaf, produk yang Anda cari tidak ada dalam katalog kami.</p>
                        <a href="/produk/" class="btn">Kembali ke Katalog</a>
                    </div>
                </div>
                <footer>
                    <p>&copy; 2025 Floravia. Semua Hak Dilindungi.</p>
                </footer>
            </body>
        </html>
        """
    
    return HttpResponse(html_content)

def kontak(request):
    html_content = """
    <!DOCTYPE html>
    <html>
        <head>
            <title>Floravia - Kontak</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <style>
                body {
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    margin: 0;
                    padding: 0;
                    background-color: #f8f9fa;
                    color: #333;
                    line-height: 1.6;
                }
                header {
                    background-color: #2c6e49;
                    color: white;
                    padding: 1rem 0;
                    text-align: center;
                }
                .container {
                    width: 80%;
                    margin: 0 auto;
                    padding: 2rem 0;
                }
                nav {
                    background-color: #4c956c;
                    padding: 1rem 0;
                }
                nav ul {
                    list-style-type: none;
                    margin: 0;
                    padding: 0;
                    text-align: center;
                }
                nav ul li {
                    display: inline;
                    margin: 0 15px;
                }
                nav ul li a {
                    color: white;
                    text-decoration: none;
                    font-weight: bold;
                    transition: color 0.3s;
                }
                nav ul li a:hover {
                    color: #d8f3dc;
                }
                .contact-container {
                    display: flex;
                    flex-wrap: wrap;
                    margin-top: 2rem;
                }
                .contact-info {
                    flex: 1;
                    min-width: 300px;
                    background-color: white;
                    padding: 2rem;
                    border-radius: 10px;
                    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
                    margin-right: 2rem;
                    margin-bottom: 2rem;
                }
                .contact-form {
                    flex: 1;
                    min-width: 300px;
                    background-color: white;
                    padding: 2rem;
                    border-radius: 10px;
                    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
                }
                .contact-item {
                    margin-bottom: 1.5rem;
                }
                .contact-item h3 {
                    color: #2c6e49;
                    margin-bottom: 0.5rem;
                }
                .contact-icon {
                    margin-right: 10px;
                    color: #4c956c;
                }
                .map {
                    width: 100%;
                    height: 300px;
                    background-color: #ddd;
                    margin-top: 2rem;
                    border-radius: 10px;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    color: #777;
                    font-style: italic;
                }
                .form-group {
                    margin-bottom: 1.5rem;
                }
                .form-group label {
                    display: block;
                    margin-bottom: 0.5rem;
                    font-weight: bold;
                }
                .form-group input,
                .form-group textarea {
                    width: 100%;
                    padding: 0.8rem;
                    border: 1px solid #ddd;
                    border-radius: 5px;
                    font-family: inherit;
                }
                .form-group textarea {
                    min-height: 150px;
                }
                .btn {
                    display: inline-block;
                    background-color: #4c956c;
                    color: white;
                    padding: 0.8rem 1.5rem;
                    text-decoration: none;
                    border-radius: 5px;
                    transition: background-color 0.3s;
                    font-weight: bold;
                    border: none;
                    cursor: pointer;
                }
                .btn:hover {
                    background-color: #2c6e49;
                }
                footer {
                    background-color: #2c6e49;
                    color: white;
                    text-align: center;
                    padding: 2rem 0;
                    margin-top: 2rem;
                }
                .hours {
                    margin-top: 2rem;
                }
                .hours h3 {
                    color: #2c6e49;
                    margin-bottom: 0.5rem;
                }
                .hours-table {
                    width: 100%;
                    border-collapse: collapse;
                }
                .hours-table tr {
                    border-bottom: 1px solid #ddd;
                }
                .hours-table tr:last-child {
                    border-bottom: none;
                }
                .hours-table td {
                    padding: 0.5rem 0;
                }
                .hours-table td:last-child {
                    text-align: right;
                }
            </style>
        </head>
        <body>
            <header>
                <h1>Floravia</h1>
                <p>Temukan Keindahan Alam di Rumah Anda</p>
            </header>
            <nav>
                <ul>
                    <li><a href="/">Home</a></li>
                    <li><a href="/produk/">Daftar Produk</a></li>
                    <li><a href="/kontak/">Kontak</a></li>
                </ul>
            </nav>
            <div class="container">
                <h1>Hubungi Kami</h1>
                <p>Kami siap membantu Anda memilih tanaman yang tepat untuk rumah dan taman Anda.</p>
                
                <div class="contact-container">
                    <div class="contact-info">
                        <div class="contact-item">
                            <h3>Alamat</h3>
                            <p>Jl. Tanaman Hias No. 123<br>Jakarta Selatan, 12345<br>Indonesia</p>
                        </div>
                        
                        <div class="contact-item">
                            <h3>Kontak</h3>
                            <p>Telepon: (021) 1234-5678<br>Email: info@floravia.id</p>
                        </div>
                        
                        <div class="hours">
                            <h3>Jam Operasional</h3>
                            <table class="hours-table">
                                <tr>
                                    <td>Senin - Jumat</td>
                                    <td>08.00 - 17.00</td>
                                </tr>
                                <tr>
                                    <td>Sabtu</td>
                                    <td>09.00 - 15.00</td>
                                </tr>
                                <tr>
                                    <td>Minggu</td>
                                    <td>09.00 - 13.00</td>
                                </tr>
                            </table>
                        </div>
                        
                        <div class="map">
                            [Peta Lokasi Toko Floravia]
                        </div>
                    </div>
                    
                    <div class="contact-form">
                        <h3>Kirim Pesan</h3>
                        <form action="#">
                            <div class="form-group">
                                <label for="name">Nama</label>
                                <input type="text" id="name" name="name" required>
                            </div>
                            
                            <div class="form-group">
                                <label for="email">Email</label>
                                <input type="email" id="email" name="email" required>
                            </div>
                            
                            <div class="form-group">
                                <label for="subject">Subjek</label>
                                <input type="text" id="subject" name="subject" required>
                            </div>
                            
                            <div class="form-group">
                                <label for="message">Pesan</label>
                                <textarea id="message" name="message" required></textarea>
                            </div>
                            
                            <button type="submit" class="btn">Kirim Pesan</button>
                        </form>
                    </div>
                </div>
            </div>
            <footer>
                <p>&copy; 2025 Floravia. Semua Hak Dilindungi.</p>
            </footer>
        </body>
    </html>
    """
    return HttpResponse(html_content)