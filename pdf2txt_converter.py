import pandas as pd
from PyPDF2 import PdfReader
import glob
import os
import shutil


no_text_pdfs = []

all_media_dir = 'all_media'
pdf_dir = 'pdf_to_convert'

start_num = len(os.listdir(all_media_dir))

for i, file_name in enumerate(os.listdir(pdf_dir)):

    # read PDF and store its text in a string
    pdf_reader = PdfReader(os.path.join(pdf_dir, file_name))
    pdf_text = ''
    for p in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[p]
        pdf_text += (page.extract_text())

    # if some text was found in the PDF
    if pdf_text:

        # create a folder to store the PDF and TXT files
        new_media_dir = f'{all_media_dir}/media{start_num + i:05}'
        if not os.path.exists(new_media_dir):
            os.makedirs(new_media_dir)

        # move the PDF in the new folder
        shutil.move(os.path.join(pdf_dir, file_name), os.path.join(new_media_dir, file_name))

        # store the text of the PDF in a TXT file stored in the new folder
        with open(f'{new_media_dir}/text.txt', 'w', encoding='utf-8') as txt_file:
            txt_file.write(pdf_text)
        print(f'{new_media_dir}/text.txt file created.')

    else:
        no_text_pdfs.append(file_name)
        print(f'No text found in {file_name}')

# store the name of the PDFs where no text where found in a TXT file
if len(no_text_pdfs) > 0:
    with open('no_text_pdfs.txt', 'w', encoding='utf-8') as file:
        for file_name in no_text_pdfs:
            file.write(file_name + '\n')



