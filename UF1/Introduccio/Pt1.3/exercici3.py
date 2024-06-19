#Crea un programa que demani una cadena de 4 caràcters (numèrics) a l'usuari, (com "1234") els emmagatzemi a una llista convertits en enters i imprimeixi 
#la suma dels números que la formen. Heu d'utilitzar una funció interna per a fer la suma.

numInici=input("Donam un número amb 4 caràcters ")
try:
    num1=int(numInici[0])
    num2=int(numInici[1])
    num3=int(numInici[2])
    num4=int(numInici[3])

    llista=[num1,num2,num3,num4]
    print("la suma dels números és: ", sum(llista))

except:
    print("Introdueïx números tros de burro.")


#Demana a l'usuari un número i afegeix-lo al final de la llista amb un mètode de llista.
num2=input("Donam un altre número  ")
try:
    llista.append(+int(num2))
    print("la llista amb el núero nou és:", llista)

except:
    print("No és un número")

#Ara elimina aquest número de la llista amb un mètode de llista.
llista.pop(4)
print("la llista sense el nou número és:", llista)

#Ordena la llista amb un mètode de llista.
llista.sort(reverse=False)
print("la llista ordenada és: ", llista)

#Mostra el seu número màxim i el seu mínim, extrets amb funcions internes.
print("L'element més gran de la llista és: ", max(llista))
print("L'element més petit de la llista és: ", min(llista))

#Calcula la mitjana aritmètica de la llista a partir de les funcions internes sum() i len().
print("La mitjana aritmètica de la llista és: ", sum(llista) / len(llista))
