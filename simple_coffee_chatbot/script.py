import utils as ul

def coffee_bot():
  print('Welcome to the cafe!')
  drinks = []
  order_drink = 'y'
  while order_drink.lower() == 'y':
    size = ul.get_size()
    print('Great!')
    drink_type = ul.get_drink_type()
    drink = '{} {}'.format(size,drink_type)
    drinks.append(drink)
    print('Alright! That\'s a', drink )
    while True:
      order_drink = input('Would you like to order another drink? (y/n) \n')
      if order_drink in ['y', 'n', 'Y', 'N']:
        break
  name = ul.get_name()
  print('Awesome {}! Here\'s your order: '.format(name))
  for item in drinks:
    print('- ', item)
  print('Your drink will be ready shortly. Please go the counter to get your drinks!')


coffee_bot()

