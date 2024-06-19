import zipfile

arxiuOrginal=input("De quin arxiu vols veure el contingut?\n>")

arxiu=zipfile.ZipFile(arxiuOrginal,'r')

for nomArxiu in arxiu.namelist():
    print(nomArxiu)
arxiu.close()