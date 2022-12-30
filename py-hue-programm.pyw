from phue import Bridge
import logging
import random
from tkinter import *
import time
from tkinter import colorchooser

cold_white = [0.37,0.38]
warm_white = [0.45,0.4]
blue = [0,0]
light_blue = [0.2,0.3]
purple = [0.5,0.2]
green = [0,1]
orange = [1,1]
red = [1,0]

color=""

def rancol():
    b.set_light(2, 'xy', [random.random(),random.random()])
    b.set_light(4, 'xy', [random.random(),random.random()])
    b.set_light(13, 'xy', [random.random(),random.random()])

def colpick():
    colpicker_1 = colorchooser.askcolor(title="Farbe wählen")
    colpicker_2 = colpicker_1[0]
    r = colpicker_2[0]
    g = colpicker_2[1]
    b = colpicker_2[2]
    rgb_to_xy(r,g,b)
 
def all_on():
    b.set_light(2, 'on', True)
    b.set_light(4, 'on', True)
    b.set_light(13, 'on', True)
    b.set_light(2, 'bri', 254)
    b.set_light(4, 'bri', 254)
    b.set_light(13, 'bri', 254)
def all_off():
    b.set_light(2, 'on', False)
    b.set_light(4, 'on', False)
    b.set_light(13, 'on', False)

def main_on():
    b.set_light(2, 'on', True)
def main_off():
    b.set_light(2, 'on', False)
def strips_on():
    b.set_light(4, 'on', True)
def strips_off():
    b.set_light(4, 'on', False)
def desklamp_on():
    b.set_light(13, 'on', True)
def desklamp_off():
    b.set_light(13, 'on', False)

def warm_white_b():
    color = warm_white
    set_color(color)
def cold_white_b():
    color = cold_white
    set_color(color)
def blue_b():
    color = blue
    set_color(color)
def green_b():
    color = green
    set_color(color)
def red_b():
    color = red
    set_color(color)
    
def set_color(color):
    b.set_light(2, 'xy', color)
    b.set_light(4, 'xy', color)
    b.set_light(13, 'xy', color)

def rgb_to_xy(r,g,b):
    X = 0.4124*r + 0.3576*g + 0.1805*b
    Y = 0.2126*r + 0.7152*g + 0.0722*b
    Z = 0.0193*r + 0.1192*g + 0.9505*b
    x = X / (X + Y + Z)
    y = Y / (X + Y + Z)
    color=[x,y]
    set_color(color)


logging.basicConfig()
b = Bridge('192.168.1.129')

window = Tk()
window.title("Hue Controller")
window.geometry("500x200")

menu = Menu(window)
window.config(menu=menu)
mymenu = Menu(menu)
menu.add_cascade(label="Special Effects", menu = mymenu)
mymenu.add_command(label="Random", command = rancol)
mymenu.add_command(label="Pick", command = colpick)

label_1 = Label(window, text="Zimmer:")
label_1.grid(row=0,column=0,padx=10,pady=10)

all_on_button = Button(window, text="Zimmer ein", command = all_on)
all_on_button.grid(row=1, column=0, padx=10)

all_off_button = Button(window, text="Zimmer aus", command = all_off)
all_off_button.grid(row=2, column=0, padx=10)


label_2 = Label(window, text="Farben:")
label_2.grid(row=0,column=1,padx=10,pady=10)

warm_white_button = Button(window, text="W Weiss", command = warm_white_b, bg="#fcddbf")
warm_white_button.grid(row=1,column=1,padx=10)

cold_white_button = Button(window, text="K Weiss", command = cold_white_b, bg="#fff9f4")
cold_white_button.grid(row=2,column=1,padx=10)

blue_button = Button(window, text="Blau", command = blue_b, bg="#4c63f7")
blue_button.grid(row=3,column=1,padx=10)

green_button = Button(window, text="Grün", command = green_b, bg="#26ed1c")
green_button.grid(row=4,column=1,padx=10)

red_button = Button(window, text="Rot", command = red_b, bg="#f71713")
red_button.grid(row=5,column=1,padx=10)


label_3 = Label(window, text="Lampen:")
label_3.grid(row=0,column=2,padx=10,pady=10)

main_on_b = Button(window, text="Main ein", command = main_on)
main_on_b.grid(row=1, column=2, padx=10)

main_off_b = Button(window, text="Main aus", command = main_off)
main_off_b.grid(row=1, column=3, padx=10)

strips_on_b = Button(window, text="Bett ein", command = strips_on)
strips_on_b.grid(row=2, column=2, padx=10)

strips_off_b = Button(window, text="Bett aus", command = strips_off)
strips_off_b.grid(row=2, column=3, padx=10)

desklamp_on_b = Button(window, text="Tisch ein", command = desklamp_on)
desklamp_on_b.grid(row=3, column=2, padx=10)

desklamp_off_b = Button(window, text="Tisch aus", command = desklamp_off)
desklamp_off_b.grid(row=3, column=3, padx=10)

window.mainloop()