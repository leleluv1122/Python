import tkinter as tk

class Game(tk.Frame):
    def __init__(self, master):
        super(Game, self).__init__(master)
        self.width = 610
        self.height= 400
        self.canvas = tk.Canvas(self, bg ="white", width = self.width, height = self.height)
        self.canvas.pack()
        self.pack()
        self.ball = Ball(self.canvas, self.width/2, self.height/2)

        self.canvas.focus_set()
        self.canvas.bind('<Left>',
                         lambda _: self.ball.move(-10, 0))
        self.canvas.bind('<Right>',
                         lambda _: self.ball.move(10, 0))
        self.canvas.bind('<Up>',
                         lambda _: self.ball.move(0, -10))
        self.canvas.bind('<Down>',
                         lambda _: self.ball.move(0, 10))

class GameObject:
    def __init__(self, canvas, item):
        self.canvas = canvas
        self.item = item

    def move(self, x, y):
        self.canvas.move(self.item, x, y)

class Ball(GameObject):
    def __init__(self, canvas, x, y):
        self.radius = 10
        item = canvas.create_oval(x-self.radius, y-self.radius,
                                  x+self.radius, y+self.radius,
                                  fill='black')
        super(Ball, self).__init__(canvas, item)


if __name__ == '__main__':
    root = tk.Tk()
    root.title('공 움직이기')
    game = Game(root)
    game.mainloop()