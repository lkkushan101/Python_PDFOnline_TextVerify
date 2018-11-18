import requests
import PyPDF2
url = 'http://africau.edu/images/default/sample.pdf'
fileName = 'sample.pdf'
req = requests.get(url)
file = open(fileName, 'wb')
for chunk in req.iter_content(100000):
    file.write(chunk)
file.close()
pdfFileObject = open('sample.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObject)
count = pdfReader.numPages
for i in range(count):
    page = pdfReader.getPage(i)
    print(page.extractText())
    if page.extractText().find('Virtual Mechanics'):
        print('Text found...')