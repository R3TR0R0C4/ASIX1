#Crea un script que llegeixi el contingut de fruites (on cada linia te un conjunt de fruites separades per ;) i ho escrigui en un nou fitxer anomenat fruites2.txt posant una fruita a cada línia.

lectura=open("act2.txt")
arxiu2=open("fruites2.txt",mode="w")
for line in lectura:
    arxiu2.write(line.replace(";","\n"))
