# Programmers: Rasheed Mustapha
# Problem Statement: a simulation of an ATM, where users can see their balance, deposit, withdraw, or exit at any time
# Data In: action user wants to take, deposit or withdrawn amount
# Data Out: balance amount after action, prompting user for next action


# Defining variable and sentinel, prompting user for action
balance = 1000
action = input("What action would you like to take? D - Deposit, W - Withdraw, B - Give Balance, E - Exit: ")
SENTINEL = "e"
action = action.lower()

#Error message to reprompt user
while action != "d" and action != "w" and action != "b" and action != "e":
    print("Please enter a valid option!")
    action = input("What action would you like to take? D - Deposit, W - Withdraw, B - Give Balance, E - Exit: ")
    action = action.lower()

# Actions while sentinel not inputted and reprompt message
while action != SENTINEL:
    # Action for "deposit"
    if action == "d":
        deposit = int(input("How much would you like to deposit?: "))
        balance = balance + deposit
        while deposit < 0:
            print("Please enter a positive deposit value.")
            deposit = int(input("How much would you like to deposit?: "))
        print("Your balance is:", balance)
    # Action for "withdraw"
    if action == "w":
        withdraw = int(input("How much would you like to withdraw?: "))
        balance = balance - withdraw
        while withdraw < 0:
            print("Please enter a positive withdraw value.")
            withdraw = int(input("How much would you like to withdraw?: "))
        print("Your balance is:", balance)
    # Action for "balance"
    if action == "b":
        print("Your balance is:", balance)
    if balance < 0:
        print("You will be charge 5% interest because your balance is negative.")
    action = input("What action would you like to take? D - Deposit, W - Withdraw, B - Give Balance, E - Exit: ")
