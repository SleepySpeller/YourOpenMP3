import os
from colorama import Fore
import youtube_dl
import time



def getStatus(arg1):
    # Data looks something like this while downloading:
    """{'status': 'downloading', 'downloaded_bytes': 64512, 'total_bytes': 387802,
    'tmpfilename': 'Perspektiva-tgYV7AvNF-g.m4a.part', 'filename': 'Perspektiva-tgYV7AvNF-g.m4a',
    'eta': 3, 'speed': 90751.2840969309, 'elapsed': 0.7741024494171143, '_eta_str': '00:03',
    '_percent_str': ' 16.6%', '_speed_str': '88.62KiB/s', '_total_bytes_str': '378.71KiB'}
    """
    pass

def get_mp3(url, downloaded_label, downloading_label):
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

    downloading_label.pack(pady=50, padx=10)

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


    os.chdir(oldpath)

    downloading_label.pack_forget()
    downloaded_label.pack(pady=50, padx=10)

    time.sleep(3)
    downloaded_label.pack_forget()
    # os.system("cls"); print(Fore.GREEN + "The song has been successfully downloaded!"); os.system("pause")