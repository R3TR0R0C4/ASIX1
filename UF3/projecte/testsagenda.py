from os import listdir, chdir, getcwd

"""chdir("fitxersAgenda")
contingutFitxersAgeda=listdir()

for line in contingutFitxersAgeda:
    line=line.split(".")
    agendes=line[0]
    print(agendes)"""


"""cwd=getcwd()
print(cwd)
cwd=(cwd+"/fitxersAgenda")
print(cwd)"""

"""llista=[123123123,123123123]
print(type(llista[0]))"""



def gptTruca():
    print("A quin contacte vols trucar? ")
    nomContacteAtrucar = input(f"{Fore.MAGENTA}>{Fore.RESET}").capitalize()

    matching_contacts = []

    for line in agendaSeleccionada:
        fields = line.strip().split(';')
        if fields[0] == nomContacteAtrucar:
            matching_contacts.append(fields)

    if len(matching_contacts) == 0:
        print("No s'ha trobat cap contacte amb aquest nom.")
    elif len(matching_contacts) == 1:
        print("El número(s) de contacte per", nomContacteAtrucar, "és:", matching_contacts[0][3])
    else:
        print("S'han trobat múltiples contactes amb aquest nom. Si us plau, introdueix el cognom: ")
        cognom = input(f"{Fore.MAGENTA}>{Fore.RESET}").capitalize()
        found = False
        for contact in matching_contacts:
            if contact[1] == cognom:
                print("El número(s) de contacte per", nomContacteAtrucar, cognom, "és:", contact[3])
                found = True
                break
        if not found:
            print("No s'ha trobat cap contacte amb aquest cognom.")

    
    
    
    print("A quin contacte vols trucar? ")
    nomContacteAtrucar = input(f"{Fore.MAGENTA}>{Fore.RESET}").capitalize()
    
    matching_contacts = []
    
    for line in agendaSeleccionada:
        fields = line.strip().split(';')
        if fields[0] == nomContacteAtrucar:
            matching_contacts.append(fields)
    
    if len(matching_contacts) == 0:
        print("No s'ha trobat cap contacte amb aquest nom.")
    elif len(matching_contacts) == 1:
        print("El número(s) de contacte per", nomContacteAtrucar, "és:", matching_contacts[0][3])
    else:
        print("S'han trobat múltiples contactes amb aquest nom. Els detalls dels contactes són:")
        for contact in matching_contacts:
            print(contact[0], contact[1])
    
        print("Si us plau, introdueix el cognom per seleccionar el contacte:")
        cognom = input(f"{Fore.MAGENTA}>{Fore.RESET}").capitalize()
    
        found = False
        for contact in matching_contacts:
            if contact[1] == cognom:
                print("El número(s) de contacte per", nomContacteAtrucar, cognom, "és:", contact[3])
                found = True
                break
        if not found:
            print("No s'ha trobat cap contacte amb aquest cognom.")
    
    
    