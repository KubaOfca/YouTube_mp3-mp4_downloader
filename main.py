from __future__ import unicode_literals
import youtube_dl
from tkinter import filedialog as fd
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox
from time import sleep

def download(link, is_mp3):
    path = output_dir_entry.get()
    download_progress['value'] = 50 #
    root.update_idletasks()

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

    try:
        with youtube_dl.YoutubeDL(MP3_OPTS if is_mp3 else MP4_OPTS) as ydl:
            ydl.download([link])
            download_progress['value'] = 100
            root.update_idletasks()
    except:
        messagebox.showerror(title="ERROR",
                             message="Wrong YouTube URL link")

    sleep(1)
    download_progress['value'] = 0
    root.update_idletasks()

root = ttk.Window(themename='darkly')

title_label = ttk.Label(root,
                        text="YouTube mp3/mp4 dowlander")

insert_link_frame = ttk.LabelFrame(root,
                                   text="Insert YouTube link")
insert_link_entry = ttk.Entry(insert_link_frame,
                              width=60)

file_format_frame = ttk.Frame(root)
is_mp3 = ttk.BooleanVar()
mp3_radio = ttk.Radiobutton(file_format_frame,
                            text="mp3",
                            variable=is_mp3,
                            value=True)
mp4_radio = ttk.Radiobutton(file_format_frame,
                            text="mp4",
                            variable=is_mp3,
                            value=False)

output_dir_frame = ttk.LabelFrame(root,
                                  text='Select path to save download files')
output_dir_entry = ttk.Entry(output_dir_frame,
                             width=46)
browser_button = ttk.Button(output_dir_frame,
                            text='Browse',
                            command=lambda : output_dir_entry.insert(0, fd.askdirectory()),
                            bootstyle=PRIMARY)
download_frame = ttk.Frame(root)
download_button = ttk.Button(download_frame,
                             text="Download",
                             command= lambda : download(insert_link_entry.get(), is_mp3.get()),
                             bootstyle=DANGER)
download_progress = ttk.Progressbar(download_frame,
                                    orient=HORIZONTAL,
                                    length=100,
                                    mode="determinate",
                                    bootstyle=(STRIPED,SUCCESS))
# pack
title_label.pack(pady=20)
insert_link_frame.pack(padx=20, pady=20)
insert_link_entry.pack(padx=20, pady=15)
output_dir_frame.pack()
output_dir_entry.grid(row=0, column=0, padx=20, pady=10)
browser_button.grid(row=0, column=1, padx=10, pady=10)
file_format_frame.pack(padx=20, pady=20)
mp3_radio.grid(row=0, column=0, padx=10)
mp4_radio.grid(row=0, column=1, padx=10)
download_frame.pack(padx=20, pady=20)
download_button.grid(row=0, column=0, padx=20)
download_progress.grid(row=0, column=1, padx=20)
root.mainloop()
