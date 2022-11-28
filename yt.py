from tkinter import *
from tkinter import filedialog
from moviepy import *
from moviepy.editor import VideoFileClip
from pytube import YouTube
import shutil

# Functions

def select_path():
    # Ask the user to select the directory to save the video file
    path = filedialog.askdirectory()
    # change the path label to selected directory
    path_label.config(text=path)

def Download_file():
    # get user path
    get_link = link_field.get()
    # get selected path
    user_path = path_label.cget("text")
    screen.title("Dwonloading.....")
    # Download Video
    mp4_video = YouTube(get_link).streams.get_highest_resolution().download()
    vid_clip = VideoFileClip(mp4_video)
    vid_clip.close()

    # Move the file to the selected directory
    shutil.move(mp4_video, user_path)
    screen.title("Download Completed, Download another file...")




screen = Tk()
title = screen.title("Youtube Downloader")

canvas = Canvas(screen, height=500, width=500)
canvas.pack()

# image logo
logo_img = PhotoImage(file="YT.png")

# resize imgae
logo_img = logo_img.subsample(4, 4)
canvas.create_image(250, 100, image=logo_img)

# link Field
link_field = Entry(screen, width=50)
link_label = Label(screen, text="Enter link to download: ", font=('Arial', 15))

# Select path for saving the file
path_label = Label(screen, text="Select Path: ", font=('Arial', 12))
select_btn = Button(screen, text="Select", command=select_path)

canvas.create_window(250, 280, window=path_label)
canvas.create_window(250, 330, window=select_btn)
# Add widgets to the window
canvas.create_window(250, 200, window=link_label)
canvas.create_window(250, 240, window=link_field)

# Download Btn
download_btn = Button(screen, text="Download Video", command=Download_file)

# Add to canvas
canvas.create_window(250, 380, window=download_btn)

screen.mainloop()
