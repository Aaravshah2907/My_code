import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title("Buttons")
window.geometry('600x400')

# button
def bttn_func():
    print("A button is pressed.")


button_str = tk.StringVar(value='A button with String')
button = ttk.Button(window, text='Button', command=bttn_func, textvariable=button_str)
button.pack()

# checkbutton
check_var = tk.IntVar(value=10)
check = ttk.Checkbutton(
    window,
    text='Checkbox 1',
    command= lambda : print(check_var.get()),
    variable= check_var,
    onvalue=1,
    offvalue=0)
check.pack()

check2_var = tk.IntVar(value=10)
check2 = ttk.Checkbutton(
    window,
    text='Checkbox 2',
    command= lambda : print(check2_var.get()),
    variable= check2_var,
    onvalue=10,
    offvalue=5)
check2.pack()


# radiobuttons
radio_var = tk.StringVar()
radio1 = ttk.Radiobutton(
    window,
    text='Radio Button 1',
    value='Button 1',
    variable= radio_var,
    command=lambda: print(radio_var.get()))
radio1.pack()

radio2 = ttk.Radiobutton(
    window,
    text='Radio Button 2',
    value='Button 2',
    variable= radio_var,
    command=lambda: print(radio_var.get()))
radio2.pack()

# run
window.mainloop()