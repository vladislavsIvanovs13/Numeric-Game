# This will be the main file that runs our application.

from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import Canvas
from numpy import asarray
import numpy as np
import random

window = Tk()
window.title("Numeric Game")
window.geometry("1200x800")
window.config(background="MediumSeaGreen")
window.maxsize(1200, 800)

def create_canvas():
    canvas1 = Canvas(window, width=1000, height=300)
    canvas1.configure(bg="MediumAquamarine")
    canvas1.place(x=100, y=200)

create_canvas()

window.mainloop()
