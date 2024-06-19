#Exercici 1 
def generarArray(valor, vegades):
    array=[]
    try:
        for i in range(0,vegades):
            array.append(valor)
        return array
    except TypeError:
        return 'Paràmetre no permès'

#Exercici 2

def mediana(llista):
    llista=sorted(llista)
    if llista==[]:
        return 'Llista buida!'
    elif llista==[0]:
        return 0
    elif len(llista)%2==0:
        meitat=int((len(llista)/2))
        mitjanaLimitrofs=(llista[meitat-1]+llista[meitat])/2
        return(mitjanaLimitrofs)

    elif len(llista)%2!=0:
        total=len(llista)
        meitat=total/2
        meitat=int(meitat)
        meitatArredonida=round(meitat)
        return llista[meitatArredonida]


#Exercici 3

#No funcional, no cal ni mirar-lo
def replicar(llista, multiple):
    novaLlista=[]
    x=0
    while (x<multiple):
        print(x)
        for i in range(len(llista)):
            novaLlista.append(llista[i])
            novaLlista.append(llista[i])
        
        x+=1
    return novaLlista
