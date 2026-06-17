from menu import *
from money_machine import *
from coffee_maker import *

order = "ON"
menu = Menu()
coffee = CoffeeMaker()
money = MoneyMachine()
while order != "Off":
    order = input(f"what would you like to order? {menu.get_items()}").lower()
    if order == "off":
        print("Machine OFF")
        break
    drink = menu.find_drink(order)
    if drink:
        print(f"You ordered : {drink.name}")
        print(f"It'll be: ${drink.cost}")
        try :
            if coffee.is_resource_sufficient(drink) == True:
                if money.make_payment(drink.cost) == True:
                    coffee.make_coffee(drink)

        except:
            print("Sorry, we don't have enough coffee.")

