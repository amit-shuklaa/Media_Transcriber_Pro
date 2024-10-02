import yt_dlp # if you don't have the yt-dlp package then first install it to use this.You can use pip install yt-dlp

def download_video(url):
    ydl_opts = {'format': 'best'}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

download_video("https://youtu.be/LRaU4rEna8s?si=sa1lmPUBodZC8N1a") # Here you have to paste the link of your Youtube video which you have to download
