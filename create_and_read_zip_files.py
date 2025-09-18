import zipfile
import os
from pathlib import Path

  # Создаем zip-архив с файлами и помещаем его в папку ресурсов
  # zip_files: имя zip-архива
  # files_to_zip: список путей к файлам для добавления в архив
  # resources_dir: папка для ресурсов

def create_zip_files(zip_files, files_to_zip, resources_dir="resources"):

    # Создаем папку resources
    os.makedirs(resources_dir, exist_ok=True)

    # Полный путь к zip-архиву в папке resources
    zip_path = os.path.join(resources_dir, zip_files)

    # Создаем zip-архив
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for file_path in files_to_zip:
            if os.path.exists(file_path):
                # Добавляем файл в архив с сохранением имени
                zipf.write(file_path, os.path.basename(file_path))
                print(f"Добавлен файл: {file_path}")
            else:
                print(f"Файл не найден: {file_path}")

    print(f"Архив создан: {zip_path}")
    return zip_path


if __name__ == "__main__":
    # Файлы для добавления в архив (пути)
    files = [
        "File_folder/File_pdf.pdf",
        "File_folder/File_xls.xlsx",
        "File_folder/File_csv.csv"
    ]

    # Создаем архив
    zip_path = create_zip_files("documents.zip", files, "resources")