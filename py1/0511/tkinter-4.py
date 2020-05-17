from tkinter import *

window = Tk()
window.title("my gloassary")

button = Button(window, text="Click", fg="Blue")
button.pack()

button2 = Button(window, text="Reset", fg="Red", bg="Yellow")
button2.pack()

window.mainloop()