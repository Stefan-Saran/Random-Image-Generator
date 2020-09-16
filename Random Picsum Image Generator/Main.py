modules = []

try:
    import tkinter as tk
    from tkinter import ttk
    from tkinter import *
    from tkinter.messagebox import showinfo
    import subprocess
    import itertools
    import time
    from time import sleep
    from datetime import datetime
    from tkinter.ttk import Frame, Button, Style
    from PIL import Image
    from PIL import ImageTk
    import urllib
    from urllib import request
    import io
    import http.client
    import os
    import requests
except ImportError:
    import sys
    import pip
    import subprocess
    while True:
        module_installation_question = input("Some modules are missing, do you want to install all required modules for this project? yes or no.: ").lower()
        if module_installation_question == "yes":
            print("Installing required modules...")
            for module in modules:
                subprocess.call(['pip', 'install', module])
            print("Restart the editor or the script and this project should work...")
            while True:
                image_displayer = input("")
        elif module_installation_question == "no":
            print("This project won't work if one module is missing...")
        else:
            print("That is not a valid command...")

start_btn_toggle = True
about_btn_toggle = True
help_btn_toggle = True
category_btn_toggle = True
category_back_btn_toggle = True
start_back_btn_toggle = True


about_text = """
|This is Random Image Generator|

\nThis program uses images from\n www.picsum.photos \nand displays it\n

Creator = Stefan Saran

Disclaimer:
I don't own any images\ndisplayed in this application!

Creation date: 
April 13th. - May 4th. 2020

"""

help_text = """
All downloaded images are saved in
a folder named "images downloaded" and
that is located where this
application or exe file is saved.
"""

url = "https://picsum.photos//1920/1080"
start_image = "images/info.png"
end_image = "images/info2.png"
wallpaper = "images/Wallpaper.jpg"
width = 480
height = 270

img3_width = 960
img3_height = 540

img = Image.open(start_image)
img = img.resize((width, height), Image.ANTIALIAS)

img2 = Image.open(end_image)
img2 = img2.resize((width, height), Image.ANTIALIAS)

img3 = Image.open(wallpaper)
img3 = img3.resize((img3_width, img3_height), Image.ANTIALIAS)


class App():
    def __init__(self, parent, *args, **kwargs):
        self.app = parent
        self.app.geometry("959x540+400+120")
        self.app.title("Picsum Random Image Generator")

        self.image_format = str("")

        self.image_connection1 = ""

        self.photoimg1 = ImageTk.PhotoImage(img)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        self.home_frame = tk.Frame(self.app)
        self.category_frame = tk.Frame(self.app)
        self.start_frame = tk.Frame(self.app)
        self.about_frame = tk.Frame(self.app, bg="white")
        self.help_frame = tk.Frame(self.app, bg="white")
        self.home_frame.grid(row=0, column=0, sticky="nsew")

        self.home_frame.configure(bg="white")
        self.category_frame.configure(bg="white")
        self.start_frame.configure(bg="white")

        self.image_label = tk.Label(self.start_frame, image=self.photoimg1)
        self.image_label.grid(row=2, column=2, padx=90, pady=50)

        self.about_font = ("Verdana", 14)
        self.help_font = ("Verdana", 14)

        self.start_btn = tk.Button(self.home_frame, text="Start", width=30, height=3, command=self.start_btn_fun)
        self.start_btn.grid(row=1, column=1, pady=300, padx=220)

        self.about_btn = tk.Button(self.home_frame, anchor="center", text="About", width=20, height=2, command=self.about_back_btn_fun)
        self.about_btn.grid(row=0, column=0)

        self.about_label = tk.Label(self.about_frame, text=about_text, font=self.about_font, width=36, height=20, bg="white", anchor="center")
        self.about_label.grid(row=1, column=2, padx=105, sticky="nsew")
        
        self.about_back_btn = tk.Button(self.about_frame, text="Back", width=20, height=2, command=self.about_back_btn_fun)
        self.about_back_btn.grid(row=0, column=0)

        self.help_back_btn = tk.Button(self.help_frame, text="Back", width=20, height=2, command=self.help_back_btn_ftn)
        self.help_back_btn.grid(row=0, column=0)

        self.help_label = tk.Label(self.help_frame, text=help_text, font=self.help_font, width=36, height=20, bg="white", anchor="center")
        self.help_label.grid(row=2, column=1, padx=105, sticky="nsew")

        self.create_image_btn = tk.Button(self.category_frame, text="Create Images", width=20, height=2, command=self.category_error)
        self.create_image_btn.grid(row=0, column=2)

        self.category_back_btn = tk.Button(self.category_frame, text="Back", width=20, height=2, command=self.category_back_btn_fun)
        self.category_back_btn.grid(row=0, column=0)

        self.help_btn = tk.Button(self.start_frame, text="Help", width=20, height=2, command=self.help_back_btn_ftn)
        self.help_btn.grid(row=0, column=3)

        self.download_btn = tk.Button(self.start_frame, state=tk.DISABLED, width=20, height=2, text="Download", command=self.download_image)
        self.download_btn.grid(row=3, column=2, pady=20)

        self.restart_btn = tk.Button(self.start_frame, text="Restart", anchor="center", width=20, height=2, command=self.restart_btn_fun)
        self.restart_btn.grid(row=0, column=0)

        self.app.bind("<Return>", self.image_displayer)

    def download_image(self, directory = "images downloaded"):
        self.time_now = datetime.now()
        self.time_now_format = self.time_now.strftime("%d.%m.%y - %H.%M.%S")
        if not os.path.exists(directory):
            os.makedirs(directory)
        image_name = f"{self.time_now_format}" + self.image_format
        img_data = requests.get(url).content
        with open(os.path.join(directory, image_name), "wb") as saving_files:
            saving_files.write(self.image_connection1)

    def image_creator(self):
        with urllib.request.urlopen(url) as connection1:
            self.image_connection1 = connection1.read()
            image_reading = Image.open(io.BytesIO(self.image_connection1))
            image_reading = image_reading.resize((480, 270), Image.ANTIALIAS)
            image = ImageTk.PhotoImage(image_reading)
            self.image_label.configure(image = image)
            self.image_label.image = image

    def image_displayer(self, e):
        if self.download_btn["state"] == tk.DISABLED:
            self.download_btn["state"] = tk.NORMAL
        try:
            self.image_creator()
        except urllib.error.URLError:
            self.image_label.configure(image = self.photoimg2)
            self.image_label.image = self.photoimg2
            self.download_btn["state"] = tk.DISABLED
        except http.client.IncompleteRead as e:
            self.image_creator()
        except:
            showinfo("Error", "A random error occurred, maybe the website is down,\nor the resolution of the image is too large.")

    def category_error(self):
        if category.variable.get() == "PNG":
            self.image_format = ".png"
            self.create_image_btn_fun()
        elif category.variable.get() == "JPG":
            self.image_format = ".jpg"
            self.create_image_btn_fun()
        elif category.variable.get() == "JPEG":
            self.image_format = ".jpeg"
            self.create_image_btn_fun()
        elif category.variable.get() == "Choose an image format":
            showinfo("error", "you need to choose image format!")
        else:
            showinfo("error", "random error ocurred...")


    def restart_btn_fun(self):
        self.start_frame.grid_forget()
        self.category_frame.grid(row=0, column=0, sticky="nsew")
        self.image_label.configure(image = self.photoimg1)
        self.image_label.Image = self.photoimg1
        self.download_btn["state"] = tk.DISABLED
        category.variable.set('Choose an image format')

    def create_image_btn_fun(self):
        self.category_frame.grid_forget()
        self.start_frame.grid(row=0, column=0, sticky="nsew")


    def category_back_btn_fun(self):
        self.category_frame.grid_forget()
        self.home_frame.grid(row=0, column=0, sticky="nsew")

    def start_btn_fun(self):
        self.home_frame.grid_forget()
        self.category_frame.grid(row=0, column=0, sticky="nsew")

    def about_back_btn_fun(self):
        global about_btn_toggle
        if about_btn_toggle:
            self.home_frame.grid_forget()
            self.about_frame.grid(row=0, column=0, sticky="nsew")
            about_btn_toggle = False
        else:
            self.about_frame.grid_forget()
            self.home_frame.grid(row=0, column=0, sticky="nsew")
            about_btn_toggle = True

    def help_back_btn_ftn(self):
        global help_btn_toggle
        if help_btn_toggle:
            self.start_frame.grid_forget()
            self.help_frame.grid(row=0, column=0, sticky="nsew")
            help_btn_toggle = False
        else:
            self.help_frame.grid_forget()
            self.start_frame.grid(row=0, column=0, sticky="nsew")
            help_btn_toggle = True

class category():
    def __init__(self):
        self.choices = ["Choose an image format", "PNG", "JPG", "JPEG"]
        self.variable = StringVar(App_class.category_frame)
        self.variable.set('Choose an image format')
        self.w = OptionMenu(App_class.category_frame, self.variable, *self.choices)
        self.w.grid(row=2, column=1, padx=41, pady=70)
        self.w.config(width=89)


if __name__ == "__main__":
    app1 = tk.Tk()
    app1.grid_rowconfigure(0, weight=1)
    app1.grid_columnconfigure(0, weight=1)
    App_class = App(app1)
    category = category()
    app1.mainloop()