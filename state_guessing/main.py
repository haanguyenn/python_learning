from turtle import Turtle, Screen
import pandas as pd
from get_name import Name

turtle = Turtle()
screen = Screen()
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

data_file = pd.read_csv('50_states.csv')
all_state = data_file.state.tolist()
correct_count = 0
correct_list = []

game_is_on = True
while game_is_on:
    guess = screen.textinput(f'{correct_count}/50 Correct', 'What is another state name?')
    state_guess_info = data_file[data_file['state'] == guess.title()]
    screen.tracer(0)  # prevent screen flash
    if not state_guess_info.empty:
        if guess not in correct_list:
            screen.update()  # update screen
            x_cor = state_guess_info['x'].tolist()  # or use int(state_info.x)
            y_cor = state_guess_info['y'].tolist()
            name_state = Name()
            name_state.goto(x_cor[0], y_cor[0])
            name_state.write(guess, font=('monaco', 10, 'bold'))
            correct_count += 1
            correct_list.append(guess)
    if guess == 'exit':
        game_is_on = False
        missing_state = [state for state in all_state if state not in correct_list]
        df_missing_state = pd.DataFrame(missing_state)
        df_missing_state.to_csv('your_missing_answer.csv')
        screen.bye()
screen.mainloop()
