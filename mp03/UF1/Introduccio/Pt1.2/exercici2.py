#Exercici 1 Crea un programa que a partir d'una cadena de 4 caràcters (numèrics) preguntada a l'usuari, (com "1234") imprimeixi la suma dels números que la formen. 
#Teniu en compte que només s'ha d'utilitzar un input, estem treballant les cadenes.
'''
num=(input("donam un número de 4 de llargada \n"))
print("la cadena és numèrica "+str(num.isnumeric() ))
suma=(+int(num[0]) + +int (num[1]) + +int(num[2]) + +int(num[3]))
print("el resultat és",suma)
'''

#Exercici 2 Consulta els mètodes "built-in" que teniu disponibles per a cadenes i crea un programa que a partir d'una frase donada per l'usuari calculi:
#Número de caràcters.
frase=(input("donam una frase: "))
print("La teva frase té ",len(frase),"caràcters")

#Número de paraules.
print("La teva frase té ",len(frase.split()), "paràules")
print()

#Frase  amb totes les paraules en majúscula.
print("la teva frase en majuscules és")
print(frase.upper())
print()

#Frase  amb totes les paraules en minúscula.
print("la teva frase en minuscules és")
print(frase.lower())
print()

#Preguntat un caràcter a l'usuari retorni la posició de la primera coincidència trobada a la frase.
primerCaracter=input("quin és el primer caràcter que vols buscar:  ")
print("el caràcter que busques està en la posició: ", frase.find(primerCaracter))
print()

#Preguntat un caràcter a l'usuari retorni el número de coincidències trobades a la frase.
segonCaracter=input("quin és el caràcter del que vols fer un recompte?  ")
print("el caràcter ", segonCaracter, " es repeteix",frase.count(segonCaracter), "vegades")
print()

#Mostri el número de vocals del text (has d'optimitzar al màxim aquest codi!!).
frase=frase.lower() #passem variable frase a frase en minuscula
print("El nombre de vocals de la fràse són:",frase.count("a")+frase.count("e")+frase.count("i")+frase.count("o")+frase.count("u"))
print()

