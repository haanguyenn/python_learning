#2 Sep 2021
import os

logo = logo = """
 _____________________
|  _________________  |
| | Lynn           0. | |  .----------------.  .----------------.  .----------------.  .----------------.
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------'
|_____________________|
"""

def add(a,b):
  return a + b

def substract(a,b):
  return a - b

def multiply(a,b):
  return a * b

def divide(a,b):
  return a / b

def exponent(a,b):
  return a ** b

operators = {
  '+' : add,
  '-' : substract,
  '*' : multiply,
  '/' : divide,
  '**': exponent
}

def calculation():
  cont = True
  print(logo)
  num1 = float(input('What is the number? '))
  for item in operators:
    print(item)
  while cont:
    chosen_operator = input('Pick an operator: ')
    if chosen_operator in operators:
      num2 = float(input('What is next number? '))
      total = operators[chosen_operator](num1,num2)
      print(f'{num1} {chosen_operator} {num2} = {total}')
      is_continue = input(f'Type Y if you want to continue with {total}, R to reset or N to exit: ').lower()

      if is_continue == 'y':
        num1 = total
      elif is_continue == 'r':
        os.system('clear')
        calculation()
        cont = False
      elif is_continue == 'n':
        print('Thanks for using. Bye!')
        cont = False
    else:
      print('Invalid operator. Please try again')

calculation()
