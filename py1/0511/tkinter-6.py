from tkinter import *

window = Tk()

button1 = Button(window, text="Click1",width=10,  fg="Blue")
button1.grid(row=0, column=1, sticky=W)

button2 = Button(window, text="Click2",width=10,  fg="Green")
button2.grid(row=0, column=2, sticky=W)

button3 = Button(window, text="Click3",width=10,  fg="Purple")
button3.grid(row=0, column=3, sticky=W)

button4 = Button(window, text="Click4",width=10,  fg="Red")
button4.grid(row=0, column=4, sticky=W)

button5 = Button(window, width=20, text="Reset", fg="Red", bg="Yellow")
button5.grid(row=1, column=2,columnspan=2, sticky=S)


window.mainloop()