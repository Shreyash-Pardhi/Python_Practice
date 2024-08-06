This folder has a pdf called "UniversityPhysicsVolume1". We want to break down the book into chapters and topics as per the index page.



You can use the fitz library to load and convert the pages into text.
Some basic operations with fitz-

#install fitz
pip install pymupdf
import fitz  # PyMuPDF

# 1. Open a PDF File
pdf_document = "example.pdf"
doc = fitz.open(pdf_document)

# 2. Extract Text from a Page
page_number = 0  # first page
page = doc.load_page(page_number)
text = page.get_text()


The book uses specific patterns for chapter and topic names which you can leverage to break down the book. Also You can use the  page number given in the index page.

Write a function by which we can break down any book of similar publication by just providing the pdf and page numbers of the index page.