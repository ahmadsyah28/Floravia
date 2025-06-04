# produk/management/commands/populate_products.py
from django.core.management.base import BaseCommand
from produk.models import Produk

class Command(BaseCommand):
    help = 'Populate database with sample plant products for Floravia'
    
    def add_arguments(self, parser):
        parser.add_argument(
            '--clear',
            action='store_true',
            help='Clear existing products before adding new ones',
        )
    
    def handle(self, *args, **options):
        if options['clear']:
            self.stdout.write('Clearing existing products...')
            Produk.objects.all().delete()
            self.stdout.write(
                self.style.SUCCESS('All existing products have been deleted.')
            )
        
        sample_products = [
            # Indoor Plants
            {
                'nama': 'Monstera Deliciosa',
                'kategori': 'indoor',
                'harga': 250000,
                'stok': 15,
                'deskripsi': 'Tanaman hias indoor populer dengan daun besar berlubang yang cantik. Dikenal juga sebagai "Swiss Cheese Plant" karena lubang alami pada daunnya. Cocok untuk ruang tamu atau workspace modern.',
                'perawatan': 'Letakkan di tempat dengan cahaya tidak langsung yang terang. Siram ketika lapisan atas tanah kering (1-2 kali seminggu). Bersihkan daun secara berkala dengan kain lembab. Suhu ideal 18-24°C.',
                'gambar_url': 'https://source.unsplash.com/random/400x300/?monstera,deliciosa'
            },
            {
                'nama': 'Snake Plant (Sansevieria)',
                'kategori': 'indoor',
                'harga': 150000,
                'stok': 25,
                'deskripsi': 'Tanaman yang sangat mudah perawatannya dan efektif menyerap polutan udara seperti formaldehyde dan benzene. Ideal untuk pemula atau mereka yang sering bepergian.',
                'perawatan': 'Sangat tahan kekeringan. Siram setiap 2-3 minggu sekali atau ketika tanah benar-benar kering. Toleran terhadap berbagai kondisi cahaya. Hindari penyiraman berlebihan.',
                'gambar_url': 'https://source.unsplash.com/random/400x300/?snake,plant,sansevieria'
            },
            {
                'nama': 'Fiddle Leaf Fig',
                'kategori': 'indoor',
                'harga': 350000,
                'stok': 8,
                'deskripsi': 'Tanaman indoor statement dengan daun berbentuk biola yang besar dan mengkilap. Sangat populer untuk dekorasi ruangan bergaya modern dan minimalis.',
                'perawatan': 'Butuh cahaya terang tidak langsung. Siram saat lapisan atas tanah kering. Putar pot secara berkala agar pertumbuhan merata. Hindari perubahan lokasi yang sering.',
                'gambar_url': 'https://source.unsplash.com/random/400x300/?fiddle,leaf,fig'
            },
            {
                'nama': 'Pothos Golden',
                'kategori': 'indoor',
                'harga': 85000,
                'stok': 30,
                'deskripsi': 'Tanaman merambat dengan daun berbentuk hati dan corak emas yang indah. Sangat mudah tumbuh dan cocok untuk hanging basket atau pot biasa.',
                'perawatan': 'Toleran terhadap berbagai kondisi cahaya. Siram ketika tanah mulai kering. Bisa tumbuh di air atau tanah. Pangkas secara rutin untuk pertumbuhan lebat.',
                'gambar_url': 'https://source.unsplash.com/random/400x300/?pothos,golden'
            },
            {
                'nama': 'ZZ Plant (Zamioculcas)',
                'kategori': 'indoor',
                'harga': 180000,
                'stok': 12,
                'deskripsi': 'Tanaman dengan daun mengkilap dan batang yang kokoh. Sangat tahan dalam kondisi cahaya rendah dan jarang disiram, perfect untuk office space.',
                'perawatan': 'Sangat toleran terhadap kelalaian. Siram setiap 2-4 minggu. Toleran cahaya rendah hingga sedang. Hindari penyiraman berlebihan yang dapat menyebabkan akar busuk.',
                'gambar_url': 'https://source.unsplash.com/random/400x300/?zz,plant,zamioculcas'
            },
            
            # Outdoor Plants
            {
                'nama': 'Aglaonema Red Ruby',
                'kategori': 'outdoor',
                'harga': 200000,
                'stok': 10,
                'deskripsi': 'Tanaman hias dengan daun berwarna merah menyala yang memukau. Cocok untuk taman tropis atau sebagai focal point di area outdoor yang teduh.',
                'perawatan': 'Letakkan di tempat dengan cahaya sedang hingga terang tidak langsung. Siram saat tanah mulai kering. Suka kelembaban tinggi. Lindungi dari angin kencang.',
                'gambar_url': 'https://source.unsplash.com/random/400x300/?aglaonema,red,ruby'
            },
            {
                'nama': 'Anthurium Merah',
                'kategori': 'outdoor',
                'harga': 275000,
                'stok': 7,
                'deskripsi': 'Tanaman dengan bunga berbentuk hati berwarna merah cerah yang menarik. Memberikan sentuhan tropis yang eksotis untuk taman atau teras.',
                'perawatan': 'Suka tempat lembab dengan cahaya terang tidak langsung. Siram secukupnya, jangan sampai tergenang. Berikan pupuk cair setiap 2 minggu sekali.',
                'gambar_url': 'https://source.unsplash.com/random/400x300/?anthurium,red,flower'
            },
            {
                'nama': 'Philodendron Xanadu',
                'kategori': 'outdoor',
                'harga': 165000,
                'stok': 14,
                'deskripsi': 'Philodendron dengan daun berlobus dalam yang memberikan tekstur menarik. Tumbuh dalam bentuk semak yang rapi, cocok untuk border taman.',
                'perawatan': 'Preferensi cahaya sedang hingga terang. Siram ketika tanah bagian atas kering. Tahan terhadap kelembaban tinggi. Pangkas daun tua secara berkala.',
                'gambar_url': 'https://source.unsplash.com/random/400x300/?philodendron,xanadu'
            },
            {
                'nama': 'Caladium Rainbow',
                'kategori': 'outdoor',
                'harga': 145000,
                'stok': 16,
                'deskripsi': 'Tanaman dengan daun berwarna-warni seperti pelangi. Kombinasi warna pink, hijau, dan putih yang menawan untuk mempercantik area taman.',
                'perawatan': 'Butuh cahaya terang tidak langsung. Jaga kelembaban tanah tetapi tidak tergenang. Dorman di musim kering, tunas baru muncul di musim hujan.',
                'gambar_url': 'https://source.unsplash.com/random/400x300/?caladium,colorful'
            },
            
            # Kaktus & Sukulen
            {
                'nama': 'Kaktus Golden Barrel',
                'kategori': 'kaktus',
                'harga': 125000,
                'stok': 20,
                'deskripsi': 'Kaktus berbentuk bulat dengan duri emas yang berkilau. Tanaman statement yang memberikan sentuhan desert modern untuk dekorasi rumah.',
                'perawatan': 'Butuh sinar matahari langsung minimal 6 jam sehari. Siram sangat jarang, hanya ketika tanah benar-benar kering. Drainase yang baik sangat penting.',
                'gambar_url': 'https://source.unsplash.com/random/400x300/?golden,barrel,cactus'
            },
            {
                'nama': 'Succulent Mix Pot',
                'kategori': 'kaktus',
                'harga': 75000,
                'stok': 30,
                'deskripsi': 'Campuran berbagai jenis succulent cantik dalam satu pot. Kombinasi warna dan bentuk yang menarik, perfect untuk gift atau meja kerja.',
                'perawatan': 'Tempatkan di area terang dengan sinar matahari langsung. Siram sedikit setiap 1-2 minggu. Pastikan drainase pot baik untuk mencegah akar busuk.',
                'gambar_url': 'https://source.unsplash.com/random/400x300/?succulent,mix,pot'
            },
            {
                'nama': 'Echeveria Elegans',
                'kategori': 'kaktus',
                'harga': 65000,
                'stok': 25,
                'deskripsi': 'Succulent dengan bentuk roset yang sempurna dan warna biru-hijau yang soft. Sering disebut "Mexican Snowball" karena bentuknya yang unik.',
                'perawatan': 'Cahaya terang hingga sinar matahari langsung. Siram jarang, biarkan tanah kering total antara penyiraman. Hindari air di pusat roset.',
                'gambar_url': 'https://source.unsplash.com/random/400x300/?echeveria,elegans'
            },
            {
                'nama': 'Haworthia Zebra',
                'kategori': 'kaktus',
                'harga': 55000,
                'stok': 22,
                'deskripsi': 'Succulent kecil dengan motif garis putih seperti zebra. Sangat cocok untuk terrarium atau sebagai tanaman meja karena ukurannya yang compact.',
                'perawatan': 'Preferensi cahaya terang tidak langsung. Siram saat tanah kering, lebih sering di musim panas. Toleran terhadap kondisi indoor.',
                'gambar_url': 'https://source.unsplash.com/random/400x300/?haworthia,zebra'
            },
            {
                'nama': 'Kaktus Cereus Spiral',
                'kategori': 'kaktus',
                'harga': 195000,
                'stok': 8,
                'deskripsi': 'Kaktus dengan bentuk spiral yang unik dan menawan. Pertumbuhan yang lambat membuatnya menjadi koleksi berharga untuk pecinta kaktus.',
                'perawatan': 'Sinar matahari langsung penuh. Siram sangat jarang, terutama di musim dingin. Tanah dengan drainase sangat baik. Rotasi pot untuk pertumbuhan merata.',
                'gambar_url': 'https://source.unsplash.com/random/400x300/?cereus,spiral,cactus'
            }
        ]
        
        self.stdout.write('Adding sample products...')
        created_count = 0
        
        for product_data in sample_products:
            produk, created = Produk.objects.get_or_create(
                nama=product_data['nama'],
                defaults=product_data
            )
            if created:
                created_count += 1
                self.stdout.write(
                    self.style.SUCCESS(f'✅ Created: {produk.nama} - {produk.get_formatted_harga()}')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'⚠️  Already exists: {produk.nama}')
                )
        
        self.stdout.write('')
        self.stdout.write(
            self.style.SUCCESS(f'🌱 Successfully created {created_count} new products!')
        )
        self.stdout.write(
            self.style.SUCCESS(f'📊 Total products in database: {Produk.objects.count()}')
        )
        self.stdout.write('')
        
        # Show category breakdown
        for kategori_code, kategori_name in Produk.KATEGORI_CHOICES:
            count = Produk.objects.filter(kategori=kategori_code).count()
            self.stdout.write(f'   {kategori_name}: {count} products')
        
        self.stdout.write('')
        self.stdout.write(
            self.style.SUCCESS('🎉 Database population completed! Visit http://127.0.0.1:8000/ to see your products.')
        )