#bombo=list(range(50)) # creem variable bombo i li assignem una llista amb el rang de llista de 0-49
#bombo=list(range(1,50)) # creem variable bombo i li assignem una llista amb el rang de llista de 1-49
#bombo=list(range(0,101,2)) # creem variable bombo i li assignem una llista amb el rang de llista de 0-100 i configurem el salt a 2.


#Bombo del bingo:
'''
import random

bombo=list(range(1,50)) # creem una llista amb el rang de 0-49
random.shuffle(bombo) # barreja els números dintre la llista bombo

#print(bombo.pop()) #borrem l'ultim número de la llista i el retornem

for bola in bombo:
    print(bola,end=" ")#printem el número de la variable bola, i al final declarem end=" " per que no faci un salt de linia (\n) i faci un espai
    
    
    
    #input()#esperem a l'input (enter) per continuar el codi de printar

'''
'''
llistes=[[4,6,9],[3,5,4],[3,2,1]]
for llista in llistes:
    for num in llista:
        print(num)'''

llista=[[4,6,9],[3,5,4],[3,2,1]]

x=0
y=0

while(x<len(llista)):
    while(y<len(llista[x])):
        print(llista[x][y])
        y+=1
    y=0
    x+=1
    