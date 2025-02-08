import tkinter as tk
import subprocess

file_to_run = ""

def select_function():
    if choose_the_code_you_want_to_run_var.get() == "Books":
        file_to_run = "Books-git-update.sh"
    elif choose_the_code_you_want_to_run_var.get() == "Phy Lab":
        file_to_run = "Phy_Lab_Update.sh"
    elif choose_the_code_you_want_to_run_var.get() == "Automation":
        file_to_run = "Python-Automation.sh"
    elif choose_the_code_you_want_to_run_var.get() == "Spotify Jam":
        file_to_run = "Spotify-Jam.sh"
    elif choose_the_code_you_want_to_run_var.get() == "Wifi":
        file_to_run = "Wifi-Login.sh"
    elif choose_the_code_you_want_to_run_var.get() == "Main-Code":
        file_to_run = "Main-Code.sh"
    elif choose_the_code_you_want_to_run_var.get() == "Shell-Scripts":
        file_to_run = "Shell-Scripts-Update.sh"
    elif choose_the_code_you_want_to_run_var.get() == "DSA-Update":
        file_to_run = "DSA-Update.sh"
    else:
        print("Error")
    
    command_that_executes = f'~/Desktop/Shell-Scripts/./{file_to_run}'

    subprocess.Popen(command_that_executes, shell=True)

main = tk.Tk()
main.geometry("360x175")
main.config(bg="#E4E2E2")
main.title("Shell Runner")

choose_the_code_you_want_to_run_options = ["Books","Phy Lab","Automation","Spotify Jam","Wifi","Main-Code","Shell-Scripts","DSA-Update"]
choose_the_code_you_want_to_run_var = tk.StringVar(value="Choose Program")
choose_the_code_you_want_to_run = tk.OptionMenu(main, choose_the_code_you_want_to_run_var, *choose_the_code_you_want_to_run_options)
choose_the_code_you_want_to_run.config(bg="#fff", fg="#000", bd=1, relief=tk.SUNKEN, font=("Helvetica", 20, ), cursor="arrow", padx=80)
choose_the_code_you_want_to_run.place(x=60, y=25, width=240, height=30)

button = tk.Button(master=main, text="Run Code", command=select_function)
button.config(bg="#E4E2E2", fg="#000", bd=1, relief=tk.RAISED)
button.place(x=140, y=100, width=80, height=40)

main.mainloop()