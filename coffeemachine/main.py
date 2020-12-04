from menu import MENU
from menu import resources
import math
decimal = ".2f"
water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]
money = 0
machine_on = True
def process_payment():
    quaters = int(input("quaters?")) * .25
    dimes = int(input("dimes?")) * .10
    nickles = int(input("nickles?")) * .05
    pennies = int(input("pennies?")) * .01

    total_cash = quaters + dimes + nickles + pennies
    print(f"Total money inserted: ${format(total_cash, decimal)}")
    def change_given(drink_price, total_cash):
        if total_cash < drink_price:
            print("Sorry that's not enough money. Money Refunded")
            global machine_on
            machine_on = False
        else:
            change = total_cash - drink_price
            print(f"Enjoy your {drink} ☕")
            return format(change, decimal)
    
    print(f"Your change: ${change_given(drink_price, total_cash)}")

while machine_on:
    drink = input("What would you like? (espresso/latte/cappuccino):").lower()

    if drink == "espresso":
        if water < MENU[drink]["ingredients"]["water"]:
            print(f"Sorry there is not enough water")
            machine_on = False
        elif coffee < MENU[drink]["ingredients"]["coffee"]:
            print(f"Sorry there is not enough coffee")
            machine_on = False
        else:
            drink_price = MENU[drink]["cost"]
            water -= MENU[drink]["ingredients"]["water"]
            coffee -= MENU[drink]["ingredients"]["coffee"]
            process_payment()
            money += drink_price
    elif drink == "latte":
        if water < MENU[drink]["ingredients"]["water"]:
            print(f"Sorry there is not enough water")
            machine_on = False
        elif milk < MENU[drink]["ingredients"]["coffee"]:
            print("Sorry there is not enough milk")
            machine_on = False
        elif coffee < MENU[drink]["ingredients"]["coffee"]:
            print(f"Sorry there is not enough coffee")
            machine_on = False
        else:
            drink_price = MENU[drink]["cost"]
            water -= MENU[drink]["ingredients"]["water"]
            milk -= MENU[drink]["ingredients"]["milk"]
            coffee -= MENU[drink]["ingredients"]["coffee"]   
            process_payment()
            money += drink_price
    elif drink == "cappuccino":
        if water < MENU[drink]["ingredients"]["water"]:
            print("Sorry there is not enough water")
            machine_on = False
        elif milk < MENU[drink]["ingredients"]["milk"]:
            print("Sorry there is not enough milk")
            machine_on = False
        elif coffee < MENU[drink]["ingredients"]["coffee"]:
            print("Sorry there is not enough coffee")
            machine_on = False
        else:
            drink_price = MENU[drink]["cost"]
            water -= MENU[drink]["ingredients"]["water"]
            milk -= MENU[drink]["ingredients"]["milk"]
            coffee -= MENU[drink]["ingredients"]["coffee"]              
            process_payment()
            money += drink_price
    elif drink == "report":
        print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${money}")
    elif drink == "off":
        machine_on = False
    else:
        print(f"We dont have {drink}, please pick something else..")



