from pypdf import PdfWriter
import os

merger = PdfWriter()
os.chdir("Snaps/PDFs")

for file in os.listdir():

    if file.endswith(".pdf"):
        merger.append(file)

merger.write("merged-pdf.pdf")