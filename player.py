from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.screen.register_shape("player.gif")
        self.shape("player.gif")
        self.penup()
        self.goto(0, -250)

    def go_right(self):
        new_x = self.xcor() + 40
        if -230 <= new_x <= 230:
            self.goto(new_x, self.ycor())

    def go_left(self):
        new_x = self.xcor() - 40
        if -230 <= new_x <= 230:
            self.goto(new_x, self.ycor())

    def revive(self):
        self.goto(0, -250)
