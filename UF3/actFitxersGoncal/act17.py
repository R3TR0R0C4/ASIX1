import os

for carpeta in os.listdir("/etc"):
    if os.path.isdir(f"/etc/{carpeta}"):
        print(carpeta,"és una carpeta")
    elif os.path.isfile(f"/etc/{carpeta}"):
        print(carpeta,"és un arxiu")
    else:
        print(carpeta,"és un arxiu especial")