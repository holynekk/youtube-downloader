from pytube import YouTube

yt_link = input("Enter the video link: ")

yt_obj = YouTube(yt_link)

for stream in yt_obj:
    print(stream)

