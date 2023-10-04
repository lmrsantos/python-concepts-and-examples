import PyPDF2

## READ
### OPEN
f = open("Free_Test_Data_100KB_PDF.pdf", mode="rb")
## INSTANTIATE THE OBJECT
pdf_reader = PyPDF2.PdfReader(f)

print (len(pdf_reader.pages))

## GET THE PAGE
page_one = pdf_reader.pages[0]

## EXTRACT THE TEXT
page_one_text = page_one.extract_text()

print (page_one_text)

## WRITE
# CREATE A WRITER OBJECT
pdf_writer = PyPDF2.PdfWriter()
print (type(page_one))
# the page to be added must be a PageObject type. Adding the first 2 pages only
for i in range(0,2):
    pdf_writer.add_page(pdf_reader.pages[i])
# pdf_writer.add_page(page_one)
## OPEN THE NEW FILE (It will be overrided if exists)
pdf_output = open("new_pdf.pdf", "wb")
# WRITE THE CONTENT
pdf_writer.write(pdf_output)
pdf_output.close()
f.close()
