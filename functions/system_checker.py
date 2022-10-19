import urllib.request
import os

def check():
    def connect(host='http://google.com'):
        try:
            urllib.request.urlopen(host) #Python 3.x
            return True
        except:
            return False
        
    internet = connect()
    
    if not internet:
        print("No internet connection!")
        os.system("pause")
        return 0

    return 1
        