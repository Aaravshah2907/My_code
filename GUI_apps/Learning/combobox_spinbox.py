import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title("Buttons")
window.geometry('600x500')

# Combobox
items = ['icecream','pizza','pasta']
food_str = tk.StringVar(value = 'Default Value')
cmbbos = ttk.Combobox(window,textvariable=food_str)
cmbbos['values'] = items
# cmbbos.config(values=items)
# cmbbos.configure(values=items)
cmbbos.pack()

# events for Combobox
cmbbos.bind('<<ComboboxSelected>>', lambda event: print(f'{food_str.get()} was selected'))
# cmbbos_label = ttk.Label(window, text=food_str.get())
# By defualt the second bind function will only execute.
cmbbos.bind('<<ComboboxSelected>>', lambda event: cmbbos_label.configure(text=f'{food_str.get()} was selected'))
cmbbos_label = ttk.Label(window, text='A trial')
cmbbos_label.pack()

# Spinbox

list_values = [0,1,2,3,4,5,6,7,8,9]
trial_str = tk.StringVar(value = list_values[5])
spnbox = ttk.Spinbox(window,textvariable=trial_str, command = lambda : print("Arrow pressed"))
spnbox['values'] = list_values
# spnbox.config(values=items)
# spnbox.configure(values=items)
spnbox.pack()
# event: spnbox_label.config(text=trial_str.get())
# events for Combobox
spnbox.bind('<<Increment>>', lambda event: print(f'{trial_str.get()} was selected'))
# spnbox_label = ttk.Label(window, text=food_str.get())
# By defualt the second bind function will only execute.
spnbox.bind('<<Decrement>>', lambda event: print(f'{trial_str.get()} was selected'))


# exercise
ex_letters = ['A', 'B', 'C', 'D', 'E']
ex_str = tk.StringVar(value=ex_letters[0])
ex_spin = ttk.Spinbox(window, textvariable=ex_str, values= ex_letters)
ex_spin.pack()

ex_spin.bind('<<Decrement>>', lambda event: print(f'{ex_str.get()} was selected to be decremented'))
# run
window.mainloop()