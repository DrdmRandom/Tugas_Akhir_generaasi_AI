import os
import shutil


def move_photos_to_single_folder(source_root_folder, destination_folder):
    """
    Fungsi untuk memindahkan semua file foto dari folder-folder di dalam source_root_folder
    ke satu folder tujuan.

    Parameters:
    source_root_folder (str): Path folder utama yang berisi folder-folder dengan foto.
    destination_folder (str): Path folder tujuan untuk menyimpan semua foto.
    """
    # Ekstensi foto yang didukung
    photo_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp'}

    # Pastikan folder tujuan ada
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Iterasi melalui semua subfolder
    for root, _, files in os.walk(source_root_folder):
        for file in files:
            # Periksa apakah file adalah foto berdasarkan ekstensi
            if os.path.splitext(file)[1].lower() in photo_extensions:
                source_path = os.path.join(root, file)
                destination_path = os.path.join(destination_folder, file)

                try:
                    # Pindahkan file ke folder tujuan
                    shutil.move(source_path, destination_path)
                    print(f"Moved: {source_path} -> {destination_path}")
                except Exception as e:
                    print(f"Error moving {source_path}: {e}")


# Contoh penggunaan
source_root_folder = r"C:\Users\dawwi\Downloads\Dataset 2\archive (1) V" # Ganti dengan path folder sumber
destination_folder = r"C:\Users\dawwi\Downloads\Dataset 4\Class 0"  # Ganti dengan path folder tujuan

move_photos_to_single_folder(source_root_folder, destination_folder)
