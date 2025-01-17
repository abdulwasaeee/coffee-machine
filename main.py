MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk":0
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
money=0
running=True

def resource_check(drink):
    for i in MENU[drink]["ingredients"]:
        if MENU[drink]["ingredients"][i]>resources[i]:
            print(f"Sorry there is not enough {i}.")
            return False
        return True


def payment_check(pay,drink):
    if pay<MENU[drink]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        return False
    return True


def make(drink):
    for i in MENU[drink]["ingredients"]:
     resources[i]-=MENU[drink]["ingredients"][i]
print("***COFFEE MACHINE***\n")
while running:
    coffee=input("What would you like? (espresso/latte/cappuccino): ")
    if coffee=="off":
        running=False
    elif coffee=="report":
        print(f"Water: {resources["water"]}ml\nMilk: {resources["milk"]}ml\nCoffee: {resources["coffee"]}g\nMoney: ${money}")
    elif coffee=="espresso" or coffee=="latte" or coffee=="cappuccino":
        if resource_check(coffee):
            print("Please insert coins: ")
            quarters=int(input("quarters: "))
            dimes = int(input("dimes: "))
            nickles = int(input("nickels: "))
            pennies = int(input("pennies: "))
            payment=quarters*0.25+dimes*0.10+nickles*0.05+pennies*0.01
            print(f"paid ${payment}")
            if payment_check(payment,coffee):
                money+=MENU[coffee]["cost"]
                change=round(payment-MENU[coffee]["cost"],2)
                print(f"Here is ${change} dollars in change 🪙")
                make(coffee)
                print(f"Here is your {coffee}. Enjoy! ☕")
    else:
        print("Sorry we don't serve that")

