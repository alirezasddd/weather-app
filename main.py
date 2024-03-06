import tkinter as tk
from tkinter import messagebox
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz


def get_weather():
    pass

# Basic window


root = tk.Tk()
root.title("Weather App")
root.geometry("900x490+300+200")
root.resizable(False, False)

# Search line
search_line = tk.PhotoImage(file="search.png")
search_line_lable = tk.Label(root, image=search_line)
search_line_lable.pack(pady=20, side=tk.TOP)

text_fild = tk.Entry(root, justify="center", width=17,
                     font=("poppins", 25, "bold"),
                     bg="#404040", fg="white", border=0)

text_fild.place(x=280, y=40)

search_icon = tk.PhotoImage(file="search_icon.png")
search_icon_button = tk.Button(root, image=search_icon, border=0,
                               cursor="hand2", bg="#404040", command=get_weather)

search_icon_button.place(x=540, y=34)

# logo:
logo_image = tk.PhotoImage(file="logo.png")
logo_label = tk.Label(root, image=logo_image)
logo_label.pack(side=tk.TOP)

# Botton box:
frame_image = tk.PhotoImage(file="box.png")
frame_label = tk.Label(root, image=frame_image)
frame_label.pack(pady=6, side=tk.BOTTOM)


root.mainloop()
