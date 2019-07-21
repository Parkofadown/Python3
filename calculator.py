def add(num1,num2):
    return num1 + num2

def multiply(num3, num4):
    return num3 * num4 

def subtract(num5,num6):
    return num5 - num6 

def divide(num7, num8):
    return num7 / num8 

selection = int(input("Enter 0 to quit, 1 to add, 2 to subtract, 3 to multiply, 4 to divide: "))
while selection != 0:
    if selection == 1:
        question1 = float(input("Enter first number: "))
        question2 = float(input("Enter second number: "))
        print(add(question1,question2))
        selection = int(input("Enter 0 to quit, 1 to add, 2 to subtract, 3 to multiply, 4 to divide: "))
    if selection == 2:
        question3 = float(input("Enter first number: "))
        question4 = float(input("Enter second number: "))
        print(subtract(question3, question4))
        selection = int(input("Enter 0 to quit, 1 to add, 2 to subtract, 3 to multiply, 4 to divide: "))
    if selection == 3: 
        question5 = float(input("Enter first number: "))
        question6 = float(input("Enter second number: "))
        print(multiply(question5,question6))
        selection = int(input("Enter 0 to quit, 1 to add, 2 to subtract, 3 to multiply, 4 to divide: "))
    if selection == 4: 
        question7 = float(input("Enter first number: "))
        question8 = float(input("Enter second number: "))
        print(divide(question7,question8))
        selection = int(input("Enter 0 to quit, 1 to add, 2 to subtract, 3 to multiply, 4 to divide: "))
    elif selection > 4 & selection < 0:
        print("You have entered an invalid number, try again.\n")
        selection = int(input("Enter 0 to quit, 1 to add, 2 to subtract, 3 to multiply, 4 to divide: "))
    else:
        break
        