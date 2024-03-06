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

# City Name:
city_label = tk.Label(root, font=("arial", 30, "bold"), fg="#e355cd")

city_label.place(x=120, y=160)

# Time:
time_label = tk.Label(root, font=("arial", 15, "bold"), fg="#e355cd")

time_label.place(x=120, y=230)

clock_label = tk.Label(root, font=("arial", 15, "bold"), fg="#e355cd")

clock_label.place(x=120, y=270)

# Labels :
label_one = tk.Label(root, text="WIND", font=("Helvetica", 13, "bold"),
                     fg="white", bg="#1ab5ef")

label_one.place(x=140, y=400)

label_two = tk.Label(root, text="HUMINITY", font=("Helvetica", 13, "bold"),
                     fg="white", bg="#1ab5ef")

label_two.place(x=280, y=400)

label_three = tk.Label(root, text="DESCRIPTION", font=("Helvetica", 13, "bold"),
                       fg="white", bg="#1ab5ef")

label_three.place(x=450, y=400)

label_four = tk.Label(root, text="PRESSURE", font=("Helvetica", 13, "bold"),
                      fg="white", bg="#1ab5ef")

label_four.place(x=650, y=400)

temp_label = tk.Label(root, font=("arial", 70, "bold"), fg="#e355cd")

temp_label.place(x=590, y=170)

condition_label = tk.Label(root, font=("arial", 15, "bold"), fg="#4b4bcc")

condition_label.place(x=590, y=270)

wind_label = tk.Label(root, text="...", font=("arial", 20, "bold"),
                      bg="#1ab5ef", fg="#404040")

wind_label.place(x=140, y=430)

humidity_label = tk.Label(root, text="...", font=("arial", 20, "bold"),
                          bg="#1ab5ef", fg="#404040")

humidity_label.place(x=280, y=430)

description_label = tk.Label(root, text="...", font=("arial", 20, "bold"),
                             bg="#1ab5ef", fg="#404040")

description_label.place(x=450, y=430)

pressure_label = tk.Label(root, text="...", font=("arial", 20, "bold"),
                             bg="#1ab5ef", fg="#404040")

pressure_label.place(x=650, y=430)

root.mainloop()
