menu = {
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

def check_resources(resources, coffee_type):
    """
    This will check if the coffee machine has enough resources to make coffee.
    """
    #creating a variable to confirm coffee can be made.
    can_make_coffee = False
    #espresso
    if coffee_type == 'espresso':
        if resources["water"]> 50 and resources["coffee"]> 18:
            print("There are enough resources to make espresso")
            can_make_coffee = True
            return can_make_coffee
        else:
            print("There are not enough resources to make an espresso")

    elif coffee_type == 'latte':
        if resources["water"]> 200 and resources["coffee"]> 24 and resources["milk"]> 150:
            print("There are enough resources to make latte")
            can_make_coffee = True
            return can_make_coffee
        else:
            print("There are not enough resources to make an latte")
    elif coffee_type == 'cappuccino': 
        if resources["water"]> 250 and resources["coffee"]> 24 and resources["milk"]> 100:
            print("There are enough resources to make cappuccino")
            can_make_coffee = True
            return can_make_coffee
        else:
            print("There are not enough resources to make an cappuccino")

def process_coins( quaters, dimes, nickles, pennies):
    """
    Calculates the money inserted by the user.
    """
    user_money = 0
    user_money = 0.25 * (quaters) + 0.1 * (dimes) + 0.05 * (nickles) + 0.01 * (pennies)
    return user_money

def transaction_successful(user_money,coffee_type, resources):
    """
    Checks whether the user inserted enough coins to make coffee and return the change too!
    """
    trasaction_succ = False
    user_change =0 
    if coffee_type == "espresso":
            #calculating user_change
        if user_money > 1.5:
            resources['Money'] =1.5
            user_change = user_money - 1.5
            print(f"Here is ${user_change} dollars in change.")    
            trasaction_succ = True
        else:
            print("Sorry that's not enough money. Money refunded.")  

    elif coffee_type == "latte":
        #calculating user_change
        if user_money > 2.5:
            resources['Money'] =2.5
            user_change = user_money - 1.5
            print(f"Here is ${user_change} dollars in change.")
            trasaction_succ = True    
            return trasaction_succ
        else:
            print("Sorry that's not enough money. Money refunded.")  

    elif coffee_type == "cappuccino":
        if user_money > 2.5:
            resources['Money'] =2.5
            user_change = user_money - 1.5
            print(f"Here is ${user_change} dollars in change.")
            trasaction_succ = True    
        else:
            print("Sorry that's not enough money. Money refunded.") 

def make_coffee(coffee_type, transaction_successful, resources):
    """"
    This function will check whether the transaction was successfull and will deduct from the resources and make coffee
    """
    if transaction_successful:
        if coffee_type == "espresso" and resources['water'] > 50 and resources['coffee'] > 18 :
            resources['water']-=50
            resources['coffee'] -=18
        elif coffee_type == 'latte' and resources['water'] > 200 and resources['milk'] > 150 and  resources['coffee'] > 24:
            resources['water']-=200
            resources['milk'] -=150
            resources['coffee'] -=24
        elif coffee_type == 'cappuccino' and resources['water'] > 250 and resources['milk'] > 100 and  resources['coffee'] > 24:
            resources['water']-=250
            resources['milk'] -=100
            resources['coffee'] -=24
        print(f"Here is your {coffee_type} Enjoy!")

#for the while loop
coffee_continue = True

while coffee_continue:
    #taking user input 
    user_input =  input("What would you like? (espresso/latte/cappuccino):").lower()

    if user_input == 'report':
        print(resources)
    elif user_input == 'off':
        #make sure that the coffee machine is turned off
        coffee_continue = False
    elif user_input =="espresso":
        coffee_continue = check_resources(resources, user_input)
        #pass
    elif user_input == "latte":
        #do something call the fucntion
        coffee_continue = check_resources(resources, user_input)
    elif user_input == "cappuccino":
        #call the function 
        coffee_continue = check_resources(resources, user_input)
    else:
        print("Please enter a valid input!")     

    if coffee_continue:
        print("Please insert coins")
        user_quaters = int(input("how many quarters?:"))
        user_dime = int(input("how many dimes?:"))
        user_nickes = int(input("how many nickes?:"))
        user_pennies = int(input("how many pennies?:"))

        #calling the process_coins function to calculate the user money
        user_money = process_coins(user_quaters, user_dime, user_nickes, user_pennies)

        #checking whether the user has enough money to proceed with the transaction and getting the change too.
        trasaction_succ = transaction_successful(user_money, user_input, resources)
        #make coffee
        make_coffee(user_input, trasaction_succ, resources)