from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = False
while not is_on:
    coffee_menu = Menu()
    coffee_maker_obj = CoffeeMaker()
    money = MoneyMachine()
    order = input('What would you like? (espresso/latte/cappuccino): ').lower()
    if order == 'report':
        coffee_maker_obj.report()
        money.report()
    elif order == 'off':
        is_on = True
    else:
        item_object = coffee_menu.find_drink(order)
        if coffee_maker_obj.is_resource_sufficient(item_object):
            if money.make_payment(item_object.cost):
                coffee_maker_obj.make_coffee(item_object)
