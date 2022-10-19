import functions.getURL as getURL
import functions.downloadSong as downloadSong
import functions.system_checker
import os
from colorama import Fore

import os


def setup():
    try:
        os.mkdir("songs")
        print(Fore.GREEN + "Folder successfully created!")
        os.system("pause")
    except FileExistsError:
        print(Fore.GREEN + "The songs folder already exists, skipping...")
    except PermissionError():
        print(Fore.RED + "The program doesn't have permission to create a folder!\n Make sure that the user running the software has permission to write to this folder!")

def onRun():
    if os.path.exists("songs") == False:
        print(Fore.YELLOW + "Running first time setup, please wait...")
        setup()
        
    system = functions.system_checker.check()
    
    if system == 0:
        quit()
        
    while True:
        os.system("cls")
        print(Fore.CYAN + "Welcome to the Sleepy MP3 Downloader!")
        print(Fore.WHITE + "What would you like to do?")
        print(Fore.YELLOW + "1. Download a song by its name\n2. Download a song by its url")

        answer = input(Fore.BLUE + "Type here > ")

        if(answer == "1"):
            os.system("cls")
            wantedSongName = input(Fore.WHITE + "Type the name of the song you want to download > ")
            songURL = getURL.getSongUrlByName(wantedSongName)
            print("")
            downloadSong.get_mp3(songURL[0], songURL[1])

        elif(answer == "2"):
            #add code to automatically download the song from the fucntions.downloadsong using the url provided
            wantedSongURL = input(Fore.WHITE + "Type the url of the song you want to download > ")
            downloadSong.get_mp3(wantedSongURL, "")
        else:
            print(Fore.RED + "Please choose 1 or 2")
            os.system("pause")

if __name__ == "__main__":
    onRun()