import PyPDF2
import os

cwd = os.getcwd()

print(cwd)

with open(os.path.join(cwd, "docs/dummy.pdf"), 'rb') as file:
    reader = PyPDF2.PdfFileReader(file)
    page = reader.getPage(0)
    page.rotateCounterClockwise(-90)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open(os.path.join(cwd, 'docs/tilt.pdf'), 'wb') as new_file:
        writer.write(new_file)