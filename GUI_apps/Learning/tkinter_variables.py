import tkinter as tk
from tkinter import ttk

def button_func():
    print(string_var.get())
    string_var.set('Button Pressed')

# window
window = tk.Tk()
window.title("Tkinter Variables")

# tkinter variable
string_var = tk.StringVar(value='Start Value')

#widgets
label = ttk.Label(window, text= 'label', textvariable=string_var)
label.pack()

entry = ttk.Entry(window, textvariable= string_var)
entry.pack()

button = ttk.Button(window, text='button', command=button_func)
button.pack()

ex_var = tk.StringVar(value='Test')
entry1 = ttk.Entry(window, textvariable=ex_var)
entry1.pack()
entry2 = ttk.Entry(window, textvariable=ex_var)
entry2.pack()
label = ttk.Label(window, textvariable=ex_var)
label.pack()

# run
window.mainloop()