import os,zipfile
directoriActual=os.getcwd()

directori=input("Quin directori vols comprimir?\n>")

try:
    os.chdir(directori)
    arxius=os.listdir()
except FileNotFoundError:
    print("Asegura't d'introduïr una ruta vàlida")
except NameError: 
    print("Asegura't d'introduïr una ruta vàlida")

newZip=zipfile.ZipFile(f"{directoriActual}/act18Sortida.zip",'w')
print("\n\nComprimint fitxers...\n\n")
for fitxer in arxius:
    newZip.write(fitxer,compress_type=zipfile.ZIP_LZMA)

newZip.close()