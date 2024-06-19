import zipfile

arxiuOrginal=input("De quin arxiu vols veure el contingut?\n>")

arxiu=zipfile.ZipFile(arxiuOrginal,'r')

for nomArxiu in arxiu.namelist():
    if nomArxiu.endswith(".txt"):
        print(nomArxiu)
arxiu.close()