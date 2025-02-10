# CODE CRAFTERS PRESENTATION
import math

def greeting():
    userName=input("Enter your name :")
    if not userName:
        userName = "user"
    print(f"Hello {userName}")

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def Squareroot(a):
    if a < 0:
        return "an Error! You can't find squareroots of negative numbers . "
    return math.sqrt(a)
def power(a,b):
    return pow(a,b)


def calculator():
    greeting()
    while True:
        
        print("\nEnjoy the Simple Calculator")
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Squareroot")
        print("6 Raise to power")
        print("7. Exit")
        
        choice = input("Enter choice (1/2/3/4/5/6/7): ")        
        
        if choice in ('5'):
            num1 = int(input("Enter a number to find its squareroot :"))
            print(f" The squareroot of {num1} is {Squareroot(num1)}")
        if choice in ('6'):
            num1 = int(input("Enter the number you wish to raise to a power :"))
            num2 =int(input("Enter the power :"))
            print(f"The number {num1}, raised to power {num2} is {power(num1,num2)}")
        if choice == '7':
            print("Exiting calculator. Goodbye!")
            break
        
        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                
                operations = {
                    '1': add,
                    '2': subtract,
                    '3': multiply,
                    '4': divide,
                    #'5': Squareroot,
                    #'6': power
                }
                
                result = operations[choice](num1, num2)
                print(f"Result: {result}")
            except ValueError:
                print("Invalid input. Please enter numeric values.")
        elif not choice in ('1','2','3','4','5','6','7'):
            
            print("Invalid choice. Please select a valid option.")


calculator()

