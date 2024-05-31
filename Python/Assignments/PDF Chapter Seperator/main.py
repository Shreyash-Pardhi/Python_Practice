import fitz
import re

pdf_doc = fitz.open("Assignments\\PDF Chapter Seperator\\UniversityPhysicsVolume1-LR.pdf")

page1 = pdf_doc.load_page(page_id=6)
page2 = pdf_doc.load_page(page_id=7)
page3 = pdf_doc.load_page(page_id=8)

pg = page1.get_text("text") + page2.get_text("text") + page3.get_text("text")

chapter_line = re.findall("Chapter.*",pg)
chapter_pageNo=[]

for i in chapter_line:
    strr = i
    pg_no = strr.split()[-1]
    chapter_pageNo.append(int(pg_no))
    
for i in range (len(chapter_pageNo)):
    pdf2 = fitz.open()
    if(i == (len(chapter_pageNo)-1)):
        pdf2.insert_pdf(pdf_doc,from_page=(chapter_pageNo[i]+9))
        pdf2.save(f"Chapter{i+1}.pdf")
        break
    
    pdf2 = fitz.open()
    pdf2.insert_pdf(pdf_doc,from_page=(chapter_pageNo[i]+9), to_page=(chapter_pageNo[i+1]+8))
    pdf2.save(f"Chapter{i+1}.pdf")