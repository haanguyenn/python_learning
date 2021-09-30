import time
from turtle import Screen
from player import Player
from car_manager import Car
from score_board import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('white')
screen.title('Turtle Crossing Capstone by imlynn')
screen.tracer(0)

player = Player()
screen.listen()
screen.onkey(player.move_forward, 'Up')

score_board = ScoreBoard()
game_is_on = True
game_loop = 0
lst_car = []
while game_is_on:
    time.sleep(0.1)
    screen.update()
    # create a new car every 6th loop
    if game_loop % 6 == 0:
        car = Car()
        lst_car.append(car)

    # create a series of car moving
    for num in range(len(lst_car)):
        lst_car[num].move_car()

    # detect player collide with top edge & need more precise on collision
    for car in lst_car:
        if player.distance(car) < 20:
            print('Contacted')
            score_board.reset_game()
            player.reset_game()

    # detect player collide top edge
    if player.ycor() > 280:
        player.starting_pos()
        score_board.clear()
        score_board.increase_score()
        car.speed_up()
    game_loop += 1

screen.exitonclick()
