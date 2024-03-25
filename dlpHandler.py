# Refactor of downloadSong.py

import os
import yt_dlp

speed_label = ''
playlist_label = ''
song_label = ''

def my_hook(d):
    # Uncommend if making a dump
    # Make sure logs.txt exists in advance!
    # f = open("logs.txt", "a", encoding="utf-8")
    # f.write(str(d))
    # f.close()
    
    global progressbar
    global speed_label
    global playlist_label
    global song_label
    
    if d['status'] == 'finished':
        speed_label.configure(text="Waiting for FFmpeg...")
        speed_label.pack(padx=10, pady=10)
        
    elif d['status'] == 'downloading':
        downloadSpeed = str(d['_speed_str'])
        percentage = str(d['_percent_str'])
        
        speed_label.configure(text=percentage[7:-4] + " downloaded at speed " + downloadSpeed[8:-4])
        speed_label.pack(pady=10, padx=10)
        
        song_label.configure(text="Downloading: " + d['info_dict']['title'])
        song_label.pack(pady=0, padx=10)
        
        if 'playlist_title' in d['info_dict']:
            playlist_label.configure(text="Playlist: " + d['info_dict']['playlist_title'])
            playlist_label.pack(pady=0, padx=10)

    
def get_mp3(url, download_status, playlist_status, song_status):
    global speed_label
    global playlist_label
    global song_label
    speed_label = download_status
    playlist_label = playlist_status
    song_label = song_status
    
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
    playlist_status.pack_forget()
    song_label.pack_forget()
        
    os.chdir("../")