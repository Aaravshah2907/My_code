import tkinter as tk

# window
window = tk.Tk()
window.title("Buttons")
window.geometry('600x500')

# canvas
canvas = tk.Canvas(window, bg = 'white')
canvas.pack()

canvas.create_rectangle((50,20,100,200), fill='red', width=10, dash=(4,2))
# run
window.mainloop()