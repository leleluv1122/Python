from tkinter import *

class PackManagerDemo:
    def __init__(self):
        window = Tk()
        window.title("Pack Manager Demo 1")

        Label(window, text="Blue", bg="blue").pack(side=LEFT)
        Label(window, text="Red", bg="red").pack(
            side=LEFT,fill = BOTH, expand = 1)
        Label(window, text="Green", bg="green").pack(
            side=LEFT,fill = BOTH)

        window.mainloop()

PackManagerDemo()