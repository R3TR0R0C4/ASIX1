"""numero=int(input("Dona'm un número:   "))
for multi in range (1,11):
    print(numero,"*",multi,"=",multi*numero)"""


#----------------------------------------------------
diccionari={"user1":"password","user2":"macarrons"}

"""intent=""
contrasenya="password"
x=0

while x<3:

    intent=input("Dis-me la contrasenya:  ")
    x+=1
    if intent==contrasenya:
        print("Has acertat la contrasenya")
"""
"""x=0
intent=""
while x<3:
    usuari=input("Dis-me l'usuari':  ")
    
    if usuari not in diccionari:
        print("Usuari Incorrecte")
        continue
    contrasenya=input("Dis-me la contrasenya:  ")
    x+=1
    
    if usuari in diccionari and diccionari[usuari] == contrasenya:
        print("Usuari correcte")
        break
    else:
        print("Aquesta contrasenya és incorrecta")"""

casa={'dormitori':[2,2],'menjador':[3,4],'bany':[2,4]}
for i in casa.keys():
    print (i)
"""hab=input("Quina habitacio vols consultar:  ")
print("La superficie es",hab,"és",casa[hab][0]*casa[hab][1],"m²")"""
habCombi=input("Quines habitacions vols consultar ")
habCombi=habCombi.split(",")
area=0

for hab in habCombi:
    area+=casa[hab][0]*casa[hab][1]

print(area,"m^2")

