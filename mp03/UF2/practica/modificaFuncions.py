#Establim un valor per defecte
#Amb el n2=0 establim el valor per defecte de n2, així si no passem dos arguments encara funcionaria
"""def suma(list):
    total=0
    for i in list:
        total+=i
    return total

print(suma([3,4,5,6]))
"""
#Amb un * detras de la variable de funcio es transformara en un tipus similar a una llista
"""def suma(nom,*list):#amb la variable nom rebrém la primera variable ("Pepe") i després enviarem el que sigui que hi ha quan cridem la funcio
    total=0
    for i in list:
        total+=i
    return nom+ str(total)

print(suma("Pepe",3,4,5,6))"""

"""def pizza(base,*ingredients):
    total=0
    for i in ingredients:
        total+=i
    print("El preu base és" ,base,"€")
    print("Has escollit", len(ingredients),"ingredients, amb un preu de",sum(ingredients),"€")
    print("El preu final és de",base+total,"€")

pizza(6,3,4,5,6)"""

"""def pizza(base,**ingredients):
    preuIngredients=0
    print("Has escollit els ingredients:")
    for i,p in ingredients.items():
        print(i,"amb un preu de",p,"€")        
        preuIngredients+=p
    print("El preu dels total dels ingredients és de: ",preuIngredients,"€")
    print("El preu de la base és de ",base)
    print("El preu total és de",preuIngredients+base)

pizza(6,ceba=2,pebrot=6,bacon=3)"""


