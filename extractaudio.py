from moviepy.editor import VideoFileClip


video = VideoFileClip("video.mp4") #Here you have to specify the name of the video that you have downloded.
audio = video.audio
audio.write_audiofile("extracted_audio.mp3") # You can change the name of the file according to you
video.close()
