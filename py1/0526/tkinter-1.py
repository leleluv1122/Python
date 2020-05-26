from tkinter import *

def processOK():
    print("OK button is clicked")

def processCancel():
    print("Cancel button is clicked")

window = Tk()
btnOK = Button(window, text="OK", fg="red", command = processOK)
btnCancel = Button(window, text="Cancel", bg="yellow",
                   command = processCancel)

btnOK.pack()
btnCancel.pack()

window.mainloop()