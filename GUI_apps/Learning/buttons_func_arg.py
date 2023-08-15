import tkinter as tk
from tkinter import ttk

def btn_func(entry_str):
    print('A button was pressed')
    print(entry_str.get())


def outer_func(parameter):
    def inner_func():
        print('A button was pressed')
        print(parameter.get())
    return inner_func

# window
window = tk.Tk()
window.title("Buttons")

# widgets
entry_str = tk.StringVar(value = 'Test')
entry = ttk.Entry(window, textvariable=entry_str)
entry.pack()

# button = ttk.Button(window, text= 'Button', command= btn_func(entry_str))
button = ttk.Button(window, text= 'Button', command= outer_func(entry_str))
button.pack()

# run
window.mainloop()