agenda=""
def carregarAgenda(agendaCarregar):
    global agenda
    if agendaCarregar == 1:
        agenda=open("personal.txt")
        menu()
    elif agendaCarregar == 2:
        agenda=open("laboral.txt")
        menu()
    else:
        print("Agenda no vàlida.")

def menu():
    while True:
        print("""Que voldràs fer:
              1-Llistar agenda
              2-Trucar a contacte
              3-sortir""")

        opcio=int(input("> "))

        if opcio == 1:
            llistar()
        elif opcio == 2:
            trucar()
        elif opcio == 3:
            print("Sortint...")
            break
        else:
            print("opcio no correcta")
            menu()

        break

def llistar():
    print("\n","Resultats de l'agenda: ", quinaAgeda,"\n")
    global diccionari
    diccionari={}

    for contacte in agenda.read().strip().split("\n"):
        contacte=contacte.strip().split(":")
        diccionari[contacte[1]]=contacte[0]
        
    print(diccionari)
    
    print()
    menu()


def trucar():
    print("A quina persona vols trucar? ")
    personaTrucar=input("> ")
    
    try:
        for numeroTel, persona in diccionari.items():
            if personaTrucar==persona:
                print("Trucant a",persona, "Amb el número: ",numeroTel)
    except:
        print("aquesta persona no existeix a l'agenda sel·leccionada")    


quinaAgeda=int(input("""Quina agenda vols carregar, 
                 
1-personal.txt
2-laboral.txt  \n> """))
carregarAgenda(quinaAgeda)