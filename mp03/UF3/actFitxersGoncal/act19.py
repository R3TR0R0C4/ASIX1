import os,zipfile
directoriActual=os.getcwd()

directori=input("Quin directori vols comprimir?\n>")

try:
    os.chdir(directori)
    arxius=os.listdir()
except:
    print("Asegura't d'introduïr una ruta vàlida")


newZip=zipfile.ZipFile(f"{directoriActual}/act19Sortida.zip",'w')
print("\n\nComprimint fitxers...\n\n")
for fitxer in arxius:
    if os.path.isfile(fitxer):
        newZip.write(fitxer,compress_type=zipfile.ZIP_LZMA)

newZip.close()