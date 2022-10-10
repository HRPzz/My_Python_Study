import os
import sys
import tkinter
from PIL import Image, ImageTk


# py -> exe 변환
# - pyinstaller -w --add-data './gui_basic/*.gif;gui_basic' --add-data './gui_basic/*.jpg;gui_basic' './gui_basic/label.py'


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


root = tkinter.Tk()
root.title("Nado GUI")
root.geometry("640x480")

label1 = tkinter.Label(root, text="안녕하세요")
label1.pack()

photo = tkinter.PhotoImage(file=resource_path("gui_basic/bg.gif"))
label2 = tkinter.Label(root, image=photo)
label2.pack()


def change():
    label1.config(text="또 만나요")

    global photo2
    photo2 = Image.open(resource_path('gui_basic/wallpaper.jpg'))
    photo2 = ImageTk.PhotoImage(photo2)
    label2.config(image=photo2)


btn = tkinter.Button(root, text="클릭", command=change)
btn.pack()

root.mainloop()
