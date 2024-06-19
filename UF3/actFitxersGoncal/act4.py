llegir=open("act4.txt")
suma=0
for numero in llegir.read().strip().split("\n"):
    try:
        suma+=int(numero)
    except ValueError:
        continue

print(suma)