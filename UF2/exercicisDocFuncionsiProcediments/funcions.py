#----------------Activitat 1----------------
def holaMon():
    print("Hola Món!")

#----------------Activitat 2----------------
def multi(x):
    print(x,"*",10,"és",int(x)*10)

#----------------Activitat 3----------------
def sumatori(x):
    print("El sumatori de",x,"és",sum(range(0,int(x)+1)))

#----------------Activitat 4----------------
def sumatoriRang(x,y):
    if x>y:
        print(0)
        
    else:
        print(sum(range(int(x),int(y)+1)))

#----------------Activitat 5----------------
def pitagoras(cateto1,cateto2,hipotenusa):

    if ((cateto1**2)+(cateto2**2) == hipotenusa**2):
        print("Triangle rectangle")
    else:
        print("El triangle no es rectangle")

#----------------Activitat 6----------------
def calcula_descompte(preu,descompte):
    final=preu-(preu*(descompte/100))
    print("Preu descomptat:", final,"€")

#----------------Activitat 8----------------
def conta_a(numA):
    numArecompte=int(0)
    for y in numA:
        if y == 'a':
            numArecompte=numArecompte+1
    print("El nombre de 'A' o 'a' en el text és: ",numArecompte)

#----------------Activitat 9----------------
def amagaTarjeta(nTarjeta):
    print("*"*(len(nTarjeta)-4)+nTarjeta[-4:])

#----------------Activitat 10----------------
def palindrom(paraula):
    paraula=paraula.replace(" ","")
    invertit="".join(reversed(paraula))
    if invertit==paraula:
        print(True)

#----------------Activitat 11----------------
def llistaNumeros():
    llistaNums=[]

    while True:
        numeros=input("Donam números  ")
        if numeros =="A":
            break
        elif numeros.isnumeric():
            llistaNums.append(int(numeros))

    print(llistaNums)

#----------------Activitat 12----------------
def maxArray():
    n=0
    numMax=[]
    max=-float('inf')
    while n<5:
        num=int(input("Donam números  "))
        n+=1
        numMax.append(int(num))

        if max<num:
            max=num
        
    print("Aquesta és la teva llista",numMax)
    print("Él número més gran és:",max)

#----------------Activitat 14----------------
def parellsImparells():
    llista=[]
    llistaPars=[]
    llistaImpars=[]
    sumaPars=0
    sumaImpars=0
    while True:
        llistaInputParells=input("Donam números, finalitza el programa introduïnt 'A':  ")
        if llistaInputParells=="A":
            break
        else: llista.append(int(llistaInputParells))

    for i in llista:
        if i%2==0:
            llistaPars.append(i)
            sumaPars+=i
        else:
            llistaImpars.append(i)
            sumaImpars+=i

    print("Aquests són els números Pars: ",llistaPars,"I aquest la súma d'ells:  ", sumaPars)
    print("Aquests són els números Impars: ",llistaImpars,"I aquesta la súma d'ells:  ", sumaImpars)

#----------------Activitat 15----------------
def numMinim():
    n=0
    numMin=[]
    min=-float('inf')
    


    n=0
    numMax=[]
    max=-float('inf')
    while n<5:
        num=int(input("Donam números  "))
        n+=1
        numMax.append(int(num))

        if max<num:
            max=num
        
    print("Aquesta és la teva llista",numMax)
    print("Él número més gran és:",max)

#----------------Activitat 16----------------
def inversColors():
    total=0
    colorsInicial=[255,24,90]
    resultat=[]
    print(colorsInicial)
    for i in colorsInicial:
        total+=int(i)
        resultat.append(total)
    print(resultat)

#----------------Activitat 17----------------
def contaVocals(fraseEntrada):
    diccionariResultat= {"A":0,"E":0,"I":0,"O":0,"U":0}

    for i in (fraseEntrada):
        #print(i)
        print(diccionariResultat[i])

#----------------Activitat 35----------------
def esTroba(llista,n):
    if len(llista)==0: return False #Si el nombre no està a la llista, aquesta s'agotarà, al agotar-se retornarà un False
    if llista[0]==n: return True #Si el primer nombre de la llista està 
    else: return esTroba(llista[1:],n)

#print(esTroba([4,5,6,7,8,9],5))
    
#----------------Activitat 36----------------
def sumaArray(llista):
    if len(llista)==0: return 0
    else: return llista[0]+sumaArray(llista[1:]) 

#print(sumaArray([1,2,3,4,5]))
    
#----------------Activitat 37----------------
def sumatori(a,b):
    if a>b:a,b=b,a
    if a==b: return a
    else: return a+sumatori(a+1,b)
    
#print(sumatori(3,8))
    

#----------------Activitat 38----------------
def replicar(llista,n):
    if not llista or n<2: return []
    else: return [llista[0]]*n+replicar(llista[1:],n)

#print(replicar([1,2,5,7],3))
    
#----------------Activitat 39----------------
def esTroba(text,busca):
    if len(text)==0: return False
    if text[0:len(busca)]==busca: return True
    else: return esTroba(text[1:],busca)

#print(esTroba("un tete a tete con Tete","te"))


#----------------Activitat 40----------------
def posicions_de(text,busca,index=0):
    if index==len(text):
        return []
    if text[index:index+len(busca)]==busca:
        return [index]+posicions_de(text,busca,index+1)
    else: return posicions_de(text,busca,index+1)


#print(posicions_de("un tete a tete con Tete","te"))
    
#----------------Activitat 37 modificada----------------
def sumatoriModClase(a=0,b=0):
    if a>b:a,b=b,a
    if a==b: return a
    else: return a+sumatori(a+1,b)

print(sumatoriModClase(8))