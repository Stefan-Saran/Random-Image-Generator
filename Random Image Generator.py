from PIL import Image
from urllib import request
import urllib
from tkinter.ttk import *
import tkinter as tk
from tkinter import *
import random
from PIL import ImageTk, Image
import os
from io import BytesIO
import requests
import sys
import io
from time import sleep
import datetime
from datetime import date
from tkinter.messagebox import showinfo
from datetime import datetime
from random import randrange
from tkinter import ttk
import subprocess
import time


App1 = tk.Tk()


App1.geometry("520x500")
App1.configure(bg='#1A1A1A')
App1.title("Random Image Generator")
button = tk.Button(App1, text="Download Image", width=13,
                   height=1, state=DISABLED, command=lambda: createFolder())
button.place(rely=0.82, relx=0.4)

button2 = tk.Button(App1, text="About", width=11,
                    height=1, command=lambda: popup_bonus2()).place(rely=0.05, relx=0.037)


url = "https://source.unsplash.com/random/1920x1080"

file = "images/info.png"
img = PhotoImage(file=file)
img = img.zoom(1)
img = img.subsample(1)
raw_data2 = ""

file2 = "images/info2.png"
img2 = PhotoImage(file=file2)
img2 = img2.zoom(1)
img2 = img2.subsample(1)


widget = tk.Label(App1, image=img)
widget.place(rely=0.16, relx=0.037)
# while img == widget:
#button['state'] = DISABLED


def callback(e):
    global raw_data2
    try:
        with urllib.request.urlopen(url) as connection1:
            raw_data1 = connection1.read()
            raw_data2 = raw_data1
        im = Image.open(io.BytesIO(raw_data2))
        image2 = im.resize((480, 270), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(image2)
        widget.configure(image=image)
        widget.image = image
        if (button['state'] == tk.DISABLED):
            button['state'] = tk.NORMAL
    except urllib.error.URLError:
        widget.configure(image=img2)
        widget.image = img2
        button["state"] = tk.DISABLED


today1 = datetime.now()
d2 = today1.strftime("%d.%m.%Y - %H.%M.%S")


def createFolder(directory="images downloaded"):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
        else:
            filename = f"{d2}" + '.jpg'
            img_data = requests.get(url).content
            with open(os.path.join(directory, filename), 'wb') as temp_file:
                temp_file.write(raw_data2)
    except:
        pass

    command = '"{}" "{}" "{}"'.format(
        sys.executable,
        __file__,
        os.path.basename(__file__),
    )
    App1.quit()
    subprocess.Popen(command)


def popup_bonus2():
    a = "This is Random Image Generator"
    bolded_string = "\033[1m" + a + "\033[0m"
    root = Toplevel(background="#1A1A1A")
    root.resizable(False, False)
    large_font2 = ('Verdana', 13)
    root.title("About")
    w = 320     # popup window width
    h = 400     # popup window height
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    x = (sw - w)/2
    y = (sh - h)/2
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    m = f"""


|{a}|
---------------------------
\nThis program uses images from\n unsplash.com \nand displays it\n
---------------------------
Creator = Stefan Saran
---------------------------
Disclaimer:
I don't own any images\ndisplayed in this application!
---------------------------
Creation date: 
April 13th. - May 4th. 2020
---------------------------
"""
    m += '\n'
    w = Label(root, text=m, width=120, height=18,
              background="#1A1A1A", foreground="white", font=large_font2)
    w.pack()

    root.transient(App1)
    root.grab_set()
    root.wait_window(root)
    root.mainloop()


def center_window(width=300, height=200):
    # get screen width and height
    screen_width = App1.winfo_screenwidth()
    screen_height = App1.winfo_screenheight()

    # calculate position x and y coordinates
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    App1.geometry('%dx%d+%d+%d' % (width, height, x, y))


App1.bind("<Return>", callback)

App1.resizable(False, False)
center_window(520, 500)
App1.mainloop()
