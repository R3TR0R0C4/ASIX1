###----------------------------------------------------------------------------------------------------------------------------------------
# 1.Crea un programa que a partir de dos números et calculi la mitjana aritmètica

#declarem els dos nombres
n1=5
n2=3

#sumem els nombres
suma=n1+n2

#dividim els nombres
mitjana=suma/2

#printem mitjana
print ("Exercici 1:")
print ("La mitjana de", n1, "i", n2, "és", mitjana)
print ("")


###----------------------------------------------------------------------------------------------------------------------------------------
# 2.Crea un programa que a partir d’un pes i una altura et calculi l’índex de massa corporal.
#declarem pes (kg)
pes=80

#declarem altura (m)
altura=1.7

#fem l'altura al quadrat
alturacuadrat=altura ** 2

#calculem el BMI
bmi=pes/alturacuadrat

print ("Exercici 2:")
print ("El teu índex de massa corporal és:", bmi)
print ("")

###----------------------------------------------------------------------------------------------------------------------------------------
# 3.Crea un programa que a partir d’una temperatura en Celsius et calculi la temperatura en Fahrenheid.
#declarem els graus en ºc
graus=25.0

#calculem els graus farenheit amb aquesta fòrmula (grados centígrados × 9/5) +32
cAf=(graus * 9/5) + 32

print ("Exercici 3:")
print (graus, "graus celsius són", cAf, "én farenheit")
print ("")

###----------------------------------------------------------------------------------------------------------------------------------------
#Crea un programa que a partir d’una hora i uns minuts els calculi en segons.
#declarem hores i minuts
hores=3
minuts=15

#passem hores a segons
horesAsegons=(hores * 60) * 60

#passem minuts a segons
minutsAsegons=(minuts * 60)

#sumem les dos conversions
minutsIhoresAsegons=(horesAsegons + minutsAsegons)

#printem resultats
print ("Exercici 4:")
print (hores, "hores i", minuts, "minuts són", minutsIhoresAsegons, "segons")
print ("")