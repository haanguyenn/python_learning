import random
from turtle import Turtle, Screen

my_screen = Screen()
my_screen.setup(600, 600)
user_bet = my_screen.textinput('Make your bet', 'Which one is the winner? Type your answer: ')
colors = ['yellow', 'black', 'orange', 'red', 'maroon', 'blue', 'purple']
y_position = [-200, -150, -100, 0, 100, 150, 200]
turtle_lst = []
for index in range(len(colors)):
    my_turtle = Turtle(shape='turtle')
    my_turtle.color(colors[index])
    my_turtle.penup()
    my_turtle.goto(x=-280, y=y_position[index])
    turtle_lst.append(my_turtle)


def move_forward():
    distance = random.randint(0, 10)
    turtle.forward(distance)


race_on = False
if user_bet:
    race_on = True
while race_on:
    for turtle in turtle_lst:
        move_forward()
        if turtle.xcor() > 280:
            winning_turtle = turtle.pencolor()
            if user_bet == winning_turtle:
                print(f'You win!The winner is the {winning_turtle} turtle')
            else:
                print(f'You lose!The winner is the {winning_turtle} turtle')
            race_on = False

my_screen.exitonclick()
