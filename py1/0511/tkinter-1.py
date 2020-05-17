from tkinter import *

window = Tk()
window.title("My glossary")
window.geometry("500x500") # default size

#label = Label(window, text="text")
#label.pack()

#Label(window, text="text").grid(row=0, column=0,\
#                                sticky=W)

label = Label(window, text="text")
label.grid(row=0, column=0, sticky=W)

window.mainloop()