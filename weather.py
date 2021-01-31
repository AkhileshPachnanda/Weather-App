import tkinter as tk
from tkinter import * 
from tkinter.font import Font
from PIL import ImageTk,Image
from configparser import ConfigParser
from tkinter import messagebox
import requests
import json
from PIL import Image
from io import BytesIO
root=tk.Tk()
root.title('Weather')
root.geometry("200x200")
root.iconbitmap('favicon_YRi_icon.ico')
url="http://api.weatherapi.com/v1/current.json?key={}&q={}"
config_file='config.ini'
config = ConfigParser()
config.read (config_file)
api_key = config['api_key']['key']


def getweather(city):

    result = requests.get(url.format(api_key,city))
    api= result.json()
    if result:
            city = api["location"]["name"]
            country = api["location"]["country"]
            temp = api["current"]["temp_c"] 
            icon= api["current"]["condition"]["code"]  
            weather = api["current"]["condition"]["text"]
            final =(city, country, temp , icon, weather)
            return final
    else:
        return None
    
Label(root, text="", bg= "#1a1a1a").pack()
myfont3 = Font(family="Poppins-bold", size = 10)

city_text=StringVar()
city_entry= Entry(root,textvariable=city_text, bg="#1a1a1a", bd=0.6, fg = "white", font=myfont3)
city_entry.pack()
def search():
    city = city_text.get()
    weather = getweather(city)
    if weather:
        location_lbl["text"] = "{}" .format(weather[0])
        temp_lbl["text"] = "{:.0f}°C".format(weather[2])

        weather_lbl["text"] = "{}".format(weather[4])
    
    else:
        messagebox.showerror("error")



myFont1 = Font(family="Poppins-bold", size=16)
myFont2 = Font(family="Poppins-bold", size=12)
myFont4 = Font(family="Poppins-medium", size=10)
myFont = Font(family="Poppins-bold", size=21)

search_btn=Button(root, text="Search", bd= 0, fg = "white" , bg= "#1a1a1a" , command=search, font=myFont4)
search_btn.pack()

location_lbl= Label(root, text= "", fg = "white" , bg= "#1a1a1a",  font=myFont)
location_lbl.pack()

temp_lbl= Label(root, text = "", fg = "white" , bg= "#1a1a1a", font=myFont1)
temp_lbl.pack()

weather_lbl = Label(root, text = "", fg = "white" , bg= "#1a1a1a", font=myFont2)
weather_lbl.pack()

root["bg"] = "#1a1a1a"
root.mainloop() 
