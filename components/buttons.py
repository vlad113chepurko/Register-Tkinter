from tkinter import *
from components.logic import displaySavedFiles, func_HKEY_CURRENT_USER, func_HKEY_LOCAL_MACHINE, func_HKEY_CLASSES_ROOT, func_HKEY_USERS, func_HKEY_CURRENT_CONFIG

def create_buttons(buttons_frame, files_frame):
    btn_HKEY_CURRENT_USER = Button(buttons_frame, font=('Arial', 12), width=24, text="HKEY_CURRENT_USER", command=lambda: func_HKEY_CURRENT_USER(files_frame, "HKEY_CURRENT_USER"))
    btn_HKEY_CURRENT_USER.grid(row=0, column=0, padx=10, pady=5)

    btn_HKEY_LOCAL_MACHINE = Button(buttons_frame, font=('Arial', 12), width=24, text="HKEY_LOCAL_MACHINE", command=lambda: func_HKEY_LOCAL_MACHINE(files_frame, "HKEY_LOCAL_MACHINE"))
    btn_HKEY_LOCAL_MACHINE.grid(row=1, column=0, padx=10, pady=5)

    btn_HKEY_CLASSES_ROOT = Button(buttons_frame, font=('Arial', 12), width=24, text="HKEY_CLASSES_ROOT", command=lambda: func_HKEY_CLASSES_ROOT(files_frame, "HKEY_CLASSES_ROOT"))
    btn_HKEY_CLASSES_ROOT.grid(row=2, column=0, padx=10, pady=5)

    btn_HKEY_USERS = Button(buttons_frame, font=('Arial', 12), width=24, text="HKEY_USERS", command=lambda: func_HKEY_USERS(files_frame, "HKEY_USERS"))
    btn_HKEY_USERS.grid(row=3, column=0, padx=10, pady=5)

    btn_HKEY_CURRENT_CONFIG = Button(buttons_frame, font=('Arial', 12), width=24, text="HKEY_CURRENT_CONFIG", command=lambda: func_HKEY_CURRENT_CONFIG(files_frame, "HKEY_CURRENT_CONFIG"))
    btn_HKEY_CURRENT_CONFIG.grid(row=4, column=0, padx=10, pady=5)

    displaySavedFiles(files_frame)