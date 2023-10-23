from data import MENU
import data


amount = 0
milk = data.resources['milk']
water = data.resources['water']
coffee = data.resources['coffee']


def set_coffee_type(coffee_order):
    return coffee_order


def check_resources(coffee_type):
    if MENU[coffee_type]['ingredients']['water'] < water:
        if MENU[coffee_type]['ingredients']['coffee'] < coffee:
            if coffee_type == 'espresso':
                return True
            else:
                if MENU[coffee_type]['ingredients']['milk'] < milk:
                    return True
                else:
                    return 'Sorry there is not enough milk.'
        else:
            return 'Sorry there is not enough coffee.'
    else:
        return 'Sorry there is not enough water.'


def deduct_things(coffee_type):
    print(f'Here is your {coffee_type} ☕.Enjoy!')
    global water
    global milk
    global coffee
    global amount
    amount += 2.5
    water -= MENU[coffee_type]['ingredients']['water']
    coffee -= MENU[coffee_type]['ingredients']['coffee']
    if coffee_type == 'espresso':
        return
    milk -= MENU[coffee_type]['ingredients']['milk']


is_on = False
while not is_on:
    order = input('What would you like? (espresso/latte/cappuccino): ').lower()
    if order == 'report':
        print(f'''Milk: {milk}
Water = {water}
Coffee = {coffee}
Money =  ${amount}
        ''')
    elif order == 'off':
        is_on = True
    else:
        order_of_coffee = set_coffee_type(order)
        checked = check_resources(order_of_coffee)
        if checked == True:
            print('Please insert coins.')
            quarters = int(input('How many quarters? '))
            dimes = int(input('How many dimes? '))
            nickles = int(input('How many nickles? '))
            pennies = int(input('How many pennies? '))
            money = 0.25 * quarters + 0.10 * dimes + 0.05 * nickles + 0.10 * pennies
            money = round(money , 3)
            if money > 2.5:
                print(f'Here is your change ${round(money - 2.50 ,5)}.')
                deduct_things(order_of_coffee)
            elif money == 2.5:
                deduct_things(order_of_coffee)
            else:
                print("Sorry that's not enough money. Money refunded.")
        else:
            print(checked)










