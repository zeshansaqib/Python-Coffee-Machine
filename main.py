from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from menu import Menu

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

print("☕ Welcome to the Python Coffee Machine! ☕")

while is_on:
    print("\nWhat would you like to do?")
    print("1. Order a drink")
    print("2. See report")
    print("3. Turn off the machine")

    action = input("Please enter 1, 2, or 3: ").strip()

    if action == "3":
        print("👋 Turning off the machine. Have a great day!")
        is_on = False

    elif action == "2":
        print("\n📋 Machine Report:")
        coffee_maker.report()
        money_machine.report()

    elif action == "1":
        options = menu.get_items()
        choice = input(f"\nAvailable drinks: {options}\nWhat would you like? ").lower()

        drink = menu.find_drink(choice)
        if drink:
            if coffee_maker.is_resource_sufficient(drink):
                if money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)
        else:
            print(f"❌ '{choice}' is not on the menu. Please choose a valid drink.")

    else:
        print("❌ Invalid input. Please select 1, 2, or 3.")
