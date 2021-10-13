# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 11:40:18 2021

@author: hugod
"""

from tkinter import *
from tkinter import messagebox
import time
count=0
board=[['','','',],['','','',],['','','',]]

def create_cross(x, y, canvasName):
    canvasName.create_line(x - 100, y - 100, x + 100, y + 100  )
    canvasName.create_line(x + 100, y - 100, x - 100, y + 100  )

def create_circle(x, y, r, canvasName): #center coordinates, radius
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvasName.create_oval(x0, y0, x1, y1, outline='blue')

def create_grid(event=None):
    w = c.winfo_width() # Get current width of canvas
    h = c.winfo_height() # Get current height of canvas
    c.delete('grid_line') # Will only remove the grid_line

    # Creates all vertical lines at intevals of 100
    for i in range(0, w, 300):
        c.create_line([(i, 0), (i, h)], tag='grid_line')

    # Creates all horizontal lines at intevals of 100
    for i in range(0, h, 300):
        c.create_line([(0, i), (w, i)], tag='grid_line')

root = Tk()

c = Canvas(root, height=900, width=900, bg='white')
c.pack(fill=BOTH, expand=True)

c.bind('<Configure>', create_grid)

create_circle(150,150, 100, c)
create_cross(450, 450, c)
root.mainloop()


    
    