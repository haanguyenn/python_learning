import random
import os
print('Welcome to the Blackjack')

#Pick random card
def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

#Check blackjack and return sum
def score_calculate(lst):
  total = sum(lst)
  if total == 21 and len(lst) == 2:
    return 0
  elif total > 21 and 11 in lst:
    lst.remove(11)
    lst.append(1)
    return total
  else:
    return total

#Check final result
def compare(user_score, dealer_score):
  if user_score == dealer_score:
    print ('It is a draw.')
  elif dealer_score == 0:
    print('Blackjack. Dealer wins!')
  elif user_score == 0:
    print('Blackjack. You win!')
  elif user_score > 21:
    print('Bust! Dealer wins!')
  elif dealer_score > 21:
    print('Bust! You win!')
  elif user_score > dealer_score:
    print('You win')
  else:
    print('Dealer wins')

def play_game():
  user_card = []
  dealer_card = []
  for item in range(2):
    user_card.append(deal_card())
    dealer_card.append(deal_card())

  print(f'Your card: {user_card}')
  print(f'Dealer card: {dealer_card[0]}, x')
  game_end = False
  while not game_end:
    user_score = score_calculate(user_card)
    print(f'With {user_card}, your score is: {user_score}')
    dealer_score =score_calculate(dealer_card)

    #Check if any of player get blackjack and flag the game_end
    if user_score == 21 or dealer_score == 21 or user_score > 21:
      game_end = True
    else:
      more_draw = input('Do you want to draw another card? Type y or n: ')
      if more_draw == 'y':
        user_card.append(deal_card())
      else:
        game_end = True
      while dealer_score < 17:
        dealer_card.append(deal_card())
        dealer_score =score_calculate(dealer_card)

  print(f'With {dealer_card}, the dealer score is: {dealer_score}')
  compare(user_score, dealer_score)
# Clear the console and play a new game
  while input('Type y if you want to play a new game and n to exit: ') == 'y':
    os.system('clear')
    play_game()

play_game()






















