modules = ["pip", "requests", "datetime"]

try:
    import urllib
    from tkinter.ttk import *
    import tkinter as tk
    from tkinter import *
    from PIL import ImageTk, Image
    import os
    import requests
    import io
    from tkinter.messagebox import showinfo
    from datetime import datetime
    import subprocess
except ImportError:
    import sys
    import pip
    import subprocess
    module_installation_question = input(
        "Some modules are missing, do you want to install all required modules for this project? yes or no.: ").lower()
    if module_installation_question == "yes":
        for module in modules:
            subprocess.call(['pip', 'install', module])
        print("Restart the editor and this project should work...")
        sys.exit()
    elif module_installation_question == "no":
        print("This project won't work if one module is missing...")
        sys.exit()

Image_generator = tk.Tk()

Image_generator.geometry("520x500")
Image_generator.configure(bg='#1A1A1A')
Image_generator.title("Random Image Generator")
download_button = tk.Button(Image_generator, text="Download Image", width=13,
                            height=1, state=DISABLED, command=lambda: createFolder())
download_button.place(rely=0.82, relx=0.4)

About_button = tk.Button(Image_generator, text="About", width=11,
                         height=1, command=lambda: About_info()).place(rely=0.05, relx=0.037)


url = "https://picsum.photos//1920/1080"

image_file = "images/info.png"
img = PhotoImage(file=image_file)
img = img.zoom(1)
img = img.subsample(1)
image_connection2 = ""

file2 = "images/info2.png"
img2 = PhotoImage(file=file2)
img2 = img2.zoom(1)
img2 = img2.subsample(1)


widget = tk.Label(Image_generator, image=img)
widget.place(rely=0.16, relx=0.037)
# while img == widget:
#button['state'] = DISABLED


def binding(e):
    global image_connection2
    try:
        with urllib.request.urlopen(url) as connection1:
            image_connection1 = connection1.read()
            image_connection2 = image_connection1
        image_reading = Image.open(io.BytesIO(image_connection2))
        image_resizing = image_reading.resize((480, 270), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(image_resizing)
        widget.configure(image=image)
        widget.image = image
        if (download_button['state'] == tk.DISABLED):
            download_button['state'] = tk.NORMAL
    except urllib.error.URLError:
        widget.configure(image=img2)
        widget.image = img2
        download_button["state"] = tk.DISABLED


time_now = datetime.now()
time_now_format = time_now.strftime("%d.%m.%Y - %H.%M.%S")

reopen_programm_format = '"{}" "{}" "{}"'.format(
    sys.executable,
    __file__,
    os.path.basename(__file__),
)


def createFolder(directory="images downloaded"):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
        filename = f"{time_now_format}" + '.jpg'
        img_data = requests.get(url).content
        with open(os.path.join(directory, filename), 'wb') as saving_files:
            saving_files.write(image_connection2)
            Image_generator.quit()
            subprocess.Popen(reopen_programm_format)
    except:
        showinfo("Error", "An error has occurred")


def About_info():
    Title = "This is Random Image Generator"
    bolded_text = "\033[1m" + Title + "\033[0m"
    About_popup = Toplevel(background="#1A1A1A")
    About_popup.resizable(False, False)
    About_font = ('Verdana', 13)
    About_popup.title("About")
    width = 320     # popup window width
    height = 400     # popup window height
    screen_width = About_popup.winfo_screenwidth()
    screen_height = About_popup.winfo_screenheight()
    x = (screen_width - width)/2
    y = (screen_height - height)/2
    About_popup.geometry('%dx%d+%d+%d' % (width, height, x, y))
    About_text = f"""
    \n
|{Title}|
---------------------------
\nThis program uses images from\n www.picsum.photos \nand displays it\n
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
    About_text += '\n'
    width = Label(About_popup, text=About_text, width=120, height=18,
                  background="#1A1A1A", foreground="white", font=About_font)
    width.pack()

    About_popup.transient(Image_generator)
    About_popup.grab_set()
    About_popup.wait_window(About_popup)
    About_popup.mainloop()


def center_window(width=300, height=200):
    # get screen width and height
    screen_width = Image_generator.winfo_screenwidth()
    screen_height = Image_generator.winfo_screenheight()

    # calculate position x and y coordinates
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    Image_generator.geometry('%dx%d+%d+%d' % (width, height, x, y))


Image_generator.bind("<Return>", binding)

Image_generator.resizable(False, False)
center_window(520, 500)
Image_generator.mainloop()
