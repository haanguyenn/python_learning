#29Aug2021
from game_hangman_resource import logo, word_list, stages
import random

#print game logo
print(logo)

display = []
lives = 6
end_game = False
false_guess = []

#system generates random word
chosen_word = random.choice(word_list)

for char in chosen_word:
  display += '_'
print(f'Here is the word you gonna guess: {display}')
print(f'Test: The system chose: {chosen_word}')

while not end_game:
  user_guess = input('Pick a character: ').lower()
  if user_guess in display:
    print(f'Hey, {user_guess} is correct but it is already here. Go with another character.')
  else:
    for position in range(len(chosen_word)):
      letter = chosen_word[position]
      if letter == user_guess:
        display[position] = letter
    print(' '.join(display))

  if user_guess not in chosen_word:
    if user_guess not in false_guess:
      false_guess.append(user_guess)
      lives -= 1
      print(f'Unfortunately, you lost a live. You only have {lives} time to try.')
      if lives == 0:
        end_game = True
        print('Unfortunately, you lost the game.')
      print(stages[lives])
    else:
      print(f'You guessed {user_guess} already. We will not count this time. Please try with another.')

  if '_' not in display:
    end_game = True
    print('You win the game. Congrats!')
