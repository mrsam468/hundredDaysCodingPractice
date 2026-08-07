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


def report():
    for resource in resources:
        print(f"{resource}: {resources[resource]}")


def what_do_you_want(type_of_coffe, money):
    change = 0
    if type_of_coffe == "espresso":
        if resources["water"] > MENU["espresso"]["ingredients"]["water"]:
            if resources["coffee"] > MENU["espresso"]["ingredients"]["coffee"]:
                if money > MENU[type_of_coffe]["cost"] or money == MENU[type_of_coffe]["cost"]:
                    resources["water"] = resources["water"] - MENU["espresso"]["ingredients"]["water"]
                    resources["coffee"] = resources["water"] - MENU["espresso"]["ingredients"]["coffee"]
                    print(f"here is your {type_of_coffe}!enjoy yourself")
                    resources["Money"] = (f"${MENU[type_of_coffe]["cost"]}")
                    change = round(money - MENU[type_of_coffe]["cost"], 2)
                    if change > 0.0:
                        print(f"your change is ${change}")
                else:
                    print("not enough enough money! your money have been refunded!")
        else:
            print("not enough resources")
    elif type_of_coffe == "latte":
        if resources["water"] > MENU["latte"]["ingredients"]["water"]:
            if resources["milk"] > MENU["latte"]["ingredients"]["milk"]:
                if resources["coffee"] > MENU["latte"]["ingredients"]["coffee"]:
                    if money > MENU[type_of_coffe]["cost"] or money == MENU[type_of_coffe]["cost"]:
                        resources["water"] = resources["water"] - MENU["latte"]["ingredients"]["water"]
                        resources["milk"] = resources["milk"] - MENU["latte"]["ingredients"]["milk"]
                        resources["coffee"] = resources["coffee"] - MENU["latte"]["ingredients"]["coffee"]
                        print(f"here is your {type_of_coffe}!enjoy yourself")
                        resources["Money"] = (f"${MENU[type_of_coffe]["cost"]}")
                        change = money - round(MENU[type_of_coffe]["cost"], 2)
                        if change > 0.0:
                            print(f"your change is ${change}")
        else:
            print("not enough resources")
    else:
        if resources["water"] > MENU["cappuccino"]["ingredients"]["water"]:
            if resources["milk"] > MENU["cappuccino"]["ingredients"]["milk"]:
                if resources["coffee"] > MENU["cappuccino"]["ingredients"]["coffee"]:
                    if money > MENU[type_of_coffe]["cost"] or money == MENU[type_of_coffe]["cost"]:
                        resources["water"] = resources["water"] - MENU["cappuccino"]["ingredients"]["water"]
                        resources["milk"] = resources["milk"] - MENU["cappuccino"]["ingredients"]["milk"]
                        resources["coffee"] = resources["coffee"] - MENU["cappuccino"]["ingredients"]["coffee"]
                        print(f"here is your {type_of_coffe}!enjoy yourself")
                        resources["Money"] = (f"${MENU[type_of_coffe]["cost"]}")
                        change = money - round(MENU[type_of_coffe]["cost"])
                        if change > 0.0:
                            print(f"your change is ${change}")

        else:
            print("not enough resources")


def main():
    decision = input("what do you want do you want (report/coffee)").lower()
    if decision == "coffee":
        what_person_wants = input("What would you like? (espresso/latte/cappuccino): ")
        print("insert coins")
        dime = int(input("dime ")) * 0.10
        nickel = int(input("nickel ")) * 0.05
        pennies = int(input("pennies ")) * 0.01
        quater = int(input("quater ")) * 0.25
        total = dime + nickel + pennies + quater
        what_do_you_want(what_person_wants, total)
    else:

        report()


needs_another_coffe = True
while needs_another_coffe:
    main()
    turn_off = input("do you want to turn off? (y/n): ")
    if turn_off == "y":
        needs_another_coffe = False
