Flask Image Processing Project

Deskripsi Proyek
Proyek ini bertujuan untuk membangun sistem pemrosesan gambar secara paralel menggunakan Python, Flask sebagai backend server, dan Dask untuk menjalankan komputasi terdistribusi. Aplikasi ini memungkinkan pengguna untuk mengunggah beberapa gambar sekaligus, memprosesnya (mengubah ukuran dan format), dan mengunduh hasilnya.


Fitur Utama
Unggah Banyak Gambar: Pengguna dapat mengunggah beberapa gambar dalam sekali proses.
Resize dan Konversi Format: Gambar akan diubah ukurannya ke resolusi yang telah ditentukan dan dikonversi ke format PNG.
Pemrosesan Paralel: Menggunakan Dask untuk mempercepat proses gambar dalam jumlah besar.
API Flask: Menggunakan Flask sebagai server untuk menangani unggahan dan unduhan gambar.

Teknologi yang Digunakan
Python 
Flask
Dask
Pillow (PIL)



Instalasi dan Konfigurasi

1. Clone Repository
git clone https://github.com/ladyaksm/image-processing-parallel.git
cd image-processing-parallel

2. Buat Virtual Environment (Opsional)
python -m venv venv
source venv/bin/activate  # Untuk Linux/Mac
venv\Scripts\activate    # Untuk Windows

3. Instalasi Dependensi
pip install -r requirements.txt

4. Jalankan Aplikasi
python app.py

Aplikasi akan berjalan di http://localhost:5000.

Struktur Proyek

.
├── app.py                         # Flask backend
├── process_images.py              # Modul pemrosesan gambar
├── requirements.txt               # Dependensi proyek
├── static
│   ├── input                      # Folder untuk unggah gambar
│   └── output                     # Folder hasil pemrosesan
└── README.md                      # Dokumentasi ini

Penggunaan

1. Mengunggah Gambar

Buka Postman atau tool API lainnya.
Kirimkan HTTP POST request ke http://localhost:5000/upload dengan form-data dan key images.
Gambar akan diproses dan hasilnya dapat diunduh di folder static/output.

2. Mengunduh Gambar

Kirimkan GET request ke http://localhost:5000/output/<nama_file> untuk mengunduh gambar hasil.
Contoh Request
curl -X POST -F "images=@path/to/image.jpg" http://localhost:5000/upload
Catatan Penting
Hanya mendukung file dengan ekstensi .jpg, .jpeg, dan .png.
Pastikan folder static/input dan static/output sudah dibuat sebelum menjalankan aplikasi.
