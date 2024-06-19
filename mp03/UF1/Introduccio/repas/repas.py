'''
1.Crea un programa que demani números enters al usuari. Si l’usuari escriu 0, el programa es donarà per finalitzat i informarà 
al usuari del número màxim entrat, el número mínim i de quants números s’han entrat.

2.La successió de Finobacci es una successió on cada element es resultat de la suma dels dos anteriors. 
De tal forma que: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, etc.Crea un algorisme que demani una entrada n, 
l’algorisme pintarà fins a n elements de la successió de Fibonacci. Si n=2, el resultat serà 0, 1 si n=5 el resultat serà 0, 1, 1, 2, 3.

3.Crea un programa que vagi demanant entrades alfanumeriques al usuari, si aquestes entrades contenen la lletra A guardarles en un array. 
Si l’usuari escriu “exit” acabar el programa i mostrar les entrades que contenen la lletra A.
'''

menu=int(input('''Disme quin programa vols executar:  
1) Ex1 Num enters
2) Ex2 Num Finobacci
3) Ex3 Demanar entrades
'''))

match menu:
    case 1:

        llistaNumeros=[]
        introNum=1
        maxi=0
        minim=00
        cont=1

        while introNum!=0:
           introNum=int(input("Donam números per sumar:  "))
           if introNum==0:
               break
           else:        
                llistaNumeros.append(introNum)

        print("El resultat de la suma és:", sum(llistaNumeros))
        print("El número més gran de la llista és:",max(llistaNumeros))
        print("El número més petit de la llista és:",min(llistaNumeros))
        print("A la llista hi han",len(llistaNumeros),"números")





    case 2:
        numInputFibon=int(input("Fins a quin número vols veure la llista de Fibonacci:  "))
        suma=0
        fibo=[0,1]
        #mesura amb len quantitat de elements llista, suma l'ultim element i el penultim, quan la suma sigue mes gran que l'input break i printa la llista

    case 3:
        arrayparaules=[]
        
        while True:
            paraula=input("Disme paraules:  ").lower()
            if paraula == "exit":
                break
            if ('a' in paraula or 'A' in paraula):
                arrayparaules.append(paraula)
            else:
                continue
        print(arrayparaules)

        