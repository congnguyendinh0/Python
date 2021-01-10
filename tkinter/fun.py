from tkinter import *

window = Tk()
window.title("GUI")
window.minsize(width="500",height="500")

mylabel=Label(text="tkinter label",font=("Arial",24,"bold"))
mylabel.pack(side="left")

mylabel["text"]= "New Text"
mylabel.config(text="New Text")

def click_button():
    print("Hi")


button = Button(text="Click", command=click_button)
button.pack()

window.mainloop()