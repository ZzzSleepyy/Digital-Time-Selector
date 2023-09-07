from tkinter import *
import tkinter as tk
from tkinter import ttk
import time
from PIL import ImageTk, Image
import pytz
from datetime import datetime

window = tk.Tk()
window.configure(bg='#0C090A')
window.geometry('500x200')
window.resizable(0,0)
window.attributes('-transparentcolor', '#0C090A')
window.title("Time selector 0.1")


click_menu = PhotoImage(file='pack/menu.png')
menu_okay = Image.open("pack/menu.png")
resized = menu_okay.resize((40,40))

click_x = PhotoImage(file='pack/x.png')
x_okay = Image.open("pack/x.png")
resized_x = x_okay.resize((40,40))


button_x = ImageTk.PhotoImage(resized_x)
button_menu = ImageTk.PhotoImage(resized)


def win_toggle():
    label1=tk.Label(bg='#DCDEE5', width=40, height=100,)
    label1.place(x=0,y=0)
    
    label2=tk.Label(label1, text = 'Nicko', bg='#DCDEE5',font=("Segoe Script", 15))
    label2.place(x=73,y=50)
    
    def dele():
        label1.destroy()
        switch.destroy()
    def toggle():
        window.destroy()
        
    open = tk.Button(label1, image=button_x, borderwidth=0, command=dele, bg= '#DCDEE5')
    open.place(x=0,y=0)
    
    switch = tk.Button(window, text='Exit', bd=0, bg="white", activebackground="white", width=20,height=3, command=toggle or win_toggle)
    switch.place(x=50,y=100)


menu_button = tk.Button(window, command= win_toggle, image=button_menu ,border=0, activebackground= '#0C090A', bg = '#0C090A')
menu_button.place(x=0,y=0)

def present():
    selected_timezone = timezone_label.cget("text")
    if selected_timezone:
        timezone = pytz.timezone(selected_timezone)
        current_time = datetime.now(timezone) 
        display_t = current_time.strftime('%I:%M:%S %p')
        digital_clock.config(text=display_t)
    digital_clock.after(200, present)

def search_timezones_by_country(event):
    selected_country = country_combobox.get() 
    selected_country_code = country_codes.get(selected_country)

    matching_timezones = pytz.country_timezones.get(selected_country_code, [])
    
    if matching_timezones:
        timezone_label.config(text=matching_timezones[0])
    else:
        timezone_label.config(text="")

digital_clock = tk.Label(window, width=10, height=2, font=("Comic Sans MS", 40), bg='#0C090A', fg='#C9C0BB')
digital_clock.pack()

country_names = list(pytz.country_names.values())
country_codes = {name: code for code, name in pytz.country_names.items()}

country_combobox = ttk.Combobox(window, values=country_names, font=("Comic Sans MS", 12))
country_combobox.set("Philippines") 
country_combobox.bind("<<ComboboxSelected>>", search_timezones_by_country)
country_combobox.place(y=120, x=145)

timezone_label = tk.Label(window, text="Asia/Manila", font=("Comic Sans MS", 14), bg='#0C090A', fg='#C9C0BB', anchor=tk.CENTER)
timezone_label.place(y=175)

present()
window.mainloop()