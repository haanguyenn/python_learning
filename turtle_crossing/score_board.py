from turtle import Screen, Turtle

FONT = ('Courtier', 30, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-250, 260)
        self.score = 0
        with open('high_score.txt') as file:
            self.high_score = int(file.read())
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f'Score: {self.score} Highest score: {self.high_score}', font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()
    #
    # def end_game(self):
    #     self.goto(0, 0)
    #     self.write('Game over', align='center', font=FONT)

    def reset_game(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('high_score.txt', 'w') as file:
                file.write(f'{self.high_score}')
        self.score = 0
        self.update_score()

