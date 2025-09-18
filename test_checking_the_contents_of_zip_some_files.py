from zipfile import ZipFile
import PyPDF2
from io import BytesIO
import os.path


def test_checking_the_contents_of_zip_pdf_file():
    with ZipFile(os.path.abspath('resources/documents.zip')) as zip_file:
        print("Список доступных файлов в архиве:")
        print(zip_file.namelist())
        with zip_file.open('File_folder/File_pdf.pdf') as pdf_file:
            # Создаем PdfReader из бинарных данных
            pdf_reader = PyPDF2.PdfReader(BytesIO(pdf_file.read()))
            print("Первая страница файла содержит текст:")
            text= pdf_reader.pages[0].extract_text()
            print(text)
            assert "PBR руководство от Allegorithmic" in text
