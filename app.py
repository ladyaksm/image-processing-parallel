from flask import Flask, request, jsonify, send_from_directory
import os
from werkzeug.utils import secure_filename
from process_images import process_images_in_parallel

# Inisialisasi Flask
app = Flask(__name__)

# Konfigurasi folder
UPLOAD_FOLDER = 'static/input'
OUTPUT_FOLDER = 'static/output'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['OUTPUT_FOLDER'] = OUTPUT_FOLDER

# Membuat folder jika belum ada
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Fungsi untuk memvalidasi ekstensi file
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Route untuk unggah gambar
@app.route('/upload', methods=['POST'])
def upload_images():
    if 'images' not in request.files:
        return jsonify({"error": "No files provided!"}), 400

    files = request.files.getlist('images')
    uploaded_files = []
    for file in files:
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            uploaded_files.append(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    if not uploaded_files:
        return jsonify({"error": "No valid files uploaded!"}), 400

    # Proses gambar secara paralel
    results = process_images_in_parallel(uploaded_files, app.config['OUTPUT_FOLDER'])
    return jsonify({"results": results}), 200

# Route untuk mengunduh gambar hasil
@app.route('/output/<filename>', methods=['GET'])
def download_file(filename):
    return send_from_directory(app.config['OUTPUT_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)
