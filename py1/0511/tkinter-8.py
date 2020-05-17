from tkinter import *

window = Tk()
window.title("my glossary")

Label(window, text="Student ID").grid(row=0,column=0, sticky=E)
Label(window, text="Name").grid(row=1, column=0, sticky=E)
Label(window, text="Phone Number").grid(row=2, column=0, sticky=E)


entry1 = Entry(window, width=20, bg="White")
entry2 = Entry(window, width=20, bg="White")
entry3 = Entry(window, width=20, bg="White")

entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)
entry3.grid(row=2, column=1)

window.mainloop()