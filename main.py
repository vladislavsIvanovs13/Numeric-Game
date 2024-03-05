from tkinter import *
import tkinter as tk
from tkinter import Canvas
from string_generator import Generator

class Main:
    def __init__(self, window):
        self.window = window
        self.window.title("Numeric Game")
        self.button = Button(window, text="Generate string", height=2, width=15,
                             command=self.display_string)
        self.button.place(x=180, y=510)
        self.canvas = Canvas(window, width=1000, height=300)
        self.canvas.configure(bg="MediumAquamarine")
        self.canvas.place(x=100, y=200)

    def display_string(self):
        string = Generator.generate_string(25)
        for number in string:
            print(number, end='')
        text = Text(window, bg="MediumAquamarine", height=1, width=37, font=('Times New Roman',25))
        text.insert(tk.END, string)
        text.place(x=280,y=340)
        
if __name__ == "__main__":
    window = Tk()
    window.geometry("1200x800")
    window.config(background="MediumSeaGreen")
    window.maxsize(1200, 800)
    Main(window)
    window.mainloop()

    