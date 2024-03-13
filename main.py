from tkinter import *
import tkinter as tk
from tkinter import Canvas
from string_generator import Generator

class Main:
    def __init__(self, window):
        self.window = window
        self.window.title("Numeric Game")
        rules_text = """Spēles Noteikumi - Spēles sākumā ir dota ģenerētā skaitļu virkne.
        Spēlētāji izpilda gājienus pēc kārtas.
        Katram spēlētājam ir 0 punktu spēles sākumā.
        Gājiena laikā spēlētājs var - saskaitīt skaitļu pāri un summu ierakstīt saskaitīto skaitļu pāra vieta vietā
        kā arī pieskaitīt savam punktu skaitam 1 punktu, VAI nodzēst to skaitli, kas ir palicis bez pāra
        un atņemt vienu punktu no sava punktu skaita.
        Spēle beidzas, kad skaitļu virknē paliek viens skaitlis.
        UZVAR SPĒLĒTĀJS, KAM IR VAIRĀK PUNKTI."""

        rules_label = Label(window, text=rules_text, font=('Times New Roman', 12), justify=LEFT)
        rules_label.place(x=180, y=20)
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


    
