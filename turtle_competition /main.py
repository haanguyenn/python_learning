from turtle import Turtle, Screen
import turtle

my_turtle = Turtle()
my_turtle.shape('turtle')
my_turtle.color('blue')
my_screen = Screen()


def backward():
    return my_turtle.backward(10)


def forward():
    return my_turtle.forward(10)


def turn_left():
    new_heading = my_turtle.heading() + 10
    return my_turtle.setheading(new_heading)


def turn_right():
    new_heading = my_turtle.heading() - 10
    return my_turtle.setheading(new_heading)


def clear():
    my_turtle.clear()
    my_turtle.penup()
    my_turtle.home()
    my_turtle.pendown()



my_screen.onkey(key='s', fun=backward)
my_screen.onkey(key='w', fun=forward)
my_screen.onkey(key='a', fun=turn_left)
my_screen.onkey(key='d', fun=turn_right)
my_screen.onkey(key='c', fun=clear)

my_screen.listen()
my_screen.exitonclick()
