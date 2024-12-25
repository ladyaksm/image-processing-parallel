import os
from PIL import Image
from dask import delayed, compute

# Fungsi untuk memproses gambar
def process_image(image_path, output_path, size=(1920, 1080), format='PNG', quality=95):
    try:
        with Image.open(image_path) as img:
            img = img.resize(size)  # Mengubah ukuran gambar
            img.save(output_path, format=format, quality=quality)  # Menyimpan gambar
        return f"{os.path.basename(image_path)} processed successfully."
    except Exception as e:
        return f"Error processing {os.path.basename(image_path)}: {e}"

# Fungsi untuk mendistribusikan tugas menggunakan Dask
def process_images_in_parallel(image_paths, output_dir, size=(1920, 1080), format='PNG'):
    tasks = []
    for image_path in image_paths:
        # Ubah nama output_path agar memiliki ekstensi sesuai format
        output_filename = f"{os.path.splitext(os.path.basename(image_path))[0]}.{format.lower()}"
        output_path = os.path.join(output_dir, output_filename)
        
        task = delayed(process_image)(image_path, output_path, size=size, format=format)
        tasks.append(task)
    results = compute(*tasks)  # Mengeksekusi semua tugas secara paralel
    return results

