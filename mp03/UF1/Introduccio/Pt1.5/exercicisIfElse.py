"""
---Tasca1: (Opció del menu 1 Nota)
Escriu un programa que sol·liciti una puntuació entre 0 i 10. Si la puntuació és fora d'aquest rang, mostra un missatge d'error. Si la puntuació està entre 0 i 10, 
mostra la qualificació usant la taula següent:
Puntuació Qualificació
>= 9 Excel·lent
>= 8 Notable
>= 7 Bé
>= 5 Suficient
< 5 Insuficient
Bateria de proves:
Introduïu puntuació: 9.5 -> Excel·lent
Introduïu puntuació: perfecte -> Puntuació incorrecta
Introduïu puntuació: 11 Puntuació -> Incorrecta
Introduïu puntuació: 7.5 -> Bé
Introduïu puntuació: 0.5 -> Insuficient

---Tasca 2: (Opció del menu 2 Anys)
Escriu un programa que demani l'any actual i un altre any qualsevol. El resultat ha de mostrar quants anys han passat des de l'any introduït o quants anys falten.
Ara milloreu el programa per a fer que quan la diferència sigui només d'un any, ens digui que només falta un any.

---Tasca 3: (Opció del menu 3 Joc de daus)
Creeu un joc de daus on es generi una tirada per a cadascun dels jugadors, quan escriguin la paraula "tirar" en un input i posteriorment es mostri el resultat de la partida.
Podeu utilitzar la funció randint() de la llibreria random:
Exemple d'ús:
import random
numero = random.randint(1, 6)
"""


import random

menu=int(input('''Disme quin programa vols executar:  
1) Exercici 1 Nota
2) Exercici 2 Anys
3) Exercici 3 Joc de daus
'''))


match menu:
    case 1:
        try:
            nota=float(input("Donam una nota entre 0 i 10:  "))

        except ValueError:
            print("Nota no vàlida")

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
                print("Nota no vàlida")



    case 2: #Comparar anys
        try:
            anyActual=+int(input("Disme a quin any estem:  "))
            anyComparar=+int(input("Disme un any qualsevol:  "))
        except:
            print("Anys introduïnts no correctes.")

        if (anyActual>anyComparar):
            anyTemp=anyActual-anyComparar
            print("Falten", anyTemp, "anys")
        elif (anyActual<anyComparar):
            anyTemp=anyComparar-anyActual
            print("Han passat", anyTemp, "anys")
        else:
            print("l'any és el mateix")
 

    case 3:
        numeroDauAleatu1=0
        numeroDauAleatu2=0
        numeroDauAleatu3=0

        jugador1=input("Jugador 1, Posa 'tirar' per iniciar:  ").lower()

        if (jugador1=="tirar"):
            numeroDauAleatu1 = random.randint(1, 6)
            print("Jugador 1, el teu número és:", numeroDauAleatu1)

        else:
            print("No has posat 'tirar'")


        jugador2=input("Jugador 2, Posa 'tirar' per iniciar:  ").lower()
        

        if (jugador2=="tirar"):
            numeroDauAleatu2 = random.randint(1, 6)
            print("Jugador 2, el teu número és:", numeroDauAleatu2)

        else:
            print("No has posat 'tirar'")
        
        jugador3=input("Jugador 3, Posa 'tirar' per iniciar:  ").lower()

        if (jugador3=="tirar"):
            numeroDauAleatu3 = random.randint(1, 6)
            print("Jugador 3, el teu número és:", numeroDauAleatu3)

        else:
            print("No has posat 'tirar'")


        if (numeroDauAleatu1>numeroDauAleatu2 and numeroDauAleatu1>numeroDauAleatu3):
            print("Guanya el jugador 1")
        elif (numeroDauAleatu2>numeroDauAleatu1 and numeroDauAleatu2>numeroDauAleatu3):
            print("Guanya el jugador 2")
        elif (numeroDauAleatu3>numeroDauAleatu1 and numeroDauAleatu3>numeroDauAleatu2):
            print("Guanya el jugador 3")
        else:
            print("Heu empatat")
