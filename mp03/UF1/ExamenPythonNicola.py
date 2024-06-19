#----------------------------------------------TASCA 1---------------------------------------------- Feta/Funcional
"""ingredients={"pebrot":[2,True], "ceba":[1.5,True], "bacon":[2,False], "peperoni":[1.8,False]}
preuBasePizza=6
preuIngredients=0
print(ingredients.keys())
preguntaPizza=input("pizza? ")



for i in preguntaPizza.split("+"):
    preuIngredients=preuIngredients+ingredients[i][0]
preuFinal=preuIngredients+preuBasePizza


vip=input("Tens tarjeta vip?  ")
if vip == "si":
    print("El preu final de la pizza és",preuFinal-(preuFinal*0.1),"€")
else:
    print("El preu final de la pizza és",preuFinal)"""


#----------------------------------------------TASCA 2---------------------------------------------- mitat/noFuncional
"""

ingredients={"pebrot":[2,True], "ceba":[1.5,True], "bacon":[2,False], "peperoni":[1.8,False]}
preuBasePizza=6
preuIngredients=0
preuFinal=0
preguntaPizza=""
llista=[]
print(ingredients.keys())
#print(ingredients["pebrot"][1])


while True:
    preguntaPizza=input("pizza? ").lower()
    if preguntaPizza!="fi":
        for i in preguntaPizza.split("+"): #Recorrem la pregunta i la separem segons els signes de +
            preuIngredients=preuIngredients+ingredients[i][0] #Sumem els ingredients que l'usuari introdueix a l'input amb el cost de l'ingredient al diccionari
            preuFinal=preuIngredients+preuBasePizza
            if ingredients[i][1] == False: # si el camp resulta false al diccionari printem que no es apte per vegans i trenquem loop
                print("No apte per vegans")
                break
            print(preuFinal)
        preuFinal=preuFinal+preuFinal
    else:


        vip=input("Tens tarjeta vip?  ")
        if vip == "si":
            print("El preu final de la pizza és",preuFinal-(preuFinal*0.1),"€")
            break
        else:
            print("El preu final de la pizza és",preuFinal)
            break

"""

#----------------------------------------------TASCA 3---------------------------------------------- Feta/Funcional

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
my_list = [6, 7, 8, 1, 5, 6, 9, 2, 4, 6]

for y in my_list:
    if y in my_list:
        my_list.pop(y)
print("\nla llista sense repeticions:")
print(sorted(my_list))