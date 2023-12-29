from customtkinter import *
from tube import *

app = CTk()
app.geometry("500x500")

set_appearance_mode("dark")

entry = CTkEntry(master=app, placeholder_text="Ingresa el link del video", width = 300)
entry.place(relx=0.5, rely=0.5, anchor="center")

btn = CTkButton(master=app, text="Descargar audio", corner_radius=0, fg_color="#C70039", hover_color="#FF5733", border_width=2, command=lambda: process_link(entry.get()))
btn.place(relx = 0.5, rely = 0.7, anchor = "center")

app.mainloop()
