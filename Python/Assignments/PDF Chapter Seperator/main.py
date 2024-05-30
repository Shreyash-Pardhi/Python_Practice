import fitz
import re

pdf_doc = fitz.open("Assignments\\PDF Chapter Seperator\\UniversityPhysicsVolume1-LR.pdf")

page1 = pdf_doc.load_page(page_id=6)
page2 = pdf_doc.load_page(page_id=7)
page3 = pdf_doc.load_page(page_id=8)

pg = page1.get_text("text") + page2.get_text("text") + page3.get_text("text")

chap = re.findall("Chapter.*",pg)
pg_list=[]

for i in chap:
    strr = i
    pg_no = strr.split()[-1]
    pg_list.append(int(pg_no))

for i in range (len(pg_list)-1):

    pdf2 = fitz.open()
    pdf2.insert_pdf(pdf_doc,from_page=(pg_list[i]+9), to_page=(pg_list[i+1]+8))
    pdf2.save(f"Chapter{i+1}.pdf")