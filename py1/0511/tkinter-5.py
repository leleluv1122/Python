from tkinter import *

window = Tk()
window.title("my glossary")

button = Button(window, text="This text is very very very long", width=30, bg="Yellow", fg="Blue")
button.grid(row=0,column=0,sticky=E)

button1 = Button(window, text="Click2",width=30,  fg="Green", bg="White")
button1.grid(row=0, column=1, sticky=E)

button2 = Button(window, text="Click3",width=30,  fg="Purple", bg="White" )
button2.grid(row=1, column=0, sticky=E)

button3 = Button(window, text="This text is very very very long",width=30,  bg="Yellow", fg="Red")
button3.grid(row=1, column=1, sticky=E)

window.mainloop()