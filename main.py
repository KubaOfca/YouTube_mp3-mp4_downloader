from __future__ import unicode_literals
import youtube_dl
from tkinter import filedialog as fd
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox
from time import sleep
import re
import threading
import os
import sys

#TODO correct threading

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
    print(t1.is_alive())

def info_download_progress(d):
    if d['status'] == 'finished':
        print("Done downloading")
    if d['status'] == 'downloading':
        percent = re.findall("\d+", d['_percent_str'])[0] # in order to covnert to int
        download_progress['value'] = int(percent)
        download_time.configure(text=f"Remaining Time  {d['_eta_str']}")
        download_progress.update_idletasks()
        download_time.update_idletasks()



def download():
    link = insert_link_entry.get()
    is_mp3_loc = is_mp3.get()
    path = output_dir_entry.get()
    root.update_idletasks()

    MP3_OPTS = {
        'format': 'bestaudio/best',
        'outtmpl': f'{path}\%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
        }],
        'progress_hooks': [info_download_progress],
    }

    MP4_OPTS = {'outtmpl': f'{path}\%(title)s.%(ext)s',
                'progress_hooks': [info_download_progress], }

    try:
        with youtube_dl.YoutubeDL(MP3_OPTS if is_mp3_loc else MP4_OPTS) as ydl:
            ydl.download([link])
            root.update_idletasks()
    except:
        messagebox.showerror(title="ERROR",
                             message="Wrong YouTube URL link")

    sleep(1)
    download_progress['value'] = 0
    download_time.configure(text='Remaining Time  00:00')
    root.update_idletasks()

root = ttk.Window(themename='darkly')
t1 = threading.Thread(target=download)

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
                             command=t1.start,
                             bootstyle=DANGER)
stop_button = ttk.Button(download_frame,
                             text="Stop",
                             command=restart_program,
                             bootstyle=WARNING,
                             width=9)
download_progress = ttk.Progressbar(download_frame,
                                    orient=HORIZONTAL,
                                    length=100,
                                    mode="determinate",
                                    bootstyle=(STRIPED,SUCCESS))

download_time = ttk.Label(download_frame,
                          text='Remaining Time  00:00')
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
stop_button.grid(row=1, column=0, padx=20, pady=10)
download_progress.grid(row=0, column=1, padx=20)
download_time.grid(row=0, column=2, padx=20)

root.mainloop()
