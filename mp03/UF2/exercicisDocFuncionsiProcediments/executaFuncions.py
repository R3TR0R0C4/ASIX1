import funcions

print('''
Quina activitat de funcions vols executar?

(1) Activitat 1 | Hola Mon
(2) Activitat 2 | Multiplicacio
(3) Activitat 3 | Sumatori
(4) Activitat 4 | Sumatori rang
(5) Activitat 5 | Pitagoras
(6) Activitat 6 | Descompte
(8) Activitat 8 | Compta As
(9) Activitat 9 | Amaga Tarjeta
(10) Activitat 10 | Palindrom
(11) Activitat 11 | Conta Nums
(12) Activitat 12 | Número més gran
(14) Activitat 14 | Parells i imparells
(16) Activitat 16 | Inverteix valors RGB
      
 ''')

menu=int(input("Quines funcions vols executar:  "))
match menu:
    case 1:
        funcions.holaMon()
    
    case 2:
        numAct2=input("Disme un numero a multiplicar: ")
        funcions.multi(numAct2)
    
    case 3:
        numAct3=input("Disme quin numero vols el sumatori: ")
        funcions.sumatori(numAct3)
        
    case 4:
        num1Act4=input("Disme el primer numero: ")
        num2Act4=input("Disme el segon número: ")
        funcions.sumatoriRang(num1Act4,num2Act4)
    
    case 5:
        num1Act5=int(input("catet 1: "))
        num2Act5=int(input("catet 2: "))
        num3Act5=int(input("Hipotenusa: "))

        funcions.pitagoras(num1Act5,num2Act5,num3Act5)
    case 6:
        preu=int(input("Preu: "))
        descompte=int(input("Descompte: "))
        funcions.calcula_descompte(preu,descompte)

    case 8:
        text=input("Dis-me el text a contar: ").lower()
        funcions.conta_a(text)

    case 9:
        noTarjeta=input("Dona'm el nº de tarjeta ")
        funcions.amagaTarjeta(noTarjeta)

    case 10:
        palindrom=input("dona'm una paraula ")
        funcions.palindrom(palindrom)

    case 11: 
        funcions.llistaNumeros()

    case 12:
        funcions.maxArray()
    
    case 14:
        funcions.parellsImparells()

    case 16:
        funcions.inversColors()

    case 17:
        funcions.contaVocals(input("Donam una frase:  ").upper())

    case 35:
        funcions.esTroba(input("Donam un número: "))
    case _:
        print("Opció no vàlida")