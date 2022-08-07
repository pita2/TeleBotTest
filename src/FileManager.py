import PyPDF2
import os
from docx2pdf import convert
class PdfFile():
    def split(self):
        for filename in os.listdir("files"):
            with open(os.path.join("files", filename), 'rb') as pdf_file:
                pdf_reader = PyPDF2.PdfFileReader(pdf_file)
                for i in range(pdf_reader.numPages):
                    pdf_writer = PyPDF2.PdfFileWriter()
                    pdf_writer.addPage(pdf_reader.getPage(i))
                    output_file_name = f'{filename[:len(filename)-4]}_{i}.pdf'
                    with open(os.path.join("files", output_file_name), 'wb') as output_file:
                        pdf_writer.write(output_file)
            os.remove(os.path.join("files", filename))

    def merge(self):
        pdf_merger = PyPDF2.PdfFileMerger()

        for pdf_file_name in os.listdir("files"):
            pdf_file = open(os.path.join("files", pdf_file_name), "rb")
            pdf_merger.append(pdf_file)
            pdf_file.close()
            os.remove(os.path.join("files", pdf_file_name))

        pdf_file_merged = open(os.path.join("files", 'merged.pdf'), "wb+")
        pdf_merger.write(pdf_file_merged)
    def convert(self):
        for filename in os.listdir("files"):
            pass
