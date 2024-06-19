#Diccionaris
'''
diccionari={"dog":"perro","cat":"gato"} #declarar un diccionari amb items dintre
diccionari["snake"]="serpiente" #Afegim l'item snake=serpiente
print(diccionari)
print(diccionari["dog"])
'''
notes={"MP01":[5,4,5],"MP02":[2,7,8],"MP03":[1,6,4],"MP04":[6,5,6]}

nouModul=input("Disme el mòdul que vols afegir MP05, MP06...  ").upper()
novesNotesModul=input("Dònam les notes del mòdul separades per comes  ").split(',')

llistaINT=[int(novesNotesModul[0]),int(novesNotesModul[1]),int(novesNotesModul[2])]

notes[nouModul]=llistaINT
print(notes)






modul=input("Quin modul vols consultar? ")
try:
    uf=int(input("Quina uf vols consultar? 1,2 o 3? "))-1

    print("La nota de la UF", uf+1, "del módul", modul, "és un", notes["MP0"+modul][uf])
except:
    print("Error en la uf introduïda")

print("La mitjana del módul",modul,"És un",sum(notes["MP0"+modul])/len(notes["MP0"+modul]))


'''
pregunta=input("Quina nota vols consultar? 1,2,3...?  ").upper()
try:<
    pregunta="MP0"+pregunta
    print("La nota de", pregunta, "és un", notes[pregunta])
except:
    print("el nombre introduït no és correcte")

try:
    afegirModul="MP0"+input("Quin modul vols afegir? 1,2...  ")
    afegirNota=input("Quina nota li vols posar?  ")
    afegirNota=+float(afegirNota)
    notes[afegirModul]=afegirNota
    print("Les notes són", notes)

except ValueError:
    print("La nota introduïda no és vàlida")
'''