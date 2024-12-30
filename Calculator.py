
import os
def add(first_number , second_number):
    return first_number + second_number
def subtract(first_number , second_number):
    return first_number - second_number
def multiplication(first_number , second_number):
    return first_number * second_number
def division(first_number , second_number):
    return first_number / second_number

dict = {'+':add, '-':subtract , '*':multiplication,'/': division}
first_number = int(input("What's the first number?: "))
for symbol in dict:
    print(symbol)
operator = input("Pick an operation: ")
next_number = int(input("What's the next number?: "))
calculation = dict[operator]
result = calculation(first_number=first_number,second_number=next_number)

print(f"{first_number} {operator} {next_number} = {result}")

counter = True

while counter:
    next_cal = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation, or type 'e' for exit the program: ")
    if next_cal == 'y':
        for symbol in dict:
            print(symbol)
        operator = input("Pick an operation: ")
        next_number = int(input("What's the next number?: "))
        calculation = dict[operator]
        result_cont = calculation(first_number=result,second_number=next_number)
        print(f"{result} {operator} {next_number} = {result_cont}")
    elif next_cal == 'n':
        os.system('cls')
        first_number = int(input("What's the first number?: "))
        for symbol in dict:
            print(symbol)
        operator = input("Pick an operation: ")
        next_number = int(input("What's the next number?: "))
        calculation = dict[operator]
        result = calculation(first_number=first_number,second_number=next_number)
        print(f"{first_number} {operator} {next_number} = {result}")
    else:
        counter = False
