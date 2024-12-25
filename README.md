🖼️ Flask Image Processing Project 🚀

Proyek ini adalah aplikasi berbasis Flask yang memungkinkan pengguna mengunggah gambar, memprosesnya secara paralel (resize & convert), dan mengunduh hasilnya. Menggunakan Python, Flask, Dask, dan Pillow untuk memastikan proses lebih cepat dan efisien. 💻✨

📂 Struktur Proyek
├── app.py                # Aplikasi Flask utama
├── process_images.py     # Proses resize dan konversi gambar
├── requirements.txt      # Library dan dependencies
├── static
│   ├── input             # Folder untuk gambar yang diunggah
│   └── output            # Folder untuk hasil gambar yang diproses
└── README.md

🛠️ Fitur

🚀 Parallel Processing - Proses banyak gambar sekaligus dengan Dask
🖼️ Resize & Convert - Ubah ukuran dan format gambar dengan mudah
📤 Upload & Download - Unggah dan unduh gambar melalui API Flask
🔒 File Validation - Hanya menerima file berformat PNG, JPG, dan JPEG

📥 Instalasi

Clone repositori ini:
git clone https://github.com/ladyaksm/image-processing-parallel.git

Masuk ke direktori proyek:
cd image-processing-parallel


Instal dependensi:
pip install flask pillow dask werkzeug
pip install pillow dask

🚀 Menjalankan Aplikasi
python app.py
Akses aplikasi melalui: http://127.0.0.1:5000

📤 Upload Gambar
Gunakan aplikasi  Postman atau antarmuka lain untuk mengunggah gambar ke endpoint http://127.0.0.1:5000/upload dengan metode POST.
Format form-data:
     Key: images (multiple files)
     Value: Gambar-gambar yang ingin diproses.


📥 Download Gambar Hasil
Unduh hasil di folder static/output dengan mengakses:
http://127.0.0.1:5000/output/<nama_file>.jpg.


🚪 Endpoint API
Hasil JSON API 
{
  "results": [
    "image1.jpg processed successfully.",
    "image2.jpg processed successfully."
  ]
}

Selamat mencoba! 🎉 Jangan lupa bintang ⭐ jika proyek ini bermanfaat.

