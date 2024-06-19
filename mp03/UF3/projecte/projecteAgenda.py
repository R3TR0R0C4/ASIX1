try:
    from colorama import Fore, Style 
except:
    print("Hi ha hagut un error importat la llibrera colorama, comprova la que la seva instal·lació és correcta")
    exit()
try:
    from os import listdir, chdir, mkdir, getcwd, path
except:
    print("Hi ha hagut un error important la llibreria os, comprova la que la seva instal·lació és correcta")
    exit()

try:
    cwd=getcwd()
    rutaCarpetaAgendes=(cwd+"/fitxersAgenda")
    mkdir(rutaCarpetaAgendes)
except FileExistsError:
    pass
except:
    print("Hi ha hagut un problema amb la creació de la carpeta inicial, revisa que tinguis prous permisos amb el teu usuari.")
    exit()


def menuInicial():
    print("\n\n###############Contactes#####################\nQuè vols fer?\n1-Llistar agendes.\n2-Escollir agenda.\n3-Crear agenda.\n4-Sortir.")
    try:
        opcioMenu=int(input(f"{Fore.MAGENTA}> {Style.RESET_ALL}"))
        if opcioMenu == 1:
            print()
            llistarAgendes()
        elif opcioMenu == 2:
            print()
            escollirAgenda()
        elif opcioMenu == 3:
            print()
            creaAgenda()
        elif opcioMenu == 4:
            print("Sortint de l'agenda, fins a la pròxima!")
            exit()
        else:
            print(f"{Fore.RED}Opció no vàlida{Fore.RESET}")
            menuInicial()
    
    except ValueError:
        print(f"{Fore.RED}Valor no vàlid{Fore.RESET}")
        menuInicial()

def menuAgendaEscollida():
    print("\n##########Escull una opció:##########\n1-Llistar tots els contactes.\n2-Buscar un contacte.\n3-Trucar a un contacte.\n4-Afegeix un contacte\n5-Tornar al menú principal.\n6-Sortr.")
    opcioMenu=int(input(f"{Fore.MAGENTA}> {Style.RESET_ALL}"))
    if opcioMenu == 1:
        print()
        llistarTotsContactes()
    elif opcioMenu == 2:
        print()
        buscaContacte()
    elif opcioMenu == 3:
        print()
        gptTruca()
    elif opcioMenu==4:
        print()
        afegeixContacte()
    elif opcioMenu == 5:
        print("Tornant al menú inicial...")
        menuInicial()
    elif opcioMenu == 6:
        print("Sortint de l'agenda, fins a la pròxima!")
        exit()
    else:
        print("Opció no vàlida")

def llistarAgendes(saltarFinal=False):
    print("\n#####Aquestes són les agendes guardades#####")
    
    directori = getcwd()
    directoriPresent = path.basename(directori)

    if directoriPresent != "fitxersAgenda":
        chdir("fitxersAgenda")

    contingutFitxersAgeda = listdir()

    for idx, line in enumerate(contingutFitxersAgeda):
        agendes = line.split(".")[0]
        print(f"{idx + 1}. {agendes}")

    if not saltarFinal:
        menuInicial()


def escollirAgenda():
    llistarAgendes(True)
    global agendaSeleccionada
    global agendaAobrir

    agendas = listdir()
    positions = [str(i + 1) for i in range(len(agendas))]

    while True:
        print("Quina agenda vols obrir?")
        agendaAobrir = input(f"{Fore.MAGENTA}> {Style.RESET_ALL}")

        if agendaAobrir in positions:
            agendaSeleccionada = open(agendas[int(agendaAobrir) - 1])
            menuAgendaEscollida()
            break
        else:
            print("Selecciona una posició vàlida.")


def creaAgenda():
    directori = getcwd()
    directoriPresent = path.basename(directori)

    if directoriPresent != "fitxersAgenda":
        chdir("fitxersAgenda")

    print("Quin nom vols que tingui la nova agenda?")
    nomAgendaNova = input(f"{Fore.MAGENTA}>{Fore.RESET}")

    print(f"La nova agenda es dirà {nomAgendaNova}\nEstàs segur?\nSi o No")

    while True:
        checkAgendaNova = input(f"{Fore.MAGENTA}>{Fore.RESET}").capitalize()
        if checkAgendaNova == "Si":
            print("Creant Agenda...")
            agendaNova = open(f"{nomAgendaNova}.txt",'w')
            break
        elif checkAgendaNova == "No":
            print(f"Cancelant creació de l'agenda {nomAgendaNova}")
            return
        else:
            print("Assegura't d'utilitzar 'Si' o 'No'")
    menuInicial()

def llistarTotsContactes():
    try:
        for line in agendaSeleccionada:
            line=line.split(";")
            print(f"Nom: {line[0]}")
            print(f"Cognom: {line[1]}")
            print(f"Correu: {line[2]}")
            print("Números telèfon:",end="  ")
            for numero in line[3].strip().split(","):
                print(numero.strip(),end="   ")
            print("\n")
        agendaSeleccionada.close()    

    except FileNotFoundError:
        print(f"{Fore.RED}Error, nom d'agenda no vàlida, comprova que l'has introduït correctament.{Fore.RESET}\n\n")
        escollirAgenda()

    menuAgendaEscollida()

def buscaContacte(saltarPrintBuscar=False, saltarMenuFinal=False):
    global contacteAbuscar
    global recompteContactes
    
    contacteTrobat = 0
    recompteContactes = 0
    if not saltarPrintBuscar:
        print("Quin contacte vols buscar?")
    
    contacteAbuscar = input(f"{Fore.MAGENTA}> {Style.RESET_ALL}").lower()
    
    try:
        for line in agendaSeleccionada:
            line = line.split(";")
            if line[0].strip().lower() == contacteAbuscar:
                print(f"\n\n{Fore.CYAN}Nom: {Fore.RESET}{line[0]}\n{Fore.CYAN}Cognom: {Fore.RESET}{line[1]}\n{Fore.CYAN}Correu: {Fore.RESET}{line[2]}\n{Fore.CYAN}Números telèfon:{Fore.RESET}",end=" ")
                for numero in line[3].strip().split(","):
                    print(numero.strip(), end="  ")
                    
                contacteTrobat = 1
                recompteContactes += 1
            if not contacteTrobat:
                subMenuContacteNoTrobat()
        print("\n\n")
    except FileNotFoundError:
        print(f"{Fore.RED}Error, nom d'agenda no vàlida, comprova que l'has introduït correctament.{Fore.RESET}\n\n")
    if not saltarMenuFinal:
        menuAgendaEscollida()

def subMenuContacteNoTrobat():
    print(f"\n{Fore.RED}No s'ha trobat aquest contacte.{Fore.RESET}")
    print("Què vols fer?\n1-Buscar un altre contacte.\n2-Tornar enrere.")
    opcioSumMenuContacteNo=int(input(f"{Fore.MAGENTA}> {Style.RESET_ALL}"))
    if opcioSumMenuContacteNo==1:
        buscaContacte()
    elif opcioSumMenuContacteNo==2:
        menuAgendaEscollida()
    else:
        print(f"{Fore.RED}Opció no vàlida{Fore.RESET}")
        subMenuContacteNoTrobat()

def gptTruca():
    print("A quin contacte vols trucar? ")
    nomContacteAtrucar=input(f"{Fore.MAGENTA}>{Fore.RESET}").capitalize()
    print()

    contactesMatch=[]

    for line in agendaSeleccionada:
        fields=line.strip().split(';')
        if fields[0] == nomContacteAtrucar:
            contactesMatch.append(fields)

    if len(contactesMatch) == 0:
        print("No s'ha trobat cap contacte amb aquest nom.")
    elif len(contactesMatch) == 1:
        contact=contactesMatch[0]
        numbers=eval(contact[3])
        if len(numbers) == 1:
            print("El número de contacte per", nomContacteAtrucar, "és:", numbers[0])
        else:
            print("El contacte", nomContacteAtrucar, "te diversos números. Quin vols trucar?")
            for i, number in enumerate(numbers):
                print(f"{i+1}. {number}")
    else:
        print("S'han trobat múltiples contactes amb aquest nom. Els detalls dels contactes són:")
        for i, contact in enumerate(contactesMatch):
            print(f"{i+1}. {contact[0]} {contact[1]}")

        index=input("Quin contacte vols trucar?\n")
        index=int(index) - 1

        contact=contactesMatch[index]
        numbers=eval(contact[3])
        if len(numbers) == 1:
            print("El número de contacte per", nomContacteAtrucar, "és:", numbers[0])
        else:
            print("El contacte", nomContacteAtrucar, "te diversos números. Quin vols trucar?")
            for i, number in enumerate(numbers):
                print(f"{i+1}. {number}")

            num_index=input("Quin número vols trucar?\n")
            num_index=int(num_index) - 1
            print("El número de contacte per", nomContacteAtrucar, "és:", numbers[num_index])

def afegeixContacte():
    global agendaSeleccionada
    print(agendaSeleccionada.name)
    nomAgendaAobrir = agendaSeleccionada.name

    agendaSeleccionada.close()

    agendaSeleccionada = open(nomAgendaAobrir, "a")

    print("Dis-me quins són els detalls del contacte:")
    nom = input(f"{Fore.MAGENTA}Nom: {Fore.RESET}").capitalize()
    cognom = input(f"{Fore.MAGENTA}Cognom: {Fore.RESET}").capitalize()
    correu = input(f"{Fore.MAGENTA}Correu: {Fore.RESET}")

    numeros = []
    while True:
        entrada = input(f"{Fore.MAGENTA}Introdueïx el(s) números de telèfon (escriu 'fet' quan acabis): {Fore.RESET}")
        if entrada.lower() == 'fet':
            break
        if len(entrada) >= 9 and entrada.isdigit():
            numeros.append(int(entrada))
        else:
            print("Assegurat d'escriure un número de telèfon vàlid.")
    print(f"\nAquestes són les dades del nou contacte:\n{Fore.CYAN}Nom: {Fore.RESET}{nom}\n{Fore.CYAN}Cognom: {Fore.RESET}{cognom}\n{Fore.CYAN}Correu: {Fore.RESET}{correu}\n{Fore.CYAN}Números: {Fore.RESET}{numeros}")
    print(f"Vols guardar aquest contacte? (Si o No)")

    while True:
        checkContacteNou = input(f"{Fore.MAGENTA}>{Fore.RESET}").capitalize()
        if checkContacteNou == "Si":
            print("Afegint contacte...")
            contacteFormatat=(f"\n{nom};{cognom};{correu};{numeros}")
            agendaSeleccionada.write(contacteFormatat)
            agendaSeleccionada.close()
            break
        elif checkContacteNou == "No":
            print("Operació cancelada, Tornant al menú anterior.")
            agendaSeleccionada.close()
            menuAgendaEscollida()
            break
        else:
            print("Assegura't d'utilitzar 'Si' o 'No'")

    agendaSeleccionada=open(nomAgendaAobrir)
    menuAgendaEscollida()

menuInicial()