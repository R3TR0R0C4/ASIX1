#Crea un script que llegeixi el contingut de fruites (on cada fruita ocupara una línia) i ho escrigui en un nou fitxer anomenat fruites2.txt.
lecturaFitxer=open("act1.txt")
fitxerNou=open("act6.txt",mode="w")

for linia in lecturaFitxer:
    print(linia.strip())
    fitxerNou.write(linia)
    