from tkinter import *

def saveFile(new_window, name_entry, type_entry, data_entry, update_window, register_name):
    name = name_entry.get()
    file_type = type_entry.get()
    data = data_entry.get()

    with open(f"{register_name}_{name}.{file_type}", "w") as file:
        file.write(data)

    saveFileInfo(register_name, name, file_type, data)
    update_window(new_window, register_name)
    new_window.destroy()

def saveFileInfo(register_name, name, file_type, data):
    with open("saved_files.txt", "a") as file:
        file.write(f"{register_name}|{name}|{file_type}|{data}\n")

def createFile(new_window, update_window, register_name):
    name_label = Label(new_window, font=('Arial', 12),  text='Enter name of file: ')
    name_label.grid(row=1, column=0, pady=10)

    name_entry = Entry(new_window, font=('Arial', 12))
    name_entry.grid(row=1, column=1)

    type_label = Label(new_window, font=('Arial', 12), text='Enter type of file: ')
    type_label.grid(row=2, column=0, pady=10)

    type_entry = Entry(new_window, font=('Arial', 12))
    type_entry.grid(row=2, column=1)

    data_label = Label(new_window, font=('Arial', 12),  text='Enter data of file: ')
    data_label.grid(row=3, column=0, pady=10)

    data_entry = Entry(new_window, font=('Arial', 12))
    data_entry.grid(row=3, column=1)

    buttonSave = Button(new_window, font=('Arial', 12), bg='green', fg='white', text="Save file", command=lambda: saveFile(new_window, name_entry, type_entry, data_entry, update_window, register_name))
    buttonSave.grid(row=4, column=0)

def createWindow(root, register_name):
    new_window = Toplevel(root)
    new_window.title(f"{register_name}")
    new_window.geometry("1440x1080")

    currentLabel = Label(
        new_window,
        text=f"{register_name}",
        font=('Arial', 13))
    currentLabel.grid(row=0, column=0)

# ? || Функция для обновления окна
    def update_window(window, register_name):
        for widget in window.winfo_children():
            widget.destroy()

        displaySavedFiles(window, register_name)

    buttonCreate = Button(
        new_window,
        bg="pink",
        text="Create new file",
        font=("Arial", 12),
        width=16,
        height=2,
        command=lambda: createFile(new_window, update_window, register_name))
    buttonCreate.grid(row=0, column=1)

    displaySavedFiles(new_window, register_name)

# ? || Функция для отображения сохраненных файлов
def displaySavedFiles(root, register_name=None):
    try:
        with open("saved_files.txt", "r") as file:
            files = file.readlines()
            for i, file_info in enumerate(files):
                parts = file_info.strip().split("|")
                if len(parts) == 4:
                    saved_register_name, name, file_type, data = parts
                    if register_name is None or saved_register_name == register_name:
                        label = Label(root, text=f"{name}.{file_type} - {data}")
                        label.grid(row=i+1, column=0, sticky=W)
                else:
                    print(f"Skipping invalid line: {file_info.strip()}")
    except FileNotFoundError:
        pass


# ? || Функции для отображения файлов в разных разделах реестра
def func_HKEY_CURRENT_USER(root, register_name):
    createWindow(root, register_name)

def func_HKEY_LOCAL_MACHINE(root, register_name):
    createWindow(root, register_name)

def func_HKEY_CLASSES_ROOT(root, register_name):
    createWindow(root, register_name)

def func_HKEY_USERS(root, register_name):
    createWindow(root, register_name)

def func_HKEY_CURRENT_CONFIG(root, register_name):
    createWindow(root, register_name)