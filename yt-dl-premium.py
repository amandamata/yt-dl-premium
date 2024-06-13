import yt_dlp
import os

cookies_file = '/home/user/Documents/cookies.txt'
video_url = 'https://www.youtube.com/watch?v=7X8II6J-6mU'
output_folder = '/home/user/Videos/yt'

ydl_opts = {
    'cookiefile': cookies_file,
    'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'),
    'format': 'best',
}

def download_video(url):
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == '__main__':
    download_video(video_url)
