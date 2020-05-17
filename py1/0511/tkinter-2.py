from tkinter import *

window = Tk()
window.title("my glossary")
#window.geometry("500x500")

#Label(window, text="This is the first label").grid(row=0,column=0, sticky=W)
label = Label(window, text="This is the first label")
label.grid(row=0,column=0, sticky=W)

window.mainloop()