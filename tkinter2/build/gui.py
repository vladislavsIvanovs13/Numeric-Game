
from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
# path r"C:\Users\kikap\OneDrive\Desktop\tkinter2\build\assets\frame0"
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"\tkinter2\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1440x1024")
window.configure(bg = "#1A1A1A")


canvas = Canvas(
    window,
    bg = "#1A1A1A",
    height = 1024,
    width = 1440,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    1764.638427734375,
    871.75,
    image=image_image_1
)

canvas.create_text(
    604.25,
    216.0,
    anchor="nw",
    text="Spēles Noteikumi ",
    fill="#FFFFFF",
    font=("AnonymousPro Bold", 24 * -1)
)

canvas.create_text(
    316.25,
    288.75,
    anchor="nw",
    text="Spēles sākumā ir dota ģenerētā skaitļu virkne.",
    fill="#FFFFFF",
    font=("AnonymousPro Regular", 13 * -1)
)

canvas.create_text(
    316.25,
    324.75,
    anchor="nw",
    text="Katram spēlētājam ir 0 punktu spēles sākumā.",
    fill="#FFFFFF",
    font=("AnonymousPro Regular", 13 * -1)
)

canvas.create_text(
    316.25,
    360.75,
    anchor="nw",
    text="Gājiena laikā spēlētājs var - saskaitīt skaitļu pāri un summu ierakstīt saskaitīto skaitļu pāra  vietā\nkā arī pieskaitīt savam punktu skaitam 1 punktu, VAI nodzēst to skaitli, kas ir palicis bez pāra\nun atņemt vienu punktu no sava punktu skaita.",
    fill="#FFFFFF",
    font=("AnonymousPro Regular", 13 * -1)
)

canvas.create_text(
    316.25,
    423.75,
    anchor="nw",
    text="Spēle beidzas, kad skaitļu virknē paliek viens skaitlis.",
    fill="#FFFFFF",
    font=("AnonymousPro Regular", 13 * -1)
)

canvas.create_text(
    316.25,
    459.75,
    anchor="nw",
    text="UZVAR SPĒLĒTĀJS, KAM IR VAIRĀK PUNKTI.",
    fill="#FFFFFF",
    font=("AnonymousPro Bold", 13 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=303.5,
    y=696.75,
    width=133.5,
    height=39.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=600.5,
    y=689.25,
    width=216.75,
    height=54.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=980.75,
    y=696.75,
    width=133.5,
    height=39.0
)

canvas.create_rectangle(
    305.75,
    584.25,
    1114.25,
    638.25,
    fill="#FFFFFF",
    outline="")

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    556.25,
    228.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    236.375,
    612.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    236.0,
    441.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    1184.0,
    285.75,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    1184.0,
    441.0,
    image=image_image_6
)

canvas.create_text(
    305.75,
    516.0,
    anchor="nw",
    text="COMPUTER",
    fill="#FFFFFF",
    font=("AnonymousPro Bold", 18 * -1)
)

canvas.create_text(
    427.25,
    501.75,
    anchor="nw",
    text="0",
    fill="#FFFFFF",
    font=("AnonymousPro Bold", 36 * -1)
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=643.25,
    y=507.0,
    width=133.5,
    height=39.0
)

canvas.create_text(
    1036.25,
    516.0,
    anchor="nw",
    text="USER",
    fill="#FFFFFF",
    font=("AnonymousPro Bold", 18 * -1)
)

canvas.create_text(
    1094.0,
    507.0,
    anchor="nw",
    text="0",
    fill="#FFFFFF",
    font=("AnonymousPro Bold", 36 * -1)
)

canvas.create_text(
    349.625,
    57.0,
    anchor="nw",
    text="Choose who starts",
    fill="#FFFFFF",
    font=("AnonymousPro Bold", 24 * -1)
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)
button_5.place(
    x=303.5,
    y=126.75,
    width=133.5,
    height=39.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_6 clicked"),
    relief="flat"
)
button_6.place(
    x=485.0,
    y=126.75,
    width=133.5,
    height=39.0
)

canvas.create_text(
    851.75,
    57.0,
    anchor="nw",
    text="Choose algorithm",
    fill="#FFFFFF",
    font=("AnonymousPro Bold", 24 * -1)
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_7 clicked"),
    relief="flat"
)
button_7.place(
    x=799.25,
    y=126.75,
    width=133.5,
    height=39.0
)

button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_8 clicked"),
    relief="flat"
)
button_8.place(
    x=980.75,
    y=126.75,
    width=133.5,
    height=39.0
)
window.resizable(False, False)
window.mainloop()
