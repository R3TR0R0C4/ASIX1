try:
    from tkinter import *
    from tkinter import ttk
    from tkinter import messagebox
except:
    print("Hi ha agut un error important el mòdul tkinter, assegurat que està instal·lat")

try:
    import subprocess
except:
    print("Hi ha agut un error important el mòdul subprocess")

try:
    import speedtest
except:
    print("Hi ha agut un error important el mòdul speedtest, assegurat que està instal·lat, amb 'pip install speedtest-cli'")

tracerouteDetect=subprocess.run(["traceroute"], shell=True, capture_output=True, text=True)#Correm traceroute per comprobar si està instal·lat
if "not found" in tracerouteDetect.stderr:#Si no trobem el paquet:
    print('Necessites instal·lar el paquet "traceroute", ho pots fer amb " apt install traceroute "')#Printem i tanquem programa


else:
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
        global nomInterficies
        global ipsInterficies

        nom = subprocess.run(["ip -oneline address show up | awk '/inet / {print $2}'"], shell=True, capture_output=True, text=True) #obtenim nom interficies
        nom.stdout = nom.stdout.split("\n") #separem per \n
        nom.stdout = [itemInter for itemInter in nom.stdout if itemInter] #fem una llista amb els noms

        ips = subprocess.run(["ip -oneline address show up | awk '/inet / {print $4}'"], shell=True, capture_output=True, text=True)
        ips.stdout = ips.stdout.split("\n")
        ips.stdout = [itemIps for itemIps in ips.stdout if itemIps]
        
        nomInterficies = nom.stdout 
        ipsInterficies = ips.stdout

    # Obtenim la ruta perdefecte:
    def ipRoute(interficie):
        ruta=subprocess.run([f"ip route | grep {interficie.get()}" " | awk 'FNR==1{print $3}'"], shell=True, capture_output=True, text=True) #guardem la passarel·la apartir de la interficie indicada
        ruta=ruta.stdout #passem la variable a un string per processar-la
        ruta=ruta.replace("\n","") #eliminem el \n final
        
        labelIpRoute.config(text="La passarel·la per defecte de l'intefície és:   "+ruta)
        
        global pasarela 
        pasarela=ruta

    def ethtools(interficie):
        #Obtenim la velocitat del link
        velocitat=subprocess.run([f"ethtool {interficie.get()} | grep Speed: |awk"" 'FNR==1{print$2}'"], shell=True, capture_output=True, text=True) #link speed de l'interficie
        estat=subprocess.run([f"ethtool {interficie.get()} | grep 'Link detected:' |"" awk '{print $3}'"], shell=True, capture_output=True, text=True) #estat (plugged or not)
        duplex=subprocess.run([f"ethtool {interficie.get()} | grep Duplex: |"" awk '{print$2}'"], shell=True, capture_output=True, text=True) #estat del duplex

        if "Operation not permitted" in velocitat.stderr: #Comprovem si s'ha iniciat com administrador
            labelLinkSpeed.config(text="Necessites inicar el programa amb permissos d'administrador")
        
        elif "bad command line argument(s)" in velocitat.stderr:
            labelLinkSpeed.config(text="Assegurat de sel·leccionar una interfície")

        else:
            linkSpeed = velocitat.stdout #Guardem link speed en nova variable per processar-la
            linkSpeed=linkSpeed.replace("\n", "") #Eliminem un \n del string

            linkStatus = estat.stdout
            linkStatus=linkStatus.replace("\n","")

            duplexStatus=duplex.stdout 
            duplexStatus=duplexStatus.replace("\n", "")

            labelLinkSpeed.config(text="Velocitat del link:   "+linkSpeed+"\n Estat duplex:   "+duplexStatus+"\n Cable conectat:   "+linkStatus)

    def pingsExterns():
        global pingExtern

        pingExtern=subprocess.run([f"ping -c 4 1.1.1.1 | awk 'NR==2 || NR==3 || NR==4 || NR==5'"], shell=True, capture_output=True, text=True)
        
        if pingExtern.returncode == 0: #Si s'ha realitzat sense errors:
            pingExtern=pingExtern.stdout #passem la variable a un string per processar-la
            labelPings.config(text=treuNewLine(pingExtern))

        elif pingExtern.returncode == 1: #Si no trobem l'ip
            labelPings.config(text="Ping a IP externa fallida")

        elif pingExtern.returncode == 2: #Si la xarxa no està conectada
            labelPings.config(text="Xarxa inestable, comprova la connexió")

    def tracerouteExtern():
        pingInicial=subprocess.run(["ping 1.1.1.1 -c 1"], shell=True, capture_output=True, text=True)
        if pingInicial.returncode == 1:
            labelTraceroute.config(text="Pareix que no podem arrivar a la ip '1.1.1.1', assegurat de tenir internet")

        else:
            traceroute=subprocess.run(["traceroute 1.1.1.1 | awk 'NR>1' | wc -l"], shell=True, capture_output=True, text=True)
            #tracerouteComplet=traceroute.stdout
            traceroute=traceroute.stdout
            traceroute=traceroute.replace("\n","")
            labelTraceroute.config(text="Hi ha "+traceroute+" salts fins a 1.1.1.1")

    def tracerouteIntern():
        if pasarela == "":
            labelTraceroute.config(text="Assegurat d'escollir una interfície")

        else:
            pingInicial=subprocess.run([f"ping {pasarela} -c 1"], shell=True, capture_output=True, text=True)
            if pingInicial.returncode == 1:
                labelTraceroute.config(text=f"Pareix que no podem arrivar a la ip '{pasarela}', assegurat de tenir internet")

            else:
                traceroute=subprocess.run([f"traceroute {pasarela} | awk 'NR>1' | wc -l"], shell=True, capture_output=True, text=True)
                print(traceroute)
                #tracerouteComplet=traceroute.stdout
                traceroute=traceroute.stdout
                traceroute=traceroute.replace("\n","")
                labelTraceroute.config(text="Hi ha "+traceroute+f" salts fins a {pasarela}")

    def pingIntern(ipGateway):
        global pingPasarela
        
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
        dns=subprocess.run(["nmcli device show | grep IP4.DNS"], shell=True, capture_output=True, text=True)#agarrem els dns's del sistema apartir del network manager
        
        dnsPerProva=subprocess.run(["nmcli device show | grep IP4.DNS | awk 'FNR==1{print$2}'"], shell=True, capture_output=True, text=True)#escollim el dns del sistema, aixi ens saltem la possiblitat d'utilitzar 127.0.0.53, (cache d'ubuntu)
        dnsPerProva=dnsPerProva.stdout
        dnsPerProva=dnsPerProva.replace("\n","")

        #print(f"nslookup google.com {dnsPerProva} | awk 'NR>4'")
        lookup=subprocess.run([f"nslookup google.com {dnsPerProva} | awk 'NR>4'"], shell=True, capture_output=True, text=True) #fem el lookup, en cas de no tenir el network manager instal·lat la variable estarà buida, i farà amb el dns que trobi el sistema

        textLabel=f"{dns.stdout} \n lookup a google.com amb {dnsPerProva}:\n\n{lookup.stdout}"
        labelNslookup.config(text=textLabel)

    def iptables():
        try:
            reglesIPtables=subprocess.run(["iptables", "-L", "-t", "nat"], capture_output=True, text=True, check=True)#fém la comanda d'ip tables amb opcio de mostra el nat

            #Creem una nova finestra
            top=Toplevel(window)
            top.geometry("800x420")
            top.title("Regles d'iptables")
            top.resizable(False, False)

            #Creem una scrollbar vertical
            v=Scrollbar(top, orient='vertical')
            v.pack(side=RIGHT, fill='y')
            text=Text(top, yscrollcommand=v.set)

            #Inserim el text resultant de la comanda de subprocess en un canvas
            text.insert(END, reglesIPtables.stdout)
            v.config(command=text.yview)

            #configurem el canvas per que utilitzi tot l'espai disponible
            text.pack(fill=BOTH)


        except subprocess.CalledProcessError as error:
            if error.returncode == 4: #en cas de no iniciar l'script en mode administrador fallarà la comanda així que printem un error llegible
                print("Necessites iniciar el programa com administrador.")
                messagebox.showerror("Error", "Necessites iniciar el programa com administrador.")

            #En cas de trobar un altre error:
            else:
                print("Hi ha agut un error: ", error)
                messagebox.showerror("Error", "Hi ha agut un error: ", error)

    #Realitzem el test de velocitat
    def ferSpeedtest():
        test = speedtest.Speedtest()#Realitzem el test de velocitat
        baixada = round((test.download() / 1024 / 1024), 2)#passem el valor de baixada a Mbps i l'arredonim a 2 decimals
        pujada = round((test.upload() / 1024 / 1024), 2)#passem el valor de pujada a Mbps i l'arredonim a 2 decimals
        ping = test.results.ping #Agarrem el ping del atribut results del test
        timestamp = test.results.timestamp #agarrem l'hora i data en que s'ha fer el test

        #configurem el text de les labels de la funcio "finestraSpeedtest"
        labelDownload.config(text="Velocitat de baixada:  " + str(baixada) + " Mbps") #label vel. baixada
        labelUpload.config(text="Velocitat de pujada:  " + str(pujada) + " Mbps")#label vel. pujada
        labelPing.config(text="Velocitat de ping:  " + str(ping) + " ms")#label ping time
        labelTimestamp.config(text="Hora del test: " + timestamp[:10] +" "+timestamp[11:19])#label hora i data
        labelServidor.config(text="Servidor: " + test.best['sponsor'])#label nom empresa que hosteja el server
        labelCiutat.config(text="Ciutat: " + test.best['name'] + ", " + test.best['country'])#label ciutat i pais

    #Funcio per crear una nova finestra per mostrar els resultats de la prova de velocitat
    def finestraSpeedtest():
        testSpeed = Tk()
        testSpeed.geometry("350x200")
        testSpeed.configure(bg="light Grey")
        testSpeed.title("")
        testSpeed.resizable(False, False)
        
        botoCorreTest = Button(testSpeed, text="Speedtest", command=ferSpeedtest)
        botoCorreTest.pack()

        global labelDownload, labelUpload, labelPing, labelTimestamp, labelServidor, labelCiutat
        labelDownload = Label(testSpeed)
        labelDownload.pack()

        labelUpload = Label(testSpeed)
        labelUpload.pack()

        labelPing = Label(testSpeed)
        labelPing.pack()

        labelTimestamp = Label(testSpeed)
        labelTimestamp.pack()

        labelServidor = Label(testSpeed)
        labelServidor.pack()

        labelCiutat = Label(testSpeed)
        labelCiutat.pack()

        testSpeed.mainloop()

    interficiesIPs() #cridem funcio per guardar les ips i interficies

    # Definim propietats de la finestra de tkinter
    window = Tk() #generem finestra
    window.geometry("800x750") #declarem la mida de finestra
    window.configure(bg="light Grey") #configurem color de fons
    window.title("") #configurem nom de finestra
    window.resizable(False, False) #configurem que no es pugui canviar la mida de la finestra

    #Label mostrar IP
    labelIPactual=Label(
        text="Sel·lecciona una interfície:"
    )
    labelIPactual.pack()

    #Dropdown interfícies
    dropInterficiesOpcio=StringVar() #Declarem la variable que guardarà l'opcio com a "StringVar"
    dropdownInterficies = OptionMenu(
        window, #arguments: a quina finestra asociars-se
        dropInterficiesOpcio, #arguments: variable que guardarà l'opció escollida
        *nomInterficies #arguments: Llista de la cual rep les opcións
    )
    dropdownInterficies.pack()

    #Aplica la sel·lecció del dropdown
    buttonSelecciona=Button(
        text="Sel·lecciona", 
        command=lambda: ipRoute(dropInterficiesOpcio)
    )
    buttonSelecciona.pack()

    #Mostra la ip de la passarel·la per defecte de l'interfície sel·leccionada al dropdown
    labelIpRoute=Label()
    labelIpRoute.pack()

    #Separador
    separator = ttk.Separator(orient=HORIZONTAL)
    separator.pack(fill="x",pady=10)

    #boto per funcio mostrar velocitat d'ethtools
    buttonLinkSpeed=Button(
        text="Velocitat", 
        command=lambda: ethtools(dropInterficiesOpcio)
    )
    buttonLinkSpeed.pack()

    #label per mostrar la velocitat amb ethtools
    labelLinkSpeed=Label()
    labelLinkSpeed.pack()

    #Separador
    separator = ttk.Separator(orient=HORIZONTAL)
    separator.pack(fill="x",pady=10)

    #boto per realitzar pings a ip externes
    buttonPings=Button(
        text="Ping 1.1.1.1",
        command=lambda: pingsExterns()
    )
    buttonPings.pack()

    buttonTracerouteExtern=Button(
        text="Traceroute 1.1.1.1",
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
        text="Traceroute pasarel·la",
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

    botoSpeedtest=Button(
    text="Speedtest",
    command=lambda: finestraSpeedtest()
    )
    botoSpeedtest.pack()

    window.mainloop()