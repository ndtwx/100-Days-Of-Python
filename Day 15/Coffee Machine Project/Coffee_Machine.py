from data import MENU, resources, profit
# TODO:4. Check resources sufficient?
def check_resources(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

# TODO:5. Process coins.
def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("How many 1 dollar?:")) * 1.00
    total += int(input("How many 50 cents:"))* 0.50
    total += int(input("How many 20 cents:")) * 0.20
    total += int(input("How many 10 cents:")) * 0.10
    return total

# TODO:6. Check transaction successful?
def check_transaction(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

# TODO:7. Make Coffee.
def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")
    print("-----------------------------------")

is_on = True

while is_on:
    # TODO:1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
    print(f"1.Espresso: ${MENU["espresso"]["cost"]}")
    print(f"2.Latte: ${MENU["latte"]["cost"]}")
    print(f"3.Cappuccino: ${MENU["cappuccino"]["cost"]}")
    choice = input("What would you like to drink? Choose 1 or 2 or 3 : ")
    # TODO:2. Turn off the Coffee Machine by entering “off” to the prompt.
    if choice == "off":
        is_on = False
    # TODO:3. Print report.
    elif choice == "report":
        print("REPORT:")
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Profit: ${profit}")
        print("-----------------------------------")

    elif choice == "refill":
        if (resources["water"] == 300 and
                resources["milk"] == 200 and
                resources["coffee"] == 100):
            print("Ingredients are full")
        else:
            resources["water"] = 300
            resources["milk"] = 200
            resources["coffee"] = 100
            print("Ingredients have been refilled")
        print("-----------------------------------")

    else:
        if choice == "1":
            drink = MENU["espresso"]
            choice = "Espresso"
        elif choice == "2":
            drink = MENU["latte"]
            choice = "Latte"
        elif choice == "3":
            drink = MENU["cappuccino"]
            choice = "Cappuccino"

            if check_resources(drink["ingredients"]):
                payment = process_coins()
                if check_transaction(payment, drink["cost"]):
                    make_coffee(choice, drink["ingredients"])
