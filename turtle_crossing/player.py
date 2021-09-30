from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('green')
        self.penup()
        self.left(90)
        self.starting_pos()

    def starting_pos(self):
        self.goto(0, -280)

    def move_forward(self):
        new_y = self.ycor() + 10
        self.goto(0, new_y)

    def reset_game(self):
        self.starting_pos()


