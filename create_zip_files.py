from zipfile import ZipFile
import os.path


if not os.path.exists("resources"):
    os.mkdir("resources")
zip_path = os.path.join("resources", "documents.zip")
files = [os.path.join("File_folder", "File_pdf.pdf"), os.path.join("File_folder", "File_xls.xlsx"), os.path.join("File_folder", "File_csv.csv")]
with  ZipFile(zip_path, 'w') as zip_file:
    for file in files:
        zip_file.write(file)
print("Список доступных файлов в архиве:")
print(zip_file.namelist())




