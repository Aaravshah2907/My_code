import tkinter as tk
from tkinter import ttk
import os
path = os.path.abspath("E:\My_code\GUI_apps\'Yt Learning'\deamon.jpg")
#window
window = tk.Tk(className='Demo')
var = tk.StringVar()
#element
label_1 = ttk.Label(window, image=path)
var.set("Demo text here.let's see a new line.")

label_1.pack()
#run
window.mainloop()