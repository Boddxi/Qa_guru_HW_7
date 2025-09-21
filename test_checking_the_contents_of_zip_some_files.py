from zipfile import ZipFile
import PyPDF2
from io import BytesIO
import pandas as pd
from io import TextIOWrapper


def test_checking_the_contents_of_zip_pdf_files():
    with ZipFile('resources/documents.zip') as zip_file:
        with zip_file.open('File_pdf.pdf') as pdf_file:
            # Создаем PdfReader из бинарных данных
            reader_pdf = PyPDF2.PdfReader(BytesIO(pdf_file.read()))
            print("Первая страница файла содержит текст:")
            text_pdf= reader_pdf.pages[0].extract_text()
            print(text_pdf)
            assert "PBR руководство от Allegorithmic" in text_pdf


def test_checking_the_contents_of_zip_xlsx_files():
    with ZipFile('resources/documents.zip') as zip_file:
        with zip_file.open('File_xls.xlsx') as xlsx_file:
            reader_xlsx = pd.read_excel(xlsx_file.read())
            print("Содержимое файла XlSX:")
            print(reader_xlsx)
            assert 'ширина' in reader_xlsx.columns
            assert 'Runflat' in reader_xlsx['опции'].values


def test_checking_the_contents_of_zip_csv_files():
    with ZipFile('resources/documents.zip') as zip_file:
        with zip_file.open('File_csv.csv') as csv_file:
            reader_csv = pd.read_csv(TextIOWrapper(csv_file, encoding='cp1251'))
            print("Содержимое файла CSV:")
            print(reader_csv)
            column_names = list(reader_csv.columns)
            print(column_names)
            assert ['Статус;Дата;Комментарий;Серийный номер;Обработка'] == column_names
