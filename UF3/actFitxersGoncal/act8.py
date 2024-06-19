#Crea una funció anomenada generarXML, que donat un string etiqueta i un string valor generi <etiqueta>valor</etiqueta>. Amb aquesta funció i el fitxer fruites.txt genereu una fitxer amb el contingut:
arxiu2=open("act8sortida.txt",mode="w")

def generarXML(etiqueta,etiquetaPrincipal):
    llegir=open("act1.txt")
    arxiu2.seek(0)
    arxiu2.write("<"+etiquetaPrincipal+">\n")
    for linia in llegir:
        linia=linia.strip()
        liniaFitxerNou=("<"+etiqueta+">"+linia+"</"+etiqueta+">\n")
        arxiu2.write(liniaFitxerNou)
    arxiu2.seek(0,2)
    arxiu2.write("</"+etiquetaPrincipal+">")

generarXML("fruita","fruites")
