llegir=open("act3.txt")

suma=int(0)

for numero in llegir.read().strip().split("\n"):
    numero=int(numero)
    suma+=numero

print(suma)