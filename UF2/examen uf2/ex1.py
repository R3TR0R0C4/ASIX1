#Crea una funció que donat un valor numéric i un número de vegades generi un array amb tantes vegades el valor com s’indica al parametre vegades. Temps estimat: 10 minuts
def crearArrayn(x,y):
    array=[]
    try:
        for i in range(0,y):
            array.append(x)
        return array
    except TypeError:
        return 'Paràmetre no permès'
print(crearArrayn("var",5))