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
    "money": 0,
}


def print_report():
    print(f"Water: {resources["water"]}ml")
    print(f"Milk: {resources["milk"]}ml")
    print(f"Coffee: {resources["coffee"]}g")
    print(f"Money: {resources["money"]}$")


def check_resources(drink_name):
    drink = MENU.get(drink_name)
    for ingredient, required_amount in drink["ingredients"].items():
        if resources.get(ingredient, 0) < required_amount:
            print(f"Sorry, there is not enough {ingredient}.")
            return False
    return True


def process_coins():
    print("Please insert coins.")

    quarters = int(input("How many quarters? ")) * 0.25
    dimes = int(input("How many dimes? ")) * 0.10
    nickels = int(input("How many nickles? ")) * 0.05
    pennies = int(input("How many pennies? ")) * 0.01

    paid_total = quarters + dimes + nickels + pennies
    return paid_total


def update_resources(drink, cost):
    for ingredient, amount in drink["ingredients"].items():
        resources[ingredient] -= amount
    resources["money"] += cost


def check_transaction(drink_name):
    drink = MENU[drink_name]
    cost = drink["cost"]
    paid = process_coins()

    if paid >= cost:
        change = paid - cost
        print(f"Here is {change} in change and your {drink_name}")
        update_resources(drink, cost)
    else:
        print("Sorry that's not enough. Money refunded")


on = True

while on:
    answer = input("What would you like? (espresso/latte/cappuccino): ")
    if answer == "off":
        on = False
    elif answer == "report":
        print_report()
    elif answer == "espresso" or answer == "latte" or answer == "cappuccino":
        if not check_resources(answer):
            continue
        else:
            check_transaction(answer)


# TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino): ”
# TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt.
# TODO: 3. Print report.
# TODO: 4. Check resources sufficient?
# TODO: 5. Process coins
# TODO: 6. Check transaction successful?
# TODO: 7. Make Coffee.
