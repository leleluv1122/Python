from tkinter import *
import time

window = Tk()
window.geometry("400x229")
window.title("공 옮기기")

canvas = Canvas(window, width=400, height=200, bg="white")
canvas.pack()

canvas.create_oval(100, 120, 130, 150, fill="blue")

def f_left():
    coords = canvas.coords(1)
    if coords[0] >= 0:
        canvas.move(1, -10, 0)

def f_right():
    coords = canvas.coords(1)
    if coords[2] <= 400:
        canvas.move(1, 10, 0)

def f_up():
    coords = canvas.coords(1)
    if coords[1] >= 0:
        canvas.move(1, 0, -10)

def f_down():
    coords = canvas.coords(1)
    if coords[3] <= 200:
        canvas.move(1, 0, 10)


btn1 = Button(window, text="좌", command=f_left)
btn1.place(x=145, y=203)
btn2 = Button(window, text="우", command=f_right)
btn2.place(x=170, y=203)
btn3 = Button(window, text="상", command=f_up)
btn3.place(x=195, y=203)
btn4 = Button(window, text="하", command=f_down)
btn4.place(x=220, y=203)

window.mainloop()