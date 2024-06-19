try:
    from os import listdir, path, getcwd
except:
    print("Hi ha agut un error important el mòdul 'os'")

try:
    import tkinter as tk
    from tkinter import ttk, messagebox, filedialog, simpledialog
    import tkinter.scrolledtext as scrolledtext
except:
    print("Hi ha agut un error important el paquet tkinter, assegurat de tenir-lo instal·lat amb 'pip install tk'")

try:
    import py7zr
except:
    print("Hi ha agut un error important el paquet py7zr, assegurat de tenir-lo instal·lat amb 'pip install py7zr'")

#Llistem el contingut de la carpeta oberta, ordenem primer carpetes i després arxius, aquests alfabeticament.
def llistaContingutCarpeta(ruta):
    try:
        #Llistem el contingut de la ruta donada
        contingut = listdir(ruta)

        #Guardem els arxius i carpetes en llistes separades:
        arxius = []
        carpetes = []
        for item in contingut:
            rutaItem = path.join(ruta, item)
            if path.isfile(rutaItem):
                arxius.append(item)
            elif path.isdir(rutaItem):
                carpetes.append(item)

        #Ordenem alfabeticament els arxius i carpetes:
        carpetes.sort()
        arxius.sort()
        
        #Juntem els continguts i retornem:
        contingutOrdenat = carpetes + arxius
        return contingutOrdenat

    except Exception as e:
        messagebox.showerror("Error", str(e))
        return []

#Mirem si l'arxiu és una carpeta, si ho és li posem un "/" al final, d'aquesta forma el gestor d'arxius es veu que és una carpeta i que un arxiu més facilment
def conseguirNomXdisplay(item, pathActual):
    pathSencer=path.join(pathActual, item)
    if path.isdir(pathSencer):
        item=item + "/"
        return item
    else:
        return item

#Actualitzem la variable que té el contingut de la carpeta actual
def actualitzaGestorArxius(pathActual):
    #Declarem la var global amb el directori actual
    global directoriActual
    directoriActual=pathActual
    #Eliminem l'informació dintre del frame del gestor d'arxius, per no acumular-la
    for widget in frameGestArxius.winfo_children():
        widget.destroy()

    #Per tornar a la carpeta pare:
    contents=[".."] + llistaContingutCarpeta(pathActual)
    for item in contents:
        nomArxiuDisplay=conseguirNomXdisplay(item, pathActual)
        #Declarem la variable que contindrà el contingut del gestor d'arxius (esquerra)
        label=ttk.Label(frameGestArxius, text=nomArxiuDisplay)
        label.pack(anchor="w")#Posem el frame a la esquerra de la pantalla
        label.bind("<Double-1>", lambda e, item=item: dobleClick(item, pathActual))#Mirem si l'usuari fa un doble click sobre un item, si ho fa l'enviem a la funció dobleClick

def dobleClick(item, pathActual):
    if item=="..":#Si fa click sobre '..' l'enviem a la carpeta pare
        nouPath=path.dirname(pathActual)
    else:#Si és a un altre directori l'enviem dintre d'aquest
        nouPath=path.join(pathActual, item)


    #si el path és un directori actualitzem la pantalla
    if path.isdir(nouPath):
        actualitzaGestorArxius(nouPath)
    #si el path és un arxiu cridem a l'editor
    else:
        obrirArxiuEditor(nouPath)


        
    
def obrirArxiuEditor(rutaArxiu):
    try:
        if rutaArxiu.endswith(".7z"):#Mirem si és un arxiu comprimit
            descomprimeixArx(rutaArxiu)
            return
    #Obrim l'arxiu
        with open(rutaArxiu, "r") as file:
            content=file.read()
        
        text_area.config(state=tk.NORMAL)#Configurem el frame de l'editor per que el contingut sigui editable
        text_area.delete(1.0, tk.END)#eliminem tot el text (si n'hi ha algun) en el frame del editor
        text_area.insert(tk.END, content)#Insertem el text
        text_area.edit_modified(False)#Modifiquem l'estat de modificació per si hem editat un arxiu anteriorment que no falli al guardar-lo
        text_area.rutaArxiu=rutaArxiu
    except Exception as e:
        messagebox.showerror("Error", str(e))

def guardaArxiu():
    try:
        contingut=text_area.get(1.0, tk.END)
        #Obrim arxiu amb mode edició i escribim
        with open(text_area.rutaArxiu, "w") as file:
            file.write(contingut)
        #Reiniciem l'estat de modificació
        text_area.edit_modified(False)
        messagebox.showinfo("Correcte", "Arxiu guardat correctament!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def selectorObrirCarpeta():
    #Demanem la carpeta a obrir
    selected_folder=filedialog.askdirectory(initialdir=directoriActual)
    #Si se n'ha sel·leccionat alguna actualitzem vista gestor arxius
    if selected_folder:
        actualitzaGestorArxius(selected_folder)

def creaNouArx():
    #Demanem el un popup el nom de l'arxiu
    nomArxiu=simpledialog.askstring("Nou Arxiu", "Introdueix el nom del nou arxiu amb l'extenció:")
    #si l'ha introduït, creem la ruta absoluta
    if nomArxiu:
        rutaArxiu=path.join(directoriActual, nomArxiu)
        if not path.exists(rutaArxiu):
            try:
                #l'obrim amb mode edició i escribim rés, després actualitzem vista del gestor d'arxius i obrim l'editor
                with open(rutaArxiu, "w") as file:
                    file.write("")
                actualitzaGestorArxius(directoriActual)
                obrirArxiuEditor(rutaArxiu)
            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showerror("Error", "L'arxiu ja existeix!")



def comprimeixArxiu():
    try:
        rutaArxiu=text_area.rutaArxiu
        if not rutaArxiu:
            messagebox.showerror("Error", "Ningun arxiu està obert, obre'n un primer.")
            return
        #Creem el nom de l'arxiu resultant, el guardem (com comprimit)
        output_file=rutaArxiu + ".7z"
        with py7zr.SevenZipFile(output_file, "w") as archive:
            archive.write(rutaArxiu, arcname=path.basename(rutaArxiu))
        
        messagebox.showinfo("Correcte", f"Arxiu comprimit a: {output_file}")
    except Exception as e:
        messagebox.showerror("Error", str(e))


#Descomprimim Arxiu

def descomprimeixArx(rutaArxiu):
    directoriSortida=path.dirname(rutaArxiu)    
    with py7zr.SevenZipFile(rutaArxiu, "r") as comprimit:
        comprimit.extractall(path=directoriSortida)
        messagebox.showinfo("Extracció correcta", f"Arxiu descomprimit a: {directoriSortida}")
        actualitzaGestorArxius(directoriSortida)


finPrincip=tk.Tk()
finPrincip.title("Directory Contents and File Viewer")

finestra=ttk.PanedWindow(finPrincip, orient=tk.HORIZONTAL)
finestra.pack(fill="both", expand=True)

frameGestArxius=ttk.Frame(finestra, padding="10", width=200)
finestra.add(frameGestArxius)

text_area=scrolledtext.ScrolledText(finestra, wrap=tk.WORD, state=tk.DISABLED, width=80, height=20)
finestra.add(text_area)

frameBotons=ttk.Frame(finPrincip, padding="10")
frameBotons.pack(fill="x")

botSelecCarpet=ttk.Button(frameBotons, text="Obri una carpeta", command=selectorObrirCarpeta)
botSelecCarpet.pack(side="left",padx=2)

botGuardArx=ttk.Button(frameBotons, text="Guarda Arxiu", command=guardaArxiu)
botGuardArx.pack(side="left",padx=2)

botArxNou=ttk.Button(frameBotons, text="Nou Arxiu", command=creaNouArx)
botArxNou.pack(side="left",padx=2)

compress_button=ttk.Button(frameBotons, text="Comprimeix Arxiu", command=comprimeixArxiu)
compress_button.pack(side="left",padx=2)

directoriActual=getcwd()
actualitzaGestorArxius(directoriActual)

finPrincip.mainloop()