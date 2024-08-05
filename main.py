MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
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
def check_resources(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item]>=resources[item]:
            print(f"sorry there is not enough {item}")
            return False
    return True

def process_coins():
    '''returns the total of the coins inserted'''
    print("INSERT COINS")
    quarters = int(input("how many quarters?")) * 0.25
    dimes = int(input("how many dimes?")) * 0.10
    nickels = int(input("how many nickels?")) * 0.05
    pennies = int(input("how many pennies?")) * 0.01
    total = quarters + dimes + nickels + pennies
    return total

def is_transaction_successful(money_recieved,drink_cost):
    if money_recieved>=drink_cost:
        change=round(money_recieved-drink_cost,2)
        print(f"here is ${change} in change")
        global profit
        profit+=drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded")
        return False

def make_coffee(drink_choice,order_ingredients):
    for item in order_ingredients:
        resources[item]-=order_ingredients[item]
    print(f"here is your {drink_choice}")

profit=0
machine_on=True
while machine_on:
    choice=input("What would you like? (espresso/latte/cappuccino):").lower()
    if choice=="off":
         machine_on=False
    elif choice=="report":
        print(f"water:{resources['water']},\nmilk:{resources['milk']},\ncoffee:{resources['coffee']},\nmoney:${profit}")
    else:
        if choice in MENU:
            drink=MENU[choice]
            if check_resources(drink["ingredients"]):
                payment=process_coins()
                if is_transaction_successful(payment,drink["cost"]):
                    make_coffee(choice,drink["ingredients"])
        else:
            print("oops couldn't find your drink. enter a valid drink name!")




