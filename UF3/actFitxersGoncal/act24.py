import zipfile
extraciotest=""
arxiuOrginal=input("De quin arxiu vols veure el contingut?\n>")

arxiu=zipfile.ZipFile(arxiuOrginal,'r')

for nomArxiu in arxiu.namelist():
    if nomArxiu.endswith(".txt"):
        print("Extraient... ",nomArxiu)
        arxiu.extract(nomArxiu,'act24Sortida/')

arxiu.close()