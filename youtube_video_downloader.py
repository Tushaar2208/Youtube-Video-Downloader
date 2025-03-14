import yt_dlp
import os

def download_video(url):
    desktop_path = os.path.expanduser("~/Desktop") 
    ydl_opts = {
        'verbose': True, 
        'outtmpl': os.path.join(desktop_path, '%(title)s.%(ext)s')
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([url])
            print("Video downloaded to desktop!")
        except Exception as e:
            print(f"An error occurred: {e}")


url = input("Paste YouTube video URL here: ")

download_video(url)
