def preguntarAgenda():
    agendaAobrir=int(input("""Quina agenda voldras obrir?\n1-laboral\n2-personal\n>  """))
    selecioAgenda(agendaAobrir)
    
def selecioAgenda(numeroAgenda):
    global agendaSeleccionada
    if numeroAgenda == 1:
        agendaSeleccionada=open("laboral.txt")
        menu()
    elif numeroAgenda == 2:
        agendaSeleccionada=open("personal.txt")
        menu()
    else:
        print("\n\n",numeroAgenda,"No és una opció vàlida, siusplau escolleix-ne una de les següents:")
        preguntarAgenda()

def menu():
    global nomAgenda
    nomAgenda=agendaSeleccionada.name.split(".")[0]

    print()
    print("""Que vols fer?\n1-Veure contactes\n2-Trucar a un contacte\n3-Sortir""")
    opcioMenu=int(input("> "))

    if opcioMenu == 1:
        llistarAgenda()
    elif opcioMenu == 2:
        trucar()
    elif opcioMenu == 3:
        print("Sortint...")
    else:
        print("Siusplau, escolleix una opció vàlida")
        menu()

def llistarAgenda():
    print(f"\n################ Benvingut a l'agenda {nomAgenda} ################")
    print("Aquests són els teus contactes:")

    for linies in agendaSeleccionada.read().strip().split("\n"):#Llegim l'arxiu d'agenda amb .read(), treiem elements amb .strip(), i separem per salts de linia amb .split()
        linies=linies.strip().split(":")#Separem cada linia en llistes amb .split()
        nomContacte=linies[0]#guardem nom contacte
        numeroContacte=linies[1]#i numero contacte
        print(f"{nomContacte}  {numeroContacte}")


    print()
    #menu()

def trucar():
    numAtrucar=input("A quin contacte vols trucar=\n> ")
    print("Trucant a",numAtrucar)







preguntarAgenda()


#CarregarAgenda
#Menu
#Tancar
#LlistarAgenda
#Trucar

