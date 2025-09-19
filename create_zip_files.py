import zipfile
from zipfile import ZipFile
import os.path


if not os.path.exists("resources"):
    os.mkdir("resources")
zip_path = os.path.join("resources", "documents.zip")
files = [os.path.join("File_folder", "File_pdf.pdf"), os.path.join("File_folder", "File_xls.xlsx"), os.path.join("File_folder", "File_csv.csv")]


with zipfile.ZipFile(zip_path, 'w', compression=zipfile.ZIP_DEFLATED) as zip_file:
    for file in files:
        add_file_path = os.path.join(zip_path, file)
        zip_file.write(file)
        print(add_file_path)
