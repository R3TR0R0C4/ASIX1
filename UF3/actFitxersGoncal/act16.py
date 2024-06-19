import os

for carpeta in os.listdir("/etc"):
    if os.path.isdir(f"/etc/{carpeta}"):
        print(carpeta)