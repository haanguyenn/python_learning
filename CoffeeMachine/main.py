MENU = {
    'espresso': {
        'ingredients': {
            'water': 50,
            'coffee': 18,
        },
        'cost': 1.5,
    },
    'latte': {
        'ingredients': {
            'water': 200,
            'milk': 150,
            'coffee': 24,
        },
        'cost': 2.5,
    },
    'cappuccino': {
        'ingredients': {
            'water': 250,
            'milk': 100,
            'coffee': 24,
        },
        'cost': 3.0,
    }
}

resources = {
    'water': 300,
    'milk': 200,
    'coffee': 100,
}

profit = 0
# TODO:  4. Check resources
def check_resources_sufficient(drink_ingredient):
    for item in drink_ingredient:
        if drink_ingredient[item] > resources[item]:
            print(f'Sorry there is not enough {item}.')
            return False
        return True


# TODO: 5. Process coins & get total paid
def coin_insert():
    print('Please insert coins.')
    quarters = int(input('How many quarters: '))
    dimes = int(input('How many dimes: '))
    nickles = int(input('How many nickles: '))
    pennies = int(input('How many pennies: '))
    paid = round((quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01), 2)
    return paid

#Check if the paid is sufficient for purchase
def payment_proceed(paid_total, price):
    if paid_total > price:
        global profit
        profit += price
        changes = round((paid_total - price), 2)
        print(f'Here is {changes} in changes')
        return True
    else:
        print('Sorry that is not enough money. Money refunded.')
        return False


# TODO: 7. Make coffee and deduct resources
def update_report(drink_ingredient):
    for item in drink_ingredient:
        resources[item] -= drink_ingredient[item]
        # print(f'{item}: {resources[item]}')


is_continue = True
while is_continue:

    order = input('What would you like? (espresso/latte/cappuccino): ')
    if order == 'off':
        is_continue = False
    elif order == 'report':
        for item in resources:
            print(f'{item}: {resources[item]}')
        print(f'money: {profit}')
    else:
        drink_ingredient = MENU[order]['ingredients']
        resources_sufficient = check_resources_sufficient(drink_ingredient)
        if resources_sufficient:
            #Call the get coins
            paid_total = coin_insert()
            price = MENU[order]['cost']
            if payment_proceed(paid_total, price):
                update_report(drink_ingredient)
                print(f'Here is your {order} ☕️.Enjoy!')
        else:
            is_continue = False

        # TODO: 6. Check transaction

        if input('Type yes if you want to re-order: ') != 'yes':
            print('Thank you. See you next time!')
            is_continue = False
