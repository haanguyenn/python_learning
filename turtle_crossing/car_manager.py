from turtle import Turtle
import random

COLOR = ['red', 'yellow', 'blue', 'orange', 'deep pink', 'indigo']
X_CAR = 280


class Car(Turtle):
    def __init__(self):
        super().__init__('square')
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.penup()
        self.starting_position()
        self.color(random.choice(COLOR))
        self.speed = 5

    def starting_position(self):
        new_y = random.randint(-230, 280)
        self.goto(X_CAR, new_y)

    def move_car(self):
        new_x = self.xcor() - self.speed
        self.goto(new_x, self.ycor())

    def speed_up(self):
        self.speed += 10
