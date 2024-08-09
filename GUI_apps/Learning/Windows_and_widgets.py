import tkinter as tk
from tkinter import ttk

def button_func():
    print('A button was pressed')


def exercise_button_func():
    print("Hello")


# create a window
window = tk.Tk()
window.title('Window & Widgets')
window.geometry('800x500')

# ttk lavel
label = ttk.Label(master=window, text='This is a test')
label.pack()

# create widgets
text = tk.Text(master=window)
text.pack()

# ttk widget
entry = ttk.Entry(master=window)
entry.pack()

# exercise label
exercise_label = ttk.Label(master= window, text='my label')
exercise_label.pack()

# ttk button
button = ttk.Button(master=window, text='A button', command= button_func)
button.pack()

# exercise button
# exercise_button = ttk.Button(master=window, text='exercise button', command = exercise_button_func)
exercise_button = ttk.Button(master=window, text='exercise button', command= lambda: print("Hello"))
exercise_button.pack()

# run
window.mainloop()