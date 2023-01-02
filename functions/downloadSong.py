import os
from colorama import Fore
import youtube_dl

def get_mp3(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    os.chdir("songs")

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    os.system("cls"); print(Fore.GREEN + "The song has been successfully downloaded!"); os.system("pause")