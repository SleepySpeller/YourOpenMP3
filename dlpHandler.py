# Refactor of downloadSong.py

import os
import yt_dlp

progressbar = ''
speed_label = ''

def my_hook(d):
    print("Hook called!")
    
    # Uncommend if making a dump
    # Make sure logs.txt exists in advance!
    # f = open("logs.txt", "a", encoding="utf-8")
    # f.write(str(d))
    # f.close()
    
    global progressbar
    global speed_label
    
    print("Speed str: " + d['_speed_str'])
    print("Percent str: " + d['_percent_str'])
    
    if d['status'] == 'finished':
        print("Download done!")
        progressbar.pack_forget()
        speed_label.configure(text="Waiting for FFmpeg...")
        speed_label.pack(padx=10, pady=10)
        
    elif d['status'] == 'downloading':
        print("Download is in progress!")
        
        downloadSpeed = str(d['_speed_str'])
        percentage = str(d['_percent_str'])
        
        finalText = percentage[7:-4] + " downloaded at speed " + downloadSpeed[8:-4]
        
        # TODO
        # if d['playlist'] == None:
        #     speed_label.configure(text=finalText)
        # else:
        #     speed_label.configure(text="Downloading from playlist " + d['playlist'] + "\n" + finalText)
        
        speed_label.configure(text=finalText)
        speed_label.pack(pady=10, padx=10)
    
def get_mp3(url, download_status, progress_bar):
    global progressbar
    global speed_label
    
    progressbar = progress_bar
    speed_label = download_status
    
    ydl_opts = {
        'format': 'mp3/bestaudio/best',
        'progress_hooks': [my_hook],
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
        }]
    }   
    
    os.chdir("songs")
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        error_code = ydl.download(url)
        
    download_status.configure(text="Download finished!")
    download_status.pack(padx=10, pady=10)
        
    os.chdir("../")