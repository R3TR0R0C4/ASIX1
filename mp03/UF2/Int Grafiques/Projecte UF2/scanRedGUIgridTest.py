from tkinter import *
from tkinter import ttk
import subprocess

tracerouteDetect=subprocess.run(["traceroute"], shell=True, capture_output=True, text=True)#Correm traceroute per comprobar si està instal·lat
if "not found" in tracerouteDetect.stderr:#Si no trobem el paquet:
    print('Necessites instal·lar el paquet "traceroute", ho pots fer amb " apt install traceroute "')#Printem i tanquem programa

else:
    #Declarem variables buides per les funcións.
    nomInterficies="" #nom d'interfícies del sistema
    ipsInterficies="" #ips d'interfícies del sistema
    pasarela="" #gateway de l'interficie sel·leccionada 
    pingExtern="" #resultat ping a ip externa
    pingPasarela="" #resultat ping a ip gateway

    #Funcio per treure l'ultim "\n" d'una string
    def treuNewLine(text):
        parts = text.rsplit('\n', 1)
        if len(parts) == 2:
            return parts[0] + parts[1]
        return text

    # Obtenim IP, Nom d'interficie, ho guardem en llistes i fem un diccionari amb elles
    def interficiesIPs ():
        global nomInterficies #cridem la variable global
        global ipsInterficies #cridem la variable global

        nom = subprocess.run(["ip -oneline address show up | awk '/inet / {print $2}'"], shell=True, capture_output=True, text=True) #obtenim nom interficies
        nom.stdout = nom.stdout.split("\n") #separem per \n
        nom.stdout = [itemInter for itemInter in nom.stdout if itemInter] #fem una llista amb els noms

        ips = subprocess.run(["ip -oneline address show up | awk '/inet / {print $4}'"], shell=True, capture_output=True, text=True) #obtenim ips
        ips.stdout = ips.stdout.split("\n") #separem per \n
        ips.stdout = [itemIps for itemIps in ips.stdout if itemIps] #fem una llista amb les ips
        
        nomInterficies = nom.stdout #declarem els noms en la variable global
        ipsInterficies = ips.stdout #declarem les ips en la variable global

    # Obtenim la ruta perdefecte:
    def ipRoute(interficie):
        ruta=subprocess.run([f"ip route | grep {interficie.get()}" " | awk 'FNR==1{print $3}'"], shell=True, capture_output=True, text=True) #guardem la passarel·la apartir de la interficie indicada
        ruta=ruta.stdout #passem la variable a un string per processar-la
        ruta=ruta.replace("\n","") #eliminem el \n final
        labelIpRoute.config(text="La passarel·la per defecte de l'intefície és:   "+ruta) #configurem label amb el resultat
        global pasarela #declarem variable global
        pasarela=ruta #definim la variable global amb el resultat de l'interna


    def ethtools(interficie):
        #Obtenim la velocitat del link
        velocitat=subprocess.run([f"ethtool {interficie.get()} | grep Speed: |awk"" 'FNR==1{print$2}'"], shell=True, capture_output=True, text=True) #Obtenim la link speed de l'interficie
        estat=subprocess.run([f"ethtool {interficie.get()} | grep 'Link detected:' |"" awk '{print $3}'"], shell=True, capture_output=True, text=True) #Obtenim l'estat (plugged or not)
        duplex=subprocess.run([f"ethtool {interficie.get()} | grep Duplex: |"" awk '{print$2}'"], shell=True, capture_output=True, text=True) #Obtenim l'estat del duplex

        if "Operation not permitted" in velocitat.stderr: #Comprovem si s'ha iniciat com administrador
            #print("Necessites iniciar el programa amb permissos d'administrador") #Printem a terminal (test only)
            labelLinkSpeed.config(text="Necessites inicar el programa amb permissos d'administrador")
        
        elif "bad command line argument(s)" in velocitat.stderr: #mirem si el resultat conté la string, es posible que no s'hagi sel·leccionat una interfície, printem missatge
            #print("Assegurat de sel·leccionar una interfície") #Printem a terminal (test only)
            labelLinkSpeed.config(text="Assegurat de sel·leccionar una interfície")

        else:
            linkSpeed = velocitat.stdout #Guardem link speed en nova variable per processar-la
            linkSpeed=linkSpeed.replace("\n", "") #Eliminem un \n del string

            linkStatus = estat.stdout #Guardem link status en nova variable per processar-la
            linkStatus=linkStatus.replace("\n","")#Eliminem un \n del string

            duplexStatus=duplex.stdout #Guardem duplex status en nova variable per processar-la
            duplexStatus=duplexStatus.replace("\n", "")#Eliminem un \n del string

            labelLinkSpeed.config(text="Velocitat del link:   "+linkSpeed+"\n Estat duplex:   "+duplexStatus+"\n Cable conectat:   "+linkStatus)#Configurem la label per printar velocitat

    def pingsExterns():
        global pingExtern #cridem la variable global

        pingExtern=subprocess.run([f"ping -c 4 1.1.1.1 | awk 'NR==2 || NR==3 || NR==4 || NR==5'"], shell=True, capture_output=True, text=True) #fem pings a 1.1.1.1 de cloudflare
        
        if pingExtern.returncode == 0: #Si s'ha realitzat sense errors:
            pingExtern=pingExtern.stdout #passem la variable a un string per processar-la
            labelPings.config(text=treuNewLine(pingExtern)) #configurem la label amb el resultat del ping

        elif pingExtern.returncode == 1: #Si no trobem l'ip
            labelPings.config(text="Ping a IP externa fallida") #configurem la label amb l'error

        elif pingExtern.returncode == 2: #Si la xarxa no està conectada
            labelPings.config(text="Xarxa inestable, comprova la connexió") #configurem la label amb l'error

    def tracerouteExtern():
        traceroute=subprocess.run(["traceroute 1.1.1.1"], shell=True, capture_output=True, text=True)
        labelTraceroute.config(text=traceroute.stdout)

    def tracerouteIntern():
        traceroute=subprocess.run([f"traceroute {pasarela}"], shell=True, capture_output=True, text=True)
        labelTraceroute.config(text=traceroute.stdout)

    def pingIntern(ipGateway):
        global pingPasarela #cridem la variable global
        
        if ipGateway == "": #Comprovem si la variable amb l'ip de pasarel·la esta plena o no
            labelPings.config(text="Assegurat de sel·leccionar una interficie,\n i que aquesta tigui una ip passarel·la vàlida")

        else: #En cas de que hi hagi algo fem els pings:
            pingPasarela=subprocess.run([f"ping -c 4 {ipGateway} | awk 'NR==2 || NR==3 || NR==4 || NR==5'"], shell=True, capture_output=True, text=True) #fem els pings a la ip de la passarel·la
        
            if pingPasarela.returncode == 0: #Si s'ha realitzat sense errors:
                pingPasarela=pingPasarela.stdout #passem la variable a un string per processar-la
                labelPings.config(text=treuNewLine(pingPasarela)) #configurem la label amb el resultat del ping
            elif pingPasarela.returncode == 1: #Si no trobem l'ip
                labelPings.config(text="Ping a IP externa fallida") #configurem la label amb l'error
            elif pingPasarela.returncode == 2: #Si la xarxa no està conectada
                labelPings.config(text="Xarxa inestable, comprova la connexió") #configurem la label amb l'error

    def dnslookup():
        dns=subprocess.run(["nmcli device show | grep IP4.DNS"], shell=True, capture_output=True, text=True)
        
        dnsPerProva=subprocess.run(["nmcli device show | grep IP4.DNS | awk 'FNR==1{print$2}'"], shell=True, capture_output=True, text=True)
        dnsPerProva=dnsPerProva.stdout
        dnsPerProva=dnsPerProva.replace("\n","")

        print(f"nslookup google.com {dnsPerProva} | awk 'NR>4'")
        lookup=subprocess.run([f"nslookup google.com {dnsPerProva} | awk 'NR>4'"], shell=True, capture_output=True, text=True)

        textLabel=f"{dns.stdout} \n lookup a google.com amb {dnsPerProva}:\n\n{lookup.stdout}"
        labelNslookup.config(text=textLabel)

    def iptables():
        print("test iptables:")

        reglesIPtables=subprocess.run(["iptables -L"], shell=True, capture_output=True, text=True)

        top= Toplevel(window)
        top.geometry("750x250")
        top.title("Regles d'iptables")
        Label(top, text=reglesIPtables.stdout).pack()


    interficiesIPs() #cridem funcio per guardar les ips i interficies

    # Definim propietats de la finestra de tkinter
    window = Tk() #generem finestra
    window.geometry("1000x800") #declarem la mida de finestra
    window.configure(bg="light Grey") #configurem color de fons
    window.title("") #configurem nom de finestra
    window.resizable(False, False) #configurem que no es pugui canviar la mida de la finestra

    #Label mostrar IP
    labelIPactual=Label(
        text="Sel·lecciona una interfície:"
    )
    labelIPactual.grid(column=0,row=0)

    #Dropdown interfícies
    dropInterficiesOpcio=StringVar() #Declarem la variable que guardarà l'opcio com a "StringVar"
    dropdownInterficies = OptionMenu(
        window, #arguments: a quina finestra asociars-se
        dropInterficiesOpcio, #arguments: variable que guardarà l'opció escollida
        *nomInterficies #arguments: Llista de la cual rep les opcións
    )
    dropdownInterficies.grid(column=1,row=0)

    #Aplica la sel·lecció del dropdown
    buttonSelecciona=Button(
        text="Sel·lecciona", 
        command=lambda: ipRoute(dropInterficiesOpcio)
    )
    buttonSelecciona.grid(column=2,row=0)

    buttonRefresca=Button(
        text="Refresca",
        command=lambda: interficiesIPs()
    )
    buttonRefresca.grid(column=3,row=0)
    
    #Mostra la ip de la passarel·la per defecte de l'interfície sel·leccionada al dropdown
    labelIpRoute=Label()
    labelIpRoute.grid(column=0,row=1,columnspan=4)


    """#Separador
    separator = ttk.Separator(orient=HORIZONTAL)
    separator.grid(sticky=NSEW,row=2)"""
    
    
    #boto per funcio mostrar velocitat d'ethtools
    buttonLinkSpeed=Button(
        text="Velocitat", 
        command=lambda: ethtools(dropInterficiesOpcio)
    )
    buttonLinkSpeed.grid(column=0,row=2)

    #label per mostrar la velocitat amb ethtools
    labelLinkSpeed=Label()
    labelLinkSpeed.grid(column=1,row=2,columnspan=3)
    
    
    """

    #Separador
    separator = ttk.Separator(orient=HORIZONTAL)
    separator.pack(fill="x",pady=10)

    #boto per realitzar pings a ip externes
    buttonPings=Button(
        text="Ping extern",
        command=lambda: pingsExterns()
    )
    buttonPings.pack()

    buttonTracerouteExtern=Button(
        text="Traceroute extern",
        command=lambda: tracerouteExtern()
    )
    buttonTracerouteExtern.pack()

    #boto per realitzar pings a gateways
    buttonPings=Button(
        text="Ping passarel·la",
        command=lambda: pingIntern(pasarela)
    )
    buttonPings.pack()

    buttonTracerouteIntern=Button(
        text="Traceroute Intern",
        command=lambda: tracerouteIntern()
    )
    buttonTracerouteIntern.pack()

    #label per l'estat del ping
    labelPings=Label()
    labelPings.pack()

    labelTraceroute=Label()
    labelTraceroute.pack()

    #Separador
    separator = ttk.Separator(orient=HORIZONTAL)
    separator.pack(fill="x",pady=10)

    botoNslookup=Button(
        text="test nslookup",
        command=lambda: dnslookup()
    )
    botoNslookup.pack()

    labelNslookup=Label()
    labelNslookup.pack()

    #Separador
    separator = ttk.Separator(orient=HORIZONTAL)
    separator.pack(fill="x",pady=10)

    botoIPtables=Button(
        text="Regles d'iptables",
        command=lambda: iptables()
    )
    botoIPtables.pack()

    
    """
    window.mainloop()