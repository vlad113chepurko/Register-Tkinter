from tkinter import *
from components.buttons import create_buttons

root = Tk()
root.title("Register")
root.geometry("1440x1080")


buttons_frame = Frame(root)
buttons_frame.pack(side=LEFT, fill=Y)

files_frame = Frame(root)
files_frame.pack(side=RIGHT, fill=BOTH, expand=True)

create_buttons(buttons_frame, files_frame)

root.mainloop()