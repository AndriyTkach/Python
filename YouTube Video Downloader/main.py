from pytube import YouTube
import os

url = ''
my_video = YouTube(url)

print(my_video.title)

print(my_video.thumbnail_url)

a = int(input("Audio (1) or Video (2) : "))

if a == 1:
    audio = my_video.streams.filter(only_audio=True).first()

    out_file = audio.download(output_path=".")

    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)

elif a == 2:
    my_video = my_video.streams.get_highest_resolution()

    my_video.download(output_path=".")
