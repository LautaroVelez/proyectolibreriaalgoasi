from tkinter import *
import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
from phonenumbers import timezone
from datetime import datetime
from opencage.geocoder import OpenCageGeocode
import webbrowser
import pytz
from PIL import Image, ImageTk as itk

root = Tk()
root.title("Localizador de telefono-LJM")
root.geometry("500x630")
root.resizable(False,False)


def buscar():
    entrada_numeros=entrada.get()
    numero=phonenumbers.parse(entrada_numeros)

    #pais
    locate=geocoder.description_for_number(numero, "en")
    pais.config(text=locate)

    #sim
    operador=carrier.name_for_number(numero, "en")
    sim.config(text=operador)

    #timezone
    time=timezone.time_zones_for_geographical_number(numero)
    zona.config(text=time)

    
    def callback(url):
        webbrowser.open_new(url)

    #longitudylatitud
    geocodereano = OpenCageGeocode("d3cf1876e1b2445a99d97127c77cfce8")
    query=str(locate)
    results=geocodereano.geocode(query)
    lat=results[0]['geometry']['lat']
    long=results[0]['geometry']['lng']
    longitud.config(text=long)
    latitud.config(text=lat)

    link1.bind("<Button-1>", lambda e: callback(f"https://www.openstreetmap.org/note/new#map=17/{lat}/{long}&layers=N"))
    

    #horadelcelu
    hora=datetime.now(pytz.timezone(time[0]))
    hora_local=hora.strftime("%H:%M:%S")
    clock.config(text=hora_local)
    
######################INTERFAZ GRAFICA#############################################

#TITULO
titulo=PhotoImage(file="titulo.png")
Label(root,image=titulo).place(x=80,y=80)

#ENTRADA DE DATOS
Entry_back=PhotoImage(file="buscador.png")
Label(root,image=Entry_back).place(x=80,y=190)
entrada=StringVar()
meter_num=Entry(root,textvariable=entrada,width=17,bd=0,font=("Arial",20))
meter_num.place(x=110,y=220)

#BOTONOVICH
buscar_imagen=PhotoImage(file="search.png") 
search=Button(image=buscar_imagen,borderwidth=0,cursor="hand2",bd=0,font=("arial",16),command=buscar)
search.place(x=95,y=300)


#IMAGEN MAPS
maps_imagen= Image.open("marcador-de-mapa.png")
maps_imagen=maps_imagen.resize((40,40),Image.LANCZOS)
maps_imagen=itk.PhotoImage(maps_imagen)
maps_imagen_lbl=Label(root,image=maps_imagen)
maps_imagen_lbl.pack()

#LABELS
pais=Label(root,text="",fg="black",font=("Cambria",12,"bold"))
pais.place(x=250,y=380)

sim=Label(root,text="",fg="black",font=("Cambria",12,"bold"))
sim.place(x=250,y=420)

zona=Label(root,text="",fg="black",font=("Cambria",12,"bold"))
zona.place(x=250,y=460)

clock=Label(root,text="",fg="black",font=("Cambria",12,"bold"))
clock.place(x=250,y=500)

longitud=Label(root,text="",fg="black",font=("Cambria",12,"bold"))
longitud.place(x=250,y=540)

latitud=Label(root,text="",fg="black",font=("Cambria",12,"bold"))
latitud.place(x=250,y=580)

link1 = Label (root, text="Maps", fg="blue", cursor="hand2", font=("Cambria", 12, "bold"))
link1.pack()

#########################TEXTO INSERVIBLE##############################
pais1=Label(root,text="Localidad:",fg="black",font=("Cambria",12,"bold"))
pais1.place(x=140,y=380)

sim1=Label(root,text="Proveedor:",fg="black",font=("Cambria",12,"bold"))
sim1.place(x=140,y=420)

zona1=Label(root,text="Zona:",fg="black",font=("Cambria",12,"bold"))
zona1.place(x=140,y=460)

clock1=Label(root,text="Hora:",fg="black",font=("Cambria",12,"bold"))
clock1.place(x=140,y=500)

longitud1=Label(root,text="Longitud:",fg="black",font=("Cambria",12,"bold"))
longitud1.place(x=140,y=540)

latitud1=Label(root,text="Latitud:",fg="black",font=("Cambria",12,"bold"))
latitud1.place(x=140,y=580)

root.mainloop()
