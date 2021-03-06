import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
#First choice: handle by list
password = []
for i in range (0,nr_letters):
  password.append(letters[i])

for i in range (0, nr_numbers):
  password.append(numbers[i])

for i in range (0, nr_symbols):
  password.append(symbols[i])
yourpw = ''.join(password)
print(f"Your password is {yourpw}")

#Second choice: handle by str
password = ''
for i in range(0,nr_numbers+1):
  password +=  random.choice(numbers)

for i in range(0,nr_symbols+1):
  password +=  random.choice(symbols)

for i in range(0,nr_letters+1):
  password +=  random.choice(letters)

print(f"Your password is {password}")

#Order of characters randomised:
# 4 letter, 2 symbol, 2 number = g^2jk8&P
password2 = []
for i in range (0,nr_letters):
  password2.append(random.choice(letters))

for i in range (0, nr_numbers):
  password2.append(random.choice(numbers))

for i in range (0, nr_symbols):
  password2.append(random.choice(symbols))

random.shuffle(password2)
yourpw2 = ''.join(password2)

print(f"Your password is {yourpw2}")
