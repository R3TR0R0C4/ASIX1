#Pe: replicar([1,3,3,5], 2) = [1,1,3,3,3,3,5,5]

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
        
print(replicar([1,2,3], 5))