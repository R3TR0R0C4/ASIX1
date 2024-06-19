"""gfitxer=open("prova.txt")
#print(gfitxer)
llista=[]

for linia in gfitxer:
    #print(linia,end="")
    #linia=linia.replace("\n","")
    llista.append(linia.strip())

print(llista)


contingut=gfitxer.read()
print(len(contingut))

cont=gfitxer.read
print(len(cont))



dicc={}
for linia in gfitxer:
    item=linia.strip().split(":")  
    dicc[item[0]]=item[1]
print(dicc)



contingut=gfitxer.read()

for items in contingut.strip().split("\n"):
    item=items.strip().split(":")
    dicc[item[0]]=item[1]

print(dicc)"""