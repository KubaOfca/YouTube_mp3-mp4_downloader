from __future__ import unicode_literals
import youtube_dl
import tkinter as tk
from tkinter import filedialog as fd

def download(link, is_mp3):
    path = output_dir_entry.get()

    MP3_OPTS = {
        'format': 'bestaudio/best',
        'outtmpl': f'{path}\%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
        }],
    }

    MP4_OPTS = {'outtmpl': f'{path}\%(title)s.%(ext)s'}

    with youtube_dl.YoutubeDL(MP3_OPTS if is_mp3 else MP4_OPTS) as ydl:
        ydl.download([link])


root = tk.Tk()

title_label = tk.Label(root, text="YouTube mp3/mp4 dowlander")

insert_link_frame = tk.LabelFrame(root, text="Insert YouTube link")
insert_link_entry = tk.Entry(insert_link_frame, width=60)

file_format_frame = tk.Frame(root)
is_mp3 = tk.BooleanVar()
mp3_radio = tk.Radiobutton(file_format_frame, text="mp3", variable=is_mp3, value=True)
mp4_radio = tk.Radiobutton(file_format_frame, text="mp4", variable=is_mp3, value=False)

output_dir_frame = tk.LabelFrame(root, text='Select path to save download files')
output_dir_entry = tk.Entry(output_dir_frame, width=52)
browser_button = tk.Button(output_dir_frame, text='Browse', command=lambda : output_dir_entry.insert(0, fd.askdirectory()))
download_button = tk.Button(root, text="Download", command= lambda : download(insert_link_entry.get(),
                                                                              is_mp3.get()))
title_label.pack(pady=20)
insert_link_frame.pack(padx=20, pady=20)
insert_link_entry.pack(padx=20, pady=15)
output_dir_frame.pack()
output_dir_entry.grid(row=0, column=0, padx=10, pady=10)
browser_button.grid(row=0, column=1, padx=10, pady=10)
file_format_frame.pack(padx=20, pady=10)
mp3_radio.grid(row=0, column=0)
mp4_radio.grid(row=0, column=1)
download_button.pack(pady=25)
root.mainloop()
