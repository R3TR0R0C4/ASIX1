"""numUser=int(input("Donam un usuari:  "))

while (numUser>0):
    print(numUser)
    numUser-=1

print("boom")"""



"""llistaNumeros=[]
introNum=1
while (introNum!=0):
    introNum=int(input("Donam números per sumar:  "))
    llistaNumeros.append(introNum)
print("El resultat de la suma és:", sum(llistaNumeros))"""

'''nota=99
while(nota<0 and nota>10):
    nota=float(input("Donam una nota entre 0 i 10:  "))

if (nota<0 or nota>10): #Primer de tot mirarém si la nota esta dintre del rang de 0 a 10, si està fora d'aquest rang llança un error
    print("Nota nó valida, recorda notes de 0-10")
else:
    if nota<5: #si és menor a 5 printem insuficient
        print("Insuficient")
    elif nota>=5 and nota<7: #si està o és 5 i és menor de 7 printem Suficient
        print("Suficient")
    elif nota>=7 and nota<8: #si està o és 7 i és menor de 8 printem Bé
        print("Bé")
    elif nota>=8 and nota<9:
        print("Notable")
    elif nota>=9 and nota<=10:
        print("Excelent")
    else:
        print("Nota no vàlida")'''

#Ennumerar elements d'una llista amb loops
"""
llista=["a","b","c","d"]
numllista=-1

while(numllista<len(llista)-1):
    numllista+=1
    print(llista[numllista])
    """

#Programa d'ABBA amb loops
"""llistaNoms=["Astolfo","Bartolomeo","Benjamin","Arnau"]
numllista=-1

while(numllista<len(llistaNoms)-1):
    numllista+=1
    print(llistaNoms[numllista][0],end="")
    
print("") """


#Taula de multiplicar
"""numUser=int(input("Donam un número:  "))
x=0

while(x<11):
    print("La multiplicació de ",numUser, "Per ",x, "És", numUser*x)
    x+=1"""

"""while True:
    linea= input(">")
    if linea[0] == '#':
        continue
    if linea == 'fi':
        break
    print(linea)
print('Acabat!')"""


"""diccionari={"Pellisa":22,"Gonçal":44,"Aurora":22, "Victor":18}

for nom in diccionari:
    #print(nom,"té",diccionari[nom],"anys")
    print(nom)

print(diccionari.keys())
print(diccionari.values())"""




"""resultat=0
for numero in [4,65,78,56,78]:
    resultat+=numero

print(resultat)"""

"""for num in (range(1,11)):
    print(num)"""


numUser=int(input("Donam un número:  "))
x=0

for x in (range(1,11)):
    print("La multiplicació de ",numUser, "Per ",x, "És", numUser*x)