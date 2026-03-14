#               / Library

import os 
import json
import Library.LogicWeather
import customtkinter as ct

#               / Function

def StartLogic():
    city = CityEnter.get()
    Temperature = Library.LogicWeather.Magic(city)
    if Temperature == 1:
        TempText.configure(text="Invalid City Name!")
        CityEnter.delete(0, 'end')
        print("Invalid")
        return
    TempText.configure(text=Temperature) 
    CityEnter.delete(0, 'end')
    return

#               / Interface

ct.set_appearance_mode("dark")
ct.set_default_color_theme("blue")

Interface = ct.CTk()
Interface.title("Weather App")
Interface.geometry("500x300")

Welcomer = ct.CTkLabel(Interface, text="Welcome!", font=("Helvetica", 20))
Welcomer.grid(padx=200, pady=25)

CityEnter = ct.CTkEntry(Interface, placeholder_text="Enter City!", width=250, height=15, font=("Helvetica", 15))
CityEnter.grid(padx=0, pady=30)

CityAccept = ct.CTkButton(Interface, text="Look Up", width=150, height=15, font=("Helvetica", 15), command=StartLogic)
CityAccept.grid(padx=0, pady=0)

TempText = ct.CTkLabel(Interface, text="", font=("Helvetica", 20))
TempText.grid(padx=50, pady=30)
Interface.mainloop()

# -- Made by Methams