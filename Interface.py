
#                           /// Essentials ///

#               / Library
import os 
import json
import Libr.Matfile
import Libr.LogicWeather
import customtkinter as ct

#LEARNINGSHEET///LEARNINGSHEET///LEARNINGSHEET///LEARNINGSHEET///LEARNINGSHEET///LEARNINGSHEET///LEARNINGSHEET///LEARNINGSHEET///
#   Will use CustomTkinter
# Label = shows text
# Entry = user input
# Button = sends you 2026 porsche if you wish hard enough
# Root = the window objects are on
# pack() = put this on the last one
#
# Entry logic
# entryBox = ct.CTKEntry(root1)
# entered = entryBox.get()
#
# Button logic 
# def someFunction():
#       print("this that")
# button1 = ct. CTKButton(root, text="Click this", command=someFunction)

def StartLogic():
    city = CityEnter.get()
    Temperature = Libr.LogicWeather.Magic(city)
    if Temperature == 1:
        TempText.configure(text="Invalid City Name!")
        CityEnter.delete(0, 'end')
        print("Invalid")
        return
    TempText.configure(text=Temperature) 
    CityEnter.delete(0, 'end')
    return


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

