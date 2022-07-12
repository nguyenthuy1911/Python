from tkinter import*
from tkinter.ttk import*
from time import strftime

root = Tk()
root.title("Digital Clock")
def clock():
    string = strftime('%H: %M: %S')
    label.config(text = string)
    label.after(1000, clock)

label = Label(root, font=("Digital-7", 50), background='black', foreground='red')
label.pack(anchor='center')
clock()

root.mainloop()