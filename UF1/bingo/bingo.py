import random
# Inicialitza llistes buides pels cartons dels jugadors
cartolina_jugador1 = []
cartolina_jugador2 = []

# Crea una llista amb el rang de 1-49 pel bombo
bombo = list(range(1, 50))

# Itera sobre les columnes dels cartons (5 columnes)
for columna in range(5):
    # Calcula el rang de números per a la columna actual
    rang_inici = columna * 10 + 1
    rang_final = columna * 10 + 9

    # Genera una columna aleatòria sense repeticions i afegeix-la al cartó del Jugador 1
    columna_cartolina_jugador1 = random.sample(list(range(rang_inici, rang_final + 1)), 5)
    cartolina_jugador1.append(columna_cartolina_jugador1)

    # Incrementa el rang per a la següent columna
    rang_inici += 10
    rang_final += 10

    # Genera una columna aleatòria sense repeticions i afegeix-la al cartó del Jugador 2
    columna_cartolina_jugador2 = random.sample(list(range(rang_inici, rang_final + 1)), 5)
    cartolina_jugador2.append(columna_cartolina_jugador2)

# Bucle principal del joc

while True:
    # Espera que l'usuari premi Enter per obtenir un número aleatori
    input("Prem Enter per obtenir un número aleatori...")

    # Aleatoritza l'ordre del bombo
    random.shuffle(bombo)

    # Retorna un número i elimina'l del bombo
    numero_resultant = bombo.pop()

    # Mostra el número que acaba de ser cridat
    print("\nNúmero cridat és:", numero_resultant)

    # Verifica si el número cridat està al cartó del Jugador 1
    for fila in range(3):
        for columna in range(5):
            if cartolina_jugador1[fila][columna] == numero_resultant:
                cartolina_jugador1[fila][columna] = "X"

    # Verifica si el número cridat està al cartó del Jugador 2
    for fila in range(3):
        for columna in range(5):
            if cartolina_jugador2[fila][columna] == numero_resultant:
                cartolina_jugador2[fila][columna] = "X"

    # Comprova si el jugador 1 ha guanyat
    if all(isinstance(x, str) for x in cartolina_jugador1[fila]):
        print("----Ha guanyat el Jugador 1!!!-----")
        break
    elif all(isinstance(x, str) for x in cartolina_jugador2[fila]):
        print("----Ha guanyat el Jugador 2!!!-----")
        break

        
    # Mostra els cartons actuals
    print("\n === Cartó Jugador 1 ===")
    for fila in range(3):
        print(cartolina_jugador1[fila])
    print("\n === Cartó Jugador 2 ===")
    for fila in range(3):
        print(cartolina_jugador2[fila])

###Falta: sol·lucionar que quan un jugador faci linia, el programa  retorni que l'ha completat