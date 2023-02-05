from tkinter import *
from pytube import YouTube

def download_video():
    link = entry.get()
    youtube = YouTube(link)
    video = youtube.streams.first()
    video.download()
    label.config(text="Pobieranie zakończyło się pomyślnie")

def download_audio():
    link = entry.get()
    youtube = YouTube(link)
    audio = youtube.streams.filter(only_audio=True).first()
    audio.download()
    label.config(text="Pobieranie zakończyło się pomyślnie")

root = Tk()
root.title("YouTube downloader")

entry = Entry(root, width=50)
entry.pack()

video_button = Button(root, text="Pobierz wideo", command=download_video)
video_button.pack()

audio_button = Button(root, text="Pobierz audio", command=download_audio)
audio_button.pack()

label = Label(root, text="")
label.pack()

root.mainloop()
