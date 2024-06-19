try:
    from subprocess import run #Importarem el procés "run" del mòdul "subprocess"
except:
    print("Hi ha agut un error important la llibreria subprocess, comprova la que la seva instal·lació és correcta")
try:
    from colorama import Fore, Style #Importarem Fore i Style per donar colors als prints
except:
    print("Hi ha agut un error importat la llibrerai colorama, comprova la que la seva instal·lació és correcta")

#Comprovem que nmap estigui instal·lat:
instalat = run(["nmap"], capture_output=True, text=True, shell=True)#Executarém nmap

if "nmap: not found" in str(instalat.stderr):#Revisem la sortida stderr per veure si nmap està instal·lat
    print("nmap no s'ha trobat instal·lat al sistema, sortint del script")#Si no està instal·lat saltem l'error


#Si està instal·lat Iniciarém el programa normalment
else:
    run(["clear"])#llimpiem la pantalla de l'usuari
    try:

        #Detecció interfícies del sistema
        interficies=run(["ip -oneline address show up | awk '/inet / {print $2}'"], shell=True, capture_output=True, text=True) #Guarda el nom de les interfícies que té el sistema.
        interficies.stdout = interficies.stdout.split("\n") #Utilitzem la funció split("\n") per separar els noms de les interfícies
        interficies.stdout = [itemInter for itemInter in interficies.stdout if itemInter] #L'utilitzem per treure "\n" extra que introdueix la funció anterior


        #Detecció IPs del sistema
        ips=run(["ip -oneline address show up | awk '/inet / {print $4}'"], shell=True, capture_output=True, text=True) #Guarda les IPs de les interfícies que tenen les interfícies.
        ips.stdout = ips.stdout.split("\n") #Utilitzem la funció split("\n") per separar les IPs de les interfícies
        ips.stdout = [itemIps for itemIps in ips.stdout if itemIps] #L'utilitzem per treure "\n" extra que introdueix la funció anterior


        #Generem el diccionari interficies-ips    
        interficiesIPs = {interficies.stdout[i]: ips.stdout[i] for i in range(len(interficies.stdout))} #Usem les dos llistes (d'interficies i de ips) per generar un diccionari. https://www.geeksforgeeks.org/python-convert-two-lists-into-a-dictionary/
    
    
    except:
        #Printem si hi ha agut algun error mentre detectavem les ips o les interfícies
        print(f"{Fore.RED}Hi ha hagut un problema inesperat detectant les IPs del sistema{Fore.RESET}")


    #Selecció interfície on usarém nmap
    print(Fore.CYAN+"Dis-me quina interfície vols utilitzar:")
    
    #Printem les intefícies que s'han trobat apartir del diccionari anterior
    for interf, ip in interficiesIPs.items():
        print(f"{Fore.BLUE}{interf}: {Fore.GREEN}{ip}{Fore.RESET}")
    
    #Preguntem a l'usuari quina interfície vol utilitzar (preguntem el nom).
    interNMAP=input(f"{Fore.MAGENTA}> {Style.RESET_ALL}") 

    #Printem a l'usuari quina interfície amb quina IP ha seleccionat.
    print("\n"f"{Fore.CYAN}Has sel·leccionat l'interfície --  {Fore.GREEN}{interNMAP}{Fore.CYAN} -- Amb l'IP -- {Fore.GREEN}{interficiesIPs[interNMAP]}{Fore.CYAN} --{Fore.RESET}") 



    #Execució nmap ping sweep i guardat en una variable
    print(f"{Fore.CYAN}La comanda que s'executarà és: {Fore.YELLOW}  nmap "+"-sn "+interficiesIPs[interNMAP]+f" -oG - {Fore.RESET}""\n") #Printem informació a l'usuari sobre quina comanda executarém.
    nmapPingSweep=run(["nmap -sn "+interficiesIPs[interNMAP]+" -oG - | awk '/Up$/{print $2}'"], shell=True, capture_output=True, text=True) #Realitzem el ping sweep i sel·leccionem només les IPs amb l'awk.
    
    nmapPingSweep.stdout = nmapPingSweep.stdout.split("\n") #Utilitzem la funció split("\n") per a que les IPs passin a ser items de llista, ja a que per defecte és un sol item separat per salts de linia.
    nmapPingSweep.stdout = [itemNmap for itemNmap in nmapPingSweep.stdout if itemNmap] #L'utilitzem per treure un item que es crearà que estarà buit degut a la transformació del split.
    
    
    print(f"{Fore.CYAN}Aquestes són les IPs que s'han trobat:{Fore.RESET}\n")
    #Printem les IPs que s'han trobat.
    for num, (ipsPingSweep) in enumerate(nmapPingSweep.stdout, start=1): #utilitzarém la variable num pel nombre del principi, i ipsPingSweep per les ips de la llista, després un enumerate que començarà pel número 1. 
        print(f"{Fore.BLUE}{num} - {Fore.GREEN}{ipsPingSweep}{Fore.RESET}") #I ho printem:
    print("\n")


    print(f"{Fore.CYAN}De quina IP vols saber els ports?{Fore.RESET}")
    interNmapPort=int(input(f"{Fore.MAGENTA}> {Style.RESET_ALL}")) #Demanem a l'usuari quina ip vol
    
    nmapPortScan=run(["nmap -p- -sV "+nmapPingSweep.stdout[interNmapPort-1]+" | awk '/open/'"], shell=True, capture_output=True, text=True) #Comanda per realitzar un escaneig de ports a l'ip.

    print("\n"f"{Fore.CYAN}Aquesta és la comanda que s'executarà:  "+f"{Fore.YELLOW}nmap -p- "+nmapPingSweep.stdout[interNmapPort-1]+f"\n")
    print(f"{Fore.CYAN}Aquests són els ports i serveis que té el host:\n{Fore.GREEN}{nmapPortScan.stdout}{Fore.RESET}")

    portsNMAP = nmapPortScan.stdout.split("\n")


    portsProces = [linePorts.split()[0] for linePorts in portsNMAP if linePorts.strip()]
    versioProces = [' '.join(lineVersio.split()[2:]) for lineVersio in portsNMAP if lineVersio.strip()]


    diccionariPortsVersio = {portsProces[i]: versioProces[i] for i in range(len(portsProces))}
    print(f"{Fore.RED}{diccionariPortsVersio}{Fore.RESET}")

    print(f"{Fore.CYAN}Sobre quin port vols fer un escaneig de vulnerabilitats?")
    portsVulnerInput=input(f"{Fore.MAGENTA}> {Style.RESET_ALL}")
    
    print(f"{Fore.CYAN}S'utilitzarà l'script vulners...{Fore.RESET}")
    print(f"{Fore.CYAN}La comanda que s'està utilitzant és:  nmap -sV -p {Fore.YELLOW}{portsVulnerInput} {interNmapPort} --script vulners | awk '/\| /' \n{Fore.RESET}")
    
    portsVulnerRun=run(["nmap -sV -p "+portsVulnerInput+" "+interNmapPort+" --script vulners | awk '/\| /'"], shell=True, capture_output=True, text=True) #Comanda per realitzar un escaneig de ports a l'ip.

    print(f"{Fore.GREEN},{portsVulnerRun.stdout},{Fore.RESET}")