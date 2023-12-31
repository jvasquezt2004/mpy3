from customtkinter import *
from tube import *

app = CTk()
app.geometry("500x500")

set_appearance_mode("dark")
set_default_color_theme("GhostTrain.json")

audio = CTkFrame(master=app, border_width=2)
audio.pack(expand=True)

label_audio = CTkLabel(master=audio, text="Descargar de youtube")
entry = CTkEntry(master=audio, placeholder_text="Ingresa el link del video", width = 300)
btn_audio = CTkButton(master=audio, text="Descargar audio", corner_radius=0, border_width=2, command=lambda: process_link_audio(entry.get()))
btn_video = CTkButton(master=audio, text="Descargar video", corner_radius=0, border_width=2, command=lambda: process_link_video(entry.get()))

label_audio.pack(anchor="s", expand=True, pady=10, padx=30)
entry.pack(anchor="s", expand=True, pady=10, padx=30)
btn_audio.pack(anchor="n", expand=True, pady=30, padx=20)
btn_video.pack(anchor="n", expand = True, pady=30, padx=20)

app.mainloop()
