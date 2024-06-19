import os,zipfile
directoriActual=os.getcwd()
mida=5

directori=input("Quin directori vols comprimir?\n>")

try:
    os.chdir(directori)
    arxius=os.listdir()
except FileNotFoundError:
    print("Asegura't d'introduïr una ruta vàlida")
except NameError: 
    print("Asegura't d'introduïr una ruta vàlida")

newZip=zipfile.ZipFile(f"{directoriActual}/act21Sortida.zip",'w')
print("\n\nComprimint fitxers...\n\n")
for fitxer in arxius:
    mida=os.stat(fitxer).st_size
    if mida>mida*1024*1024:
        newZip.write(fitxer,compress_type=zipfile.ZIP_LZMA)

newZip.close()
