def print_message():
  print('We\'re sorry, we did not understand your selection. Please enter the corresponding letter for your response.')


def get_drink_type():
  res = input('What type of drink would you like?\n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n>')
  if res.lower() == 'a':
    return 'Brewed Coffee'
  elif res.lower() == 'b':
    return order_mocha()
  elif res.lower() == 'c':
    return order_latte()
  else:
    print_message()
    return get_drink_type()

def get_size():
  res = input('What size drink can I get for your? \n[a] Tall \n[b] Grande \n[c] Venti \n>')
  if res.lower() == 'a':
    return 'Tall'
  elif res.lower() == 'b':
    return 'Grande'
  elif res.lower() == 'c':
    return 'Venti'
  else:
    print_message()
    return get_size()

def order_latte():
  res = input('And what kind of milk for your latte?\n[a] 2% milk \n[b] Non-fat milk \n[c] Soy milk \n>')
  if res.lower() == 'a':
    return 'Latte with 2% milk'
  elif res.lower() == 'b':
    return 'Latte with Non-fat milk'
  elif res.lower() == 'c':
    return 'Latte with Soy milk'
  else:
    print_message()
    return order_latte()

def order_mocha():
  while True:
    res = input('Would you like to try our limited-edition peppermint mocha?\n[a] Sure! \n[b] Maybe next time!\n>')
    if res.lower() == 'a':
      return 'peppermint mocha'
    elif res.lower() == 'b':
      return 'Mocha'
    print_message()


def get_name():
  res = input('Can we get your name? :')
  return res
