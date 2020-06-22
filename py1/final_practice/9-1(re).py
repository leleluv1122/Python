from tkinter import *

class Ball:
    def __init__(self):
        window = Tk()
        window.geometry("400x229")
        window.title("공 옮기기")

        canvas = Canvas(window, width=400, height=200, bg="white")
        canvas.pack()

        canvas.create_oval(100, 120, 130, 150, fill="blue")

        btn1 = Button(window, text="좌", command=self.f_left)
        btn1.place(x=145, y=203)
        btn2 = Button(window, text="우", command=self.f_right)
        btn2.place(x=170, y=203)
        btn3 = Button(window, text="상", command=self.f_up)
        btn3.place(x=195, y=203)
        btn4 = Button(window, text="하", command=self.f_down)
        btn4.place(x=220, y=203)

        window.mainloop()

    def f_left(self):
        self.canvas.move(-10, 0)

    def f_right(self):
        self.canvas.move(10, 0)

    def f_up(self):
        self.canvas.move(0, -10)

    def f_down(self):
        self.canvas.move(0, 10)

Ball()