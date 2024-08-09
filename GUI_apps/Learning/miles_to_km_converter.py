import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    mile_input = entry_int.get()
    km_output = mile_input * 1.61
    output_str.set(f'{km_output} km')


#window creation
window = ttk.Window(themename= 'journal')
window.title('Converter 1')
window.geometry('500x225')

# title
title_label = ttk.Label(master= window, text= 'Miles to Kilometres', font= 'Calibri 24 bold')
title_label.pack()

# input Label
input_frame = ttk.Frame(master= window)
entry_int = tk.IntVar()
entry = ttk.Entry(master= input_frame, textvariable=entry_int)
button = ttk.Button(master=input_frame, text= 'Convert', command= convert)
entry.pack(side='left', padx= 10)
button.pack(side='left')
input_frame.pack(pady= 10)

# ouput
output_str = tk.StringVar()
output_label = ttk.Label(
    master=window, 
    text='Output Placeholder', 
    font= 'Calibri 24', 
    textvariable=output_str)
output_label.pack(pady=5)

# run
window.mainloop()