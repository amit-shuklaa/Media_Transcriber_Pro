import yt_dlp


def list_formats_and_download(url, format_id=None):
    try:
        # Extract video info to list formats
        with yt_dlp.YoutubeDL() as ydl:
            info_dict = ydl.extract_info(url, download=False)
            formats = info_dict.get('formats', [])

            # List all available formats
            print("Available formats:")
            for f in formats:
                print(f"Format ID: {f['format_id']}, Extension: {f['ext']}, Resolution: {f.get('format_note', 'N/A')}")

        # If a format_id is provided, download the specific format
        if format_id:
            ydl_opts = {'format': format_id}
        else:
            ydl_opts = {'format': 'best'}  # Default to best format

        # Download the video in the chosen format
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

    except Exception as e:
        print(f"Error: {e}")


# Example usage: Replace the URL with the desired YouTube video
video_url = "https://www.youtube.com/watch?v=H14bBuluwB8"
# list_formats_and_download(video_url)  # List formats
list_formats_and_download(video_url, format_id='396')
