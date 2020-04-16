import PyPDF2 as pdf

pdfObj = open('texto.pdf','rb')
pdfReader = pdf.PdfFileReader(pdfObj)

x=pdfReader.numPages
pageObj = pdfReader.getPage(x-1)
text = pageObj.extractText()

file1=open(r"texto.txt","a")
file1.writelines(text)
file1.close()