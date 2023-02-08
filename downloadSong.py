import os
from colorama import Fore
import youtube_dl
import time
import json

progressbar = ''
speed_label = ''


downloadArgument = {}

def getStatus(arg1):
    
    try:
        args = arg1.get("_percent_str"); args = args[1:3] ;args = int(args) ;args = args/100
        progressbar.set(args)
        speed_label.configure(text="Download speed: " + arg1.get("_speed_str"))
    except:
        progressbar.pack_forget()  
        speed_label.pack_forget()  
    
def get_mp3(url, downloaded_label, downloading_label, progress_bar, speedlabel):
    downloading_label.pack(pady=10, padx=10)
    global progressbar
    global speed_label
    progressbar = progress_bar
    progressbar.pack(padx=20, pady=10)
    progressbar.set(0)
    speed_label = speedlabel
    speed_label.pack(padx=20, pady=0)
    
    ydl_opts = {
        'format': 'bestaudio/best',
        'progress_hooks': [getStatus],
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192', 
        }],
    }
    oldpath = os.getcwd()
    os.chdir("songs")

    

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


    os.chdir(oldpath)

    downloading_label.pack_forget()
    downloaded_label.pack(pady=10, padx=10)

    time.sleep(3)
    downloaded_label.pack_forget()