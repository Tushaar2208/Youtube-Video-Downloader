import yt_dlp
import os

def download_video(url):
    desktop_path = os.path.expanduser("~/Desktop")  
    ydl_opts = {
        'verbose': True, 
        'format': 'bestvideo[height<=1080]+bestaudio/best',  
        'merge_output_format': 'mp4', 
        'outtmpl': os.path.join(desktop_path, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',
        }]
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([url])
            print("Video downloaded in 1080p to desktop!")
        except Exception as e:
            print(f"An error occurred: {e}")


url = input("Paste YouTube video URL here: ")
download_video(url)
