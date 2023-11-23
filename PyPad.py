import tkinter as tk
import os
import tkinter.filedialog as tkFile
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox

VERSION = 5.1

INFO = '''© 2023 Culmutive

All rights reserved.'''

def write_prep():
    def write():
        file_content = write_content.get('1.0', 'end-1c')

        types = [("Text files", "*.txt")]
        file_write = tkFile.asksaveasfile(title="Save file", defaultextension=".txt", filetypes=types)

        if file_write:
            file_write.writelines(file_content)
            file_write.close()
            write_w.destroy()
            open_file_q = messagebox.askquestion("Open File?", "Do you want to open the file that you saved?")

            if open_file_q == "yes":
                open_prep()

    write_w = tk.Tk()
    write_w.title("Create file")
    write_w.geometry("400x380")
    write_w.focus_force()

    write_title = tk.Label(write_w, text="Create file", font=("Helvetica 15"))
    write_title.pack()

    write_content_label = tk.Label(write_w, text="Content to write:", font=("Arial 10"))
    write_content_label.pack()

    write_content = ScrolledText(write_w, width=40, height=15)
    write_content.pack()

    save_button = tk.Button(write_w, text="Save", command=write, cursor="hand2")
    save_button.pack()

def open_prep():
    def save():
        file_content_to_write = file_content_write.get("1.0", "end-1c")
        file_path_usable = file_path.replace("\\", "\\\\")
        
        file_to_write_to = open(file_path_usable, "w")
        file_to_write_to.write(file_content_to_write)
        file_to_write_to.close()

    types = [("Text Files", "*.txt")]

    open_file = tkFile.askopenfile(title="Open File", defaultextension=".txt", filetypes=types, mode="r")

    if open_file is not None:
        file_name = os.path.basename(open_file.name)
        file_path = os.path.abspath(open_file.name)
        file_content = open_file.read()
    
        file_w = tk.Tk()
        file_w.title("PyPad - " + file_name)
        file_w.geometry("400x380")
        file_w.focus_force()

        title_name = "Edit " + file_name
        title = tk.Label(file_w, text=title_name, font=("Helvetica", 15))
        title.pack()

        content_to_write_label = tk.Label(file_w, text="Content to write:", font=("Arial", 10))
        content_to_write_label.pack()

        file_content_write = ScrolledText(file_w, width=40, height=15)
        file_content_write.pack()
        file_content_write.insert(tk.INSERT, file_content)

        save_button = tk.Button(file_w, text="Save", command=save, cursor="hand2")
        save_button.pack()

def view_prep():
    def close_view():
        view_w.destroy()

    def view():
        view_w.destroy()

        file = tkFile.askopenfile(mode="r", filetypes=[("Text files", "*.txt")])

        if file is not None:
            file_name = os.path.basename(file.name)
            content = file.read()
            
            file_content_w = tk.Tk()
            file_content_w.title(file_name)
            file_content_w.focus_force()

            file_content_text = tk.Label(file_content_w, text=content, font=("Arial 10"))
            file_content_text.pack()

            file.close()


    view_w = tk.Tk()
    view_w.title("View File")
    view_w.focus_force()

    view_title = tk.Label(view_w, text="View File", font=("Helvetica 15"))
    view_title.pack()

    view_file_button = tk.Button(view_w, text="Choose file", command=view, cursor="hand2")
    view_file_button.pack()

    close_view_w = tk.Button(view_w, text="Cancel", command=close_view, cursor="hand2")
    close_view_w.pack(pady=5)

def info():
     version_number = str(VERSION)
     title_version = "PyPad Version " + version_number

     def close():
         info_w.destroy()

     info_w = tk.Tk()
     info_w.title("Info - PyPad")
     info_w.geometry("350x200")
     info_w.focus_force()

     info_title = tk.Label(info_w, text=title_version, font=("Helvetica 15"))
     info_title.pack()

     info_text = tk.Label(info_w, text=INFO, font=("Arial 10"))
     info_text.pack(anchor="n", pady=5)

     info_close = tk.Button(info_w, text="Cancel", command=close, cursor="hand2")
     info_close.pack(side=tk.BOTTOM, anchor="w")

window = tk.Tk()
window.title("PyPad")
window.geometry("400x300")

main_title = tk.Label(window, text="PyPad", font=("Helvetica 15"))
main_title.pack()

write_button = tk.Button(window, text="Create file", command=write_prep, cursor="hand2")
write_button.pack()

open_button = tk.Button(window, text="Open File", command=open_prep, cursor="hand2")
open_button.pack(pady=5)

view_button = tk.Button(window, text="View file", command=view_prep, cursor="hand2")
view_button.pack()

info_button = tk.Button(window, text="Info", fg="blue", command=info, cursor="hand2")
info_button.pack(anchor="w", side=tk.BOTTOM)

window.mainloop()
