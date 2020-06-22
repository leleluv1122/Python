from tkinter import *

def Check_button():
    if v1.get() == 1:
        print(1, "채우기")
    else:
        print(1, "안채우기")

def Radio_button():
    if v2.get() == 1:
        canvas.delete(2)
        canvas.create_rectangle(10, 10, 350,100)
    else:
        canvas.delete(1)
        canvas.create_oval(0, 20, 30, 50, fill="blue")

window = Tk()
window.title("라디오 버튼과 체크 버튼")

frame1 = Frame(window)
frame1.pack()

canvas = Canvas(window, bg="white", height=130)
canvas.pack()


frame2 = Frame(window)
frame2.pack()
v1 = IntVar()
cbtBold = Checkbutton(frame2, text="채우기", variable = v1, command = Check_button)
v2 = IntVar()
rbRed = Radiobutton(frame2, text="직사각형", variable = v2, value = 1, command = Radio_button)
rbYellow = Radiobutton(frame2, text="타원", variable = v2, value = 2, command = Radio_button)

cbtBold.grid(row=1, column=4)
rbRed.grid(row=1, column=2)
rbYellow.grid(row=1, column=3)

window.mainloop()