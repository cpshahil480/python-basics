from tkinter import *

window=Tk()




label=Label(window,text="welcome")
def hello():
    print("button clicked")

button1=Button(window,text="ok",command=hello)
button2=Button(window,text="ok",command=hello)

button1.grid()
button1.pack()
label.pack()

window.mainloop()