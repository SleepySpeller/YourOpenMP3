import customtkinter
from functions import downloadSong, getURL
import threading

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
        b = threading.Thread(name="background_download", target=downloadSong.get_mp3, args=(text,downloaded_label, downloading_label,))
        b.start()

def test():
    print(downloadSong.getStatus())

label_1 = customtkinter.CTkLabel(master=frame_1, justify=customtkinter.LEFT, text="YourOpenMP3", font=('segoe', 35))
label_1.pack(pady=5, padx=10)

label_2 = customtkinter.CTkLabel(master=frame_1, justify=customtkinter.LEFT, text="MP3 Downloader for all your needs!")
label_2.pack(pady=0, padx=10)

textbox = customtkinter.CTkTextbox(master=frame_1, corner_radius=3, width=500, height=25)
textbox.pack(pady=10, padx=10)

button_1 = customtkinter.CTkButton(master=frame_1, command=button_download, text="Download!")
button_1.pack(pady=10, padx=10)

button_dwnld = customtkinter.CTkButton(master=frame_1, command=test, text="Test progress bar")
button_dwnld.pack(pady=10, padx=10)

downloading_label = customtkinter.CTkLabel(master=frame_1, text="Downloading, please wait...")

downloaded_label = customtkinter.CTkLabel(master=frame_1, text="Download complete!")

app.mainloop()