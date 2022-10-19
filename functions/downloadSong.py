from pytube import YouTube
import os
from colorama import Fore

def get_mp3(url, title):
    try:
        my_video = YouTube(url)
    except Exception as e:
        print(Fore.RED + "An error has occured while trying to donwload your song! " + e)
        os.system("pause")
    
    
    try:
        audio = my_video.streams.get_audio_only()
        myAudio = my_video.streams.filter(only_audio=True).first().download(filename = "songs/" + title + ".mp3")
        print(Fore.GREEN + f"The song \"{title}\" has been downloaded successfully!")
        os.system("pause")
    except Exception as exception:
        print(Fore.RED + "An error has occured!" + exception)
        os.system("pause")