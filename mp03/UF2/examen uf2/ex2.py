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
        """total=len(llista)
        meitat=int(total/2)
        mitatArredonida=round(meitat)
        return mitatArredonida+1"""
    
        total=len(llista)
        meitat=total/2
        meitat=int(meitat)
        meitatArredonida=round(meitat)
        return llista[meitatArredonida]
print(mediana([-100000,1000000000000, 1]))