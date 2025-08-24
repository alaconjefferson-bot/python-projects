# Simple Calculator
# Step 1: Functions for each operation

def add(a, b):
    return a + b   # Addition

def subtract(a, b):
    return a - b   # Subtraction

def multiply(a, b):
    return a * b   # Multiplication

def divide(a, b):
    return a / b   # Division (walang error handling muna)

# Step 2: Menu + Loop
while True:
    print("\n--- Simple Calculator ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    if choice == "5":
        print("Goodbye!")
        break   # tapos na program

    # Ask numbers
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Do the chosen operation
    if choice == "1":
        print("Result:", add(num1, num2))
    elif choice == "2":
        print("Result:", subtract(num1, num2))
    elif choice == "3":
        print("Result:", multiply(num1, num2))
    elif choice == "4":
        print("Result:", divide(num1, num2))
    else:
        print("Invalid choice, please try again.")
