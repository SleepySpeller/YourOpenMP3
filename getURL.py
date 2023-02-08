import urllib.request
from pytube import YouTube
import re
from colorama import Fore
import os

def getSongUrlByName(wantedSongName):
    finalSearchURL = "https://www.youtube.com/results?search_query="

    wantedSongName = wantedSongName.split(" ")

    for i in range(len(wantedSongName)):
        if(i == 0):
            finalSearchURL = finalSearchURL +  wantedSongName[i]
            continue

        finalSearchURL = finalSearchURL + "+" + wantedSongName[i]


    html = urllib.request.urlopen(finalSearchURL)
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())

    for i in range(len(video_ids)):
        finalURL = "https://www.youtube.com/watch?v=" + video_ids[i]

        my_video = YouTube(finalURL)
        title = my_video.title

        print(title)

        answer = input(Fore.YELLOW + "Is the song correct? (y/n)")
        if answer == "y":
            return finalURL
        os.system("cls")