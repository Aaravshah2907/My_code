import tkinter as tk
from tkinter import ttk

def get_pos(event):
    print(f' x: {event.x} y: {event.y}')

# window
window = tk.Tk()
window.title("Buttons")
window.geometry('600x500')

# widgets
text = tk.Text(window)
text.pack()

entry = ttk.Entry(window)
entry.pack()

btn = ttk.Button(window, text='Button')
btn.pack()


# events
# window.bind('<Alt-KeyPress-a>', lambda event: print(event))
btn.bind('<Alt-KeyPress-a>', lambda event: print(event))
window.bind('<Motion>', get_pos)

window.bind('<KeyPress>', lambda event: print(f'A button was pressed ({event.char})'))

entry.bind('<FocusIn>', lambda event: print('Entry Field was selected.'))
entry.bind('<FocusOut>', lambda event: print('Entry Field was deselected.'))

text.bind('<Shift-MouseWheel>',lambda event: print("Shift+Mousewheel Detected"))

# run
window.mainloop()