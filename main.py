from locale import currency
from re import L
from tkinter import *
import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
from phonenumbers import timezone
from timezonefinder import TimezoneFinder
from geopy.geocoders import Nominatim
from datetime import datetime
import pytz

root = Tk()
root.title("Localizador de telefono-LJM")
root.geometry("365x584+200+200")
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

    #longitudylatitud
    geolocator=Nominatim(user_agent="geoapiExercises")
    location= geolocator.geocode(locate)

    long=location.longitude
    lat=location.latitude
    longitud.config(text=long)
    latitud.config(text=lat)

    #horadelcelu
    obj=TimezoneFinder()
    result= obj.timezone_at(lng=location.longitude, lat=location.latitude)

    home=pytz.timezone(result)
    local_time=datetime.now(home)
    current_time= local_time.strftime("%I:%M:%p")
    clock.config(text=current_time)

####            INTERFAZ GRAFICA OORRRWWWW         ############

#LOGO
logo=PhotoImage(file="logo.png")
Label(root,image=logo).place(x=240,y=70)
Heading=Label(root,text="Localizador de telefono",font=("Arial",15,"bold"),fg="black",bg="white")
Heading.place(x=30,y=110)

#ENTRADA DE DATOS
Entry_back=PhotoImage(file="buscador.png")
Label(root,image=Entry_back).place(x=20,y=190)
entrada=StringVar()
meter_num=Entry(root,textvariable=entrada,width=17,bd=0,font=("Arial",20))
meter_num.place(x=50,y=220)

#BOTONOVICH
buscar_imagen=PhotoImage(file="search.png") 
search=Button(image=buscar_imagen,borderwidth=0,cursor="hand2",bd=0,font=("arial",16),command=buscar)
search.place(x=35,y=300)

#BOTTONBOX
box=PhotoImage(file="box.png")
Label(root,image=box).place(x=0,y=380)

pais=Label(root,text="País:",bg="#57adff",fg="black",font=("arial",10,"bold"))
pais.place(x=50,y=440)

sim=Label(root,text="SIM:",bg="#57adff",fg="black",font=("arial",10,"bold"))
sim.place(x=200,y=440)

zona=Label(root,text="Zona:",bg="#57adff",fg="black",font=("arial",10,"bold"))
zona.place(x=50,y=480)

clock=Label(root,text="Phone Time:",bg="#57adff",fg="black",font=("arial",10,"bold"))
clock.place(x=200,y=480)

longitud=Label(root,text="Longitud:",bg="#57adff",fg="black",font=("arial",10,"bold"))
longitud.place(x=50,y=520)

latitud=Label(root,text="Latitud:",bg="#57adff",fg="black",font=("arial",10,"bold"))
latitud.place(x=200,y=520)

root.mainloop()
