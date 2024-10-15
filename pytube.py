import yt_dlp


def download_all_formats(url):
    # List and download all available formats
    ydl_opts = {
        'format': 'all',  # Download all formats
        'outtmpl': '%(title)s-%(format_id)s.%(ext)s',  # Name the file with the format ID and extension
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


# Replace this with your YouTube video link
download_all_formats("https://youtu.be/6-1CwFumx_M?si=lFSECAEm8GR5p6ch")
