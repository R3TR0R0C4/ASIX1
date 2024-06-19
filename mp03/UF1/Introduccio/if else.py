'''
if (5==5): #Codi a avaluar

    print("Funciona")
    #Codi que executem en cas de ser true

else:
    print("No funciona")
    #Codi que executem en cas de ser false

'''

"""
#Endivina el número secret
secret="6"
endivina=int(input("Endivina el número secret:   "))

if (endivina==secret):
    print(endivina,"és el número secret")

elif (endivina<secret):
    print("El número  que has triat és mes petit que el secret")

else:
    print("El número que has triat és més gran que el secret")
"""


"""
#Elif's
print('''
(1) Afegeix
(2) Esborra
(3) Edita
      
''')

opcio=input("Tria una opció:  ")


if (opcio=="1"):
    print("Has triat Afegeix")
elif (opcio=="2"):
    print("Has triat Esborra")      
elif (opcio=="3"):
    print("Has triat Edita")
else:
    print("no has triat cap opció del menú")

"""

"""
#Match (Switchcase amb javascript)

print('''
(1) Afegeix
(2) Esborra
(3) Edita
''')

x=int(input("Disme l'opció que vols:  "))
match x:
    case 1:
        print("Has escollit Afegeix")
    case 2:
        print("Has escollit Esborra")
    case 3:
        print("Has escollit Edita")
    case _:
        print("Opció no vàlida")
"""

#Activitat notes d'alumnes
nota=int(float(input("Disme la nota de l'alumne:  "))) #Passem primer a float per arrodonir, i després a int per treure el decimal

    
match nota:
    case 0|1|2|3|4:
        print("Nota Insuficient")
    case 5|6:
        print("Suficient")
    case 7|8:
        print("Notable")
    case 9|10:
        print("Excelent")
    case _:
        print("Valor introduït no vàlid")
