from Art import vending_machine_logo
from Art import coffee_emoji


def report():
    print("Available resources: ")
    print(f"Water left: {vending_resources["Water"]}ml")
    print(f"Milk left: {vending_resources["Milk"]}ml")
    print(f"Coffee left: {vending_resources["Coffee"]}g")
    print(f"Money left: ${vending_resources["Money"]}")


def resource_check(selection):
    not_enough = {}
    if selection == "espresso":
        if vending_resources["Water"] < 50:
            not_enough["Water"] = vending_resources["Water"]
        if vending_resources["Coffee"] < 18:
            not_enough["Coffee"] = vending_resources["Coffee"]
        if not_enough != {}:
            for x in not_enough:
                aquarius = x
                print(f"We are low on {aquarius}")
            return False
        else:
            vending_resources["Water"] = vending_resources["Water"] - 50
            vending_resources["Coffee"] = vending_resources["Coffee"] - 18
            return True
    if selection == "latte":
        if vending_resources["Water"] < 200:
            not_enough["Water"] = vending_resources["Water"]
        if vending_resources["Milk"] < 150:
            not_enough["Milk"] = vending_resources["Milk"]
        if vending_resources["Coffee"] < 24:
            not_enough["Coffee"] = vending_resources["Coffee"]
        if not_enough != {}:
            for x in not_enough:
                aquarius = x
                print(f"We are low on {aquarius}")
            return False
        else:
            vending_resources["Water"] = vending_resources["Water"] - 200
            vending_resources["Milk"] = vending_resources["Milk"] - 150
            vending_resources["Coffee"] = vending_resources["Coffee"] - 24
            return True

    if selection == "cappuccino":
        if vending_resources["Water"] < 250:
            not_enough["Water"] = vending_resources["Water"]
        if vending_resources["Milk"] < 100:
            not_enough["Milk"] = vending_resources["Milk"]
        if vending_resources["Coffee"] < 24:
            not_enough["Coffee"] = vending_resources["Coffee"]
        if not_enough != {}:
            for x in not_enough:
                aquarius = x
                print(f"We are low on {aquarius}")
            return False
        else:
            vending_resources["Water"] = vending_resources["Water"] - 250
            vending_resources["Milk"] = vending_resources["Milk"] - 100
            vending_resources["Coffee"] = vending_resources["Coffee"] - 24
            return True


def bill():
    drink = 0
    for y in drinks:
        if user_input == y:
            drink = drinks[user_input]
            print(f"The drink is ${drinks[user_input]}")
    print("Please insert coins:")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))

    q2 = 0
    d2 = 0
    n2 = 0
    p2 = 0
    if quarters > 0:
        q2 = quarters * .25
    if dimes > 0:
        d2 = dimes * .10
    if nickels > 0:
        n2 = nickels * .05
    if pennies > 0:
        p2 = pennies * .02

    total = q2 + d2 + n2 + p2
    if total < drink:
        print("Insert more money brokie: ")
        quarters += int(input("How many more quarters?: "))
        dimes += int(input("How many more dimes?: "))
        nickels += int(input("How many more nickels?: "))
        pennies += int(input("How many more pennies?: "))
        bill()
    elif total > drink:
        money_back = round(total - drink, 2)
        print(f"here is your shit back {money_back}")
    else:
        print("You are good to go thank you! rat")


machine_on = True
while machine_on:
    vending_resources = {"Water": 1000, "Milk": 500, "Coffee": 250, "Money": 200}
    drinks = {"espresso": 1.50, "latte": 2.50, "cappuccino": 3.00}

    print(vending_machine_logo)
    print("Thanks for using our vending machine.")
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
    check = False

    if resource_check(user_input):
        if user_input == "espresso" or user_input == "latte" or user_input == "cappuccino":
            bill()
            print(f"Here is your {user_input}: {coffee_emoji}")
            check = True
        elif user_input == "report":
            report()
        elif user_input == "off":
            machine_on = False
            break

    machine_on = False

