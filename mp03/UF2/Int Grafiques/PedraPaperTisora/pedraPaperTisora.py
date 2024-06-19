from tkinter import *
from random import *

def joc(jug):
    items={1:"pedra",2:"paper",3:"tissora",4:"llangardaix",5:"spock"}
    resol={1:(3,4),2:(1,5),3:(2,4),4:(2,5),5:(1,2)}

    cpu=randint(1,5)

    if jug==cpu:
        jugGuany="Empat"

    elif cpu in resol[jug]:
        jugGuany="Guanya Jugador"

    else:
        jugGuany="Guanya CPU"
    
    resultat.config(text=jugGuany)
    opcioJugador.config(text="Jugador ha escollit:  "+items[jug])
    opcioCpu.config(text="CPU ha escollit:  "+items[cpu])

window=Tk()
window.geometry("600x300")
window.configure(bg="light Grey")
window.title("Pedra Paper Tisora Spock Llangardaix")

label1=Label(text="Pedra Paper Tisora Spock Llangardaix",
             bg="#1f1f1f",
             foreground="white",
             width=70,
             border=10,
             anchor="center")
label1.grid(column=0,row=0,columnspan=5,pady=5)

label2=Label(text="Escull:",
             bg="#1f1f1f",
             foreground="white",

             anchor="w")
label2.grid(column=0,row=1,pady=5)


btoPedra=Button(width=9,text="Pedra",command=lambda: joc(1))
btoPedra.grid(column=0,row=2,padx=8)

btoPaper=Button(width=9,text="Paper",command=lambda: joc(2))
btoPaper.grid(column=1,row=2,padx=8)

btoTissora=Button(width=9,text="Tissora",command=lambda: joc(3))
btoTissora.grid(column=2,row=2,padx=8)

btoLlangardaix=Button(width=9,text="Llangardaix",command=lambda: joc(4))
btoLlangardaix.grid(column=3,row=2,padx=8)

btoSpock=Button(width=9,text="Spock",command=lambda: joc(5))
btoSpock.grid(column=4,row=2,padx=8)



opcioJugador=Label()
opcioJugador.grid(column=1,row=3,columnspan=3,pady=8)

opcioCpu =Label()
opcioCpu.grid(column=1,row=4,columnspan=3,pady=8)

resultat=Label()
resultat.grid(column=1,row=5,columnspan=3,pady=8)



window.resizable(False,False)
window.mainloop()