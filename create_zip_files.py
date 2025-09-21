import zipfile
import os.path

def create_zip_files():
    if not os.path.exists("resources"):
        os.mkdir("resources")

    zip_path = os.path.join("resources", "documents.zip")
    files = [os.path.join("File_folder", "File_pdf.pdf"), os.path.join("File_folder", "File_xls.xlsx"), os.path.join("File_folder", "File_csv.csv")]

    with zipfile.ZipFile(zip_path, 'x', compression=zipfile.ZIP_DEFLATED) as zip_file:
        for file in files:
            add_file_path = os.path.join(zip_path, file)
            zip_file.write(file, os.path.basename(file))
            print(f'Путь к файлу в архиве: {add_file_path}')


create_zip_files()


