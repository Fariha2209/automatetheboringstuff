import PyPDF2

pdf1File = open('/Users/farihaalam/Documents/meetingminutes.pdf', 'rb')
pdf2File = open('/Users/farihaalam/Downloads/automate_online-materials/meetingminutes2.pdf', 'rb')

pdf1Reader = PyPDF2.PdfFileReader(pdf1File) 
pdf2Reader = PyPDF2.PdfFileReader(pdf2File)

pdfWriter = PyPDF2.PdfFileWriter()

for pageNum in range(pdf1Reader.numPages):
    pageObj = pdf1Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)

for pageNum in range(pdf2Reader.numPages):
    pageObj = pdf2Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)

pdfOutputFile = open('combinedminutes.pdf', 'wb')
pdfWriter.write(pdfOutputFile)
pdfOutputFile.close()
pdf1File.close()
pdf2File.close()

#rotating
minutesFile = open('/Users/farihaalam/Documents/python/combinedminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(minutesFile)

page = pdfReader.getPage(0)
page.rotateClockwise(90)

pdfwriter = PyPDF2.PdfFileWriter()
pdfwriter.addPage(page)
resultPdfFile = open('rotatedPage.pdf', 'wb')
pdfwriter.write(resultPdfFile)
resultPdfFile.close()
minutesFile.close()

# watermark
minutesFile = open('/Users/farihaalam/Documents/meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(minutesFile)
minutesFirstPage = pdfReader.getPage(0)
pdfWatermarkReader = PyPDF2.PdfFileReader(open('/Users/farihaalam/Downloads/automate_online-materials/watermark.pdf', 'rb'))
minutesFirstPage.mergePage(pdfWatermarkReader.getPage(0))
pdfWriter = PyPDF2.PdfFileWriter()
pdfWriter.addPage(minutesFirstPage)

for pageNum in range(1, pdfReader.numPages):
    pageObj = pdfReader.getPage(pageNum)
    pdfWriter.addPage(pageObj)

resultPdfFile = open('watermarkedCover.pdf', 'wb')
pdfWriter.write(resultPdfFile)
minutesFile.close()
resultPdfFile.close()

# Encrypting

pdfFile = open('/Users/farihaalam/Documents/meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFile)
pdfWriter = PyPDF2.PdfFileWriter()

for pageNum in range(pdfReader.numPages):
    pdfWriter.addPage(pdfReader.getPage(pageNum))


pdfWriter.encrypt('swordfish')
resultPdf = open('encryptedminutes.pdf', 'wb')
pdfWriter.write(resultPdf)
resultPdf.close()
