from tkinter import *

window = Tk()
window.title("my glossary")

Label(window, text="First Name").grid(row=0,column=0)
Label(window, text="Last Name").grid(row=1, column=0)


entry1 = Entry(window, width=20, bg="Yellow")
entry2 = Entry(window, width=20, bg="Green")

entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)

window.mainloop()