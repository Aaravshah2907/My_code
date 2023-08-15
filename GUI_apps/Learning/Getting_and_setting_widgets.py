import tkinter as tk
from tkinter import ttk

def button_func():
    # get the content of the entry
    entry_text = (entry.get())
    
    # update the label
    # label.configure(text= 'some other text')
    label['text'] = entry_text
    entry['state'] = 'disabled'
    # print(label.configure())


def reset_func():
    label['text'] = 'some text'
    entry['state'] = 'enabled'
    

# window
window = tk.Tk()
window.title("Getting & Setting Widgets")

# widgets
label = ttk.Label(master=window, text='Some Text')
label.pack()

entry = ttk.Entry(master=window)
entry.pack()

button = ttk.Button(master=window, text= 'Submit & Display', command= button_func)
button.pack()

exercise_button = ttk.Button(master=window, text = 'reset button', command = reset_func)
exercise_button.pack()

# run
window.mainloop()