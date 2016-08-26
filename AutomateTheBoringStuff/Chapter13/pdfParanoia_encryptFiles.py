'''
Using the os.walk() function from Chapter 9, write a script that will go
through every PDF in a folder (and its subfolders) and encrypt the PDFs
using a password provided on the command line. Save each encrypted PDF
with an _encrypted.pdf suffix added to the original filename. Before
deleting the original file, have the program attempt to read and decrypt
the file to ensure that it was encrypted correctly.

Then, write a program that finds all encrypted PDFs in a folder (and its
subfolders) and creates a decrypted copy of the PDF using a provided password.
If the password is incorrect, the program should print a message to the user
and continue to the next PDF.
'''

import PyPDF2,os,send2trash

#parent directory
directory = 'PDFPARANOIA'

for folders,subfolders,files in os.walk(directory):
    for fileS in [fi for fi in files if fi.endswith('.pdf')]:
        pdfFile = open(folders+'\\'+fileS,'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFile)
        pdfWriter = PyPDF2.PdfFileWriter()
        for pageNum in range(pdfReader.numPages):
            pdfWriter.addPage(pdfReader.getPage(pageNum))
        pdfWriter.encrypt('allelomorphisms')
        resultPdf = open(folders+'\\'+os.path.splitext(os.path.basename(fileS))[0]+'_encrypted.pdf','wb')
        pdfWriter.write(resultPdf)
        resultPdf.close()
        resultPdf = open(folders+'\\'+os.path.splitext(os.path.basename(fileS))[0]+'_encrypted.pdf','rb')
        pdfReader = PyPDF2.PdfFileReader(resultPdf)
        pdfFile.close()
        #delete file if encrypted
        if pdfReader.isEncrypted:
            print('File %s is now encrypted. Deleting original.'%(os.path.basename(fileS)))
            resultPdf.close()
            send2trash.send2trash(folders+'\\'+fileS)
        else:
            print('File %s is NOT encrypted.'%(os.path.basename(fileS)))
            resultPdf.close()
