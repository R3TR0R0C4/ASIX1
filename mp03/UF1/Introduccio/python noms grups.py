#Demanem els cuatre noms per separat
nom1=input("Donam el primer nom:  ").upper()
nom2=input("Donam el segon nom:  ").upper()
nom3=input("Donam el tercer nom:  ").upper()
nom4=input("Donam el quart nom:  ").upper()

#posem els noms en una llista
llistatNoms=[nom1,nom2,nom3,nom4]

#printem el els items de la llista amb el primer caràcter del item indicat de la llista
print("El nom del grup és: "+llistatNoms[0][0]+llistatNoms[1][0]+llistatNoms[2][0]+llistatNoms[3][0])


#-------------------------------------------------------------------------------------------------------------------------------------------------


#demanem els noms dels membres:
noms=input("Donam els noms dels integrants separats amb espais:  ")

#separem els noms i els posem a una variable llista
llistatNoms2=noms.split()

#printem el resultat amb les inicials de cada item de la llista anterior
print("El nom del grup és: "+llistatNoms2[0][0]+llistatNoms2[1][0]+llistatNoms2[2][0]+llistatNoms2[3][0])