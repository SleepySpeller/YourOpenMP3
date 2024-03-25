import customtkinter

import dlpHandler
import threading

import os

# Init folder
try:
    if not os.path.isdir("songs"):
        os.mkdir("songs")
except Exception as e:
    print("Error in creating songs folder!\n" + e)

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

app = customtkinter.CTk()
app.geometry("800x600")
app.title("YourOpenMP3")

frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)


def button_download():
    text = textbox.get("1.0", "end-1c")
    if text[:8] == 'https://':
        download_status.configure(text="Preparing...")
        download_status.pack(padx=10, pady=10)
        
        b = threading.Thread(name="background_download", target=dlpHandler.get_mp3, args=(text, download_status, progressbar))
        b.start()

title = customtkinter.CTkLabel(master=frame_1, justify=customtkinter.LEFT, text="YourOpenMP3", font=('segoe', 35))
title.pack(pady=5, padx=10)

subtitle = customtkinter.CTkLabel(master=frame_1, justify=customtkinter.LEFT, text="MP3 Downloader for all your needs!")
subtitle.pack(pady=0, padx=10)

textbox = customtkinter.CTkTextbox(master=frame_1, corner_radius=3, width=500, height=25)
textbox.pack(pady=10, padx=10)

download_button = customtkinter.CTkButton(master=frame_1, command=button_download, text="Download!")
download_button.pack(pady=10, padx=10)

progressbar = customtkinter.CTkProgressBar(master=frame_1)

download_status = customtkinter.CTkLabel(master=frame_1, justify=customtkinter.LEFT, text="Preparing...")

app.mainloop()