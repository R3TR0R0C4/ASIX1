#demanem el dni a l'usuari
ndni=input("Donam el número del DNI (8 números 1 lletra)  ")

#separem els números del dni a una variable
cadenaNumeros=int(ndni[0:8])

#separem la lletra del dni a una altra variable i passem la lletra a majuscula per evitar fallades
lletra=ndni[8].upper()

#fem la divisio per obtenir el resto per la lletra
divisio=cadenaNumeros % 23

#declarem les lletres corresponents a cadascun dels restos de cada numero
lletres="TRWAGMYFPDXBNJZSQVHLCKE"

#declarem la variable "lletraFinal" i la comparem a l'array anterior segons el resultat de la divisió
lletraFinal=lletres[divisio]

#printem si la variable lletraFinal(comparació a la linia 17) és igual a lletra(variable que hem separat a la linia 8)
print("La lletra és correcta? ", lletraFinal == lletra)