ATM Simulation

**Overview**

This project is a Python-based simulation of an Automated Teller Machine (ATM) that allows users to interact with a bank account through a command-line interface. The program starts with an initial balance and allows the user to perform common banking actions such as depositing money, withdrawing money, checking their balance, or exiting the program.

The system runs in a loop so that users can perform multiple transactions during a single session. The program also includes error checking to handle invalid inputs and ensure that transactions are processed correctly.

**Purpose**

The purpose of this project was to practice fundamental programming concepts such as loops, conditional statements, and input validation. It also focuses on designing programs that allow continuous user interaction while maintaining correct program flow and handling possible user errors.

**Features**

- Interactive command-line ATM interface
- Users can:
    - Deposit money
    - Withdraw money
    - Check account balance
    - Exit the program
- Continuous loop allowing multiple transactions
- Error checking for invalid menu selections
- Error checking for negative deposit or withdrawal amounts
- Warning message if an account balance becomes negative

**Program Behavior**

The program begins with a starting balance of $1000. Users are presented with a menu of options and can select an action using the following commands:

D - Deposit
W - Withdraw
B - Check Balance
E - Exit

After each transaction, the user is prompted again until they choose to exit the program.

**Programming Concepts Used**

This project demonstrates several important programming concepts:
- Loops to allow continuous user interaction
- Conditional statements (if, elif, else) to process user choices
- User input and output using input() and print()
- Error checking and input validation
- Basic state management through tracking the account balance
- Testing different program paths using test cases

**What I Learned**

Through this project, I learned how to construct programs that repeatedly interact with users using loops and menus. In collaboration with loops and menus, I practiced validating user input in these loops handling potential user errors which might mess with the code. Building this ATM simulation helped reinforce how conditional logic and loops can work together to manage a program that runs continuously until a specific exit condition is met. I really enjoyed the planning and processing in this project because it challeneged my knowledge of loops and error messages.
