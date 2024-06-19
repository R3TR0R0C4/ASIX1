import os,zipfile

"""mida=os.stat("mbox.txt").st_size
print(mida/1024/1024,"mb")"""


extracioTest=zipfile.ZipFile('test.zip')

"""extracioTest.extractall()
extracioTest.close()"""

"""extracioTest.extract('act1.py')
extracioTest.extract('act2.py','test/')
extracioTest.close()"""

llistat_a_comprimir=['mbox.txt','mbox-short.txt']

newZip=zipfile.ZipFile("nou_arxiu2.zip",'w')

for fitxer in llistat_a_comprimir:
    newZip.write(fitxer,compress_type=zipfile.ZIP_LZMA)

newZip.close()