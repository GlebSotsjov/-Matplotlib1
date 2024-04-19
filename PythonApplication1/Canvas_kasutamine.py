import tkinter as tk
from tkinter import font
from random import choice

def draw_estonian_flag(canvas):
    # Отрисовка голубой полосы
    canvas.create_rectangle(0, 0, 300, 100, fill="#0072CE", width=0)
    
    # Отрисовка черной полосы
    canvas.create_rectangle(0, 100, 300, 200, fill="#000000", width=0)
    
    # Отрисовка белой полосы
    canvas.create_rectangle(0, 200, 300, 300, fill="#FFFFFF", width=0)

def draw_bahamas_flag(canvas):
    # Отрисовка треугольника синего цвета
    canvas.create_polygon(0, 0, 300, 150, 0, 300, fill="#000080", outline="")

    # Отрисовка треугольника желтого цвета
    canvas.create_polygon(0, 0, 150, 150, 0, 300, fill="#FFD700", outline="")

    # Отрисовка треугольника черного цвета
    canvas.create_polygon(300, 0, 150, 150, 300, 300, fill="#000000", outline="")

raam = tk.Tk()
raam.title("tahvel")

# Создание холста для флага
flag_canvas = tk.Canvas(raam, width=300, height=300, background="white")
flag_canvas.grid(row=0, column=0)

# Отрисовка флага
draw_estonian_flag(flag_canvas)

# Создание холста для остальных элементов
tahvel = tk.Canvas(raam, width=600, height=600, background="white")
tahvel.grid(row=0, column=1)

# Отрисовка флага Багамских островов
draw_bahamas_flag(tahvel)

# tõmbab крипсы, ühendаб остапунктиd ja väрвиb сису
# väрве saab määrata ka rgb компонентидена
# vt. http://www.colorpicker.com/а
tahvel.create_line(30, 40, 300, 40)
tahvel.create_line(30,60,  300,60,  300,100,  60,100)
tahvel.create_line(30, 130, 300, 130, width=4, fill="red")
tahvel.create_line(30, 150, 300, 150, width=5, dash=(5, 1, 2, 1), arrow=tk.LAST)
tahvel.create_polygon(30,160,  300,160,  300,200,  60,200, fill="#95BD9D")
tahvel.create_rectangle(30,260,  300,300)
tahvel.create_oval(30,260,  300,300, width=2, outline="blue", fill="wheat")
tahvel.create_oval(330, 330, 400, 400, fill="gray", activefill="pink")
suur_font = font.Font(family='Helvetica', size=32, weight='bold')
tahvel.create_text(30, 500, text="Tere!", font=suur_font, anchor=tk.NW)

colors =["black",
         "cyan",
         "magenta",
         "red",
         "blue",
         "gray",
         "yellow",
         "green",
         "lightblue",
         "pink",
         "gold"]
x0=0
y0=0
x1=600
y1=600
p=2
for i in range(150):
    x0+=p
    y0+=p
    x1-=p
    y1-=p
    tahvel.create_oval(x0,y0,x1,y1, fill=choice(colors))

raam.mainloop()
