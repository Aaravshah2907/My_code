import tkinter as tk

def save_input():
    display_text = user_entry_input.get() * 100
    user_entry_input.set(0)

window = tk.Tk()
window.title('Miles To Kilometres')
window.geometry('300x150')

heading_text_label = tk.Label(master=window, text='Miles To Kilometres', font='Calibri 24 bold')
heading_text_label.pack()

input_frame= tk.Frame(master=window)
user_entry_input = tk.IntVar()
user_entry = tk.Entry(master=input_frame, textvariable=user_entry_input)
submit_button = tk.Button(master=input_frame, text='Convert', command=save_input)
user_entry.pack(side='left',padx=10)
submit_button.pack(side='left')
input_frame.pack(pady=10)

display_text = tk.IntVar()
display_text = 0
output_label = tk.Label(master=window, textvariable=display_text)
output_label.pack()

window.mainloop()
