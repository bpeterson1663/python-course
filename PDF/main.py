import PyPDF2
import os
import sys

inputs = sys.argv[1:]
cwd = os.getcwd()

def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write('docs/all.pdf')
    

with open(os.path.join(cwd, "docs/dummy.pdf"), 'rb') as file:
    reader = PyPDF2.PdfFileReader(file)
    page = reader.getPage(0)
    page.rotateCounterClockwise(-90)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open(os.path.join(cwd, 'docs/tilt.pdf'), 'wb') as new_file:
        writer.write(new_file)
        
pdf_combiner(inputs)


# python3 main.py docs/dummy.pdf docs/twopage.pdf docs/tilt.pd