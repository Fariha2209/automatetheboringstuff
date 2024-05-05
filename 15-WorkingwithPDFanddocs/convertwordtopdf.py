import docx

wordFilename = 'testing.docx'
pdfFilename = 'testing.pdf'

doc = docx.Document()
doc.save(wordFilename)


wdFormatPDF = 17
#wordObj = win32com.client.Dispatch('Word.Application')

#docObj = wordObj.Documents.Open(wordFilename)
#docObj.SaveAs(pdfFilename, FileFormat=wdFormatPDF)
#docObj.Close()
#wordObj.Quit()