import pyqrcode as qrc
from tkinter import *

def pintarIguardar():
    global img
    valor=entrada1.get()
    qr=qrc.create(valor)
    nomArxiu=valor.replace(".","_")
    img=qr.png(f"qr_{nomArxiu}.png",scale=10,background=(255,255,255))
    qr=qr.xbm(scale=6)
    img=BitmapImage(data=qr, background="white")
    label2.config(image=img)

def pintar():
    global img
    valor=entrada1.get()
    qr=qrc.create(valor)
    qr=qr.xbm(scale=6)
    img=BitmapImage(data=qr, background="white")
    label2.config(image=img)


window=Tk()
window.geometry("550x450")
window.configure(bg="light Grey")
window.title("Creador QRs")


label1=Label(text="Aplicació Creadora QR",
             bg="#181818",
             foreground="white",
             width=66,
             border=10,
             anchor="center")
label1.grid(column=0,row=0)




label2=Label()
label2.grid(column=0,row=1)

entrada1=Entry()
entrada1.grid(column=0,row=2)


button1=Button(width=15,pady=5,text="Genera i Guarda",command=pintarIguardar)
button1.grid(column=0,row=3,)

button2=Button(width=15,pady=5,text="Genera",command=pintar)
button2.grid(column=0,row=4)

button3=Button(width=15,pady=5,text="Sortida",command=window.destroy)
button3.grid(column=0,row=5)

window.resizable(False,False)
window.mainloop()