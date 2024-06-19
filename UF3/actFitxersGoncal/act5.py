fitxer=input("Quin fitxer hem d'obrir (act1.txt):   ")
try:
    llegir=open(fitxer)
    for linia in llegir:
        print(linia.strip())
except:
    print("El nom del fitxer no existeix: missing.txt")

