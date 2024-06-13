import yt_dlp
import os

cookies_file = 'cookies.txt'
video_url = 'https://www.youtube.com/watch?v=xH0AlPxeb0M'

ydl_opts = {
    'cookiefile': cookies_file,
    'outtmpl': '%(title)s.%(ext)s',
    'format': 'best',
}

def download_video(url):
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == '__main__':
    download_video(video_url)
