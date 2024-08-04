#!/usr/bin/env python3

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}

def calculator():
    num1 = int(input("What's the first number: "))
    for symbol in operations:
        print(symbol)
    continue_calculating = True


    while continue_calculating:
        operation_symbol = input("Pick an operation from the symbols above: ")
        num2 = int(input("What's the second number: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input("Do you want to continue calculating with the previous function (y or n)?: ").lower() == "y":
            num1 = answer
        else:
            continue_calculating = False
            calculator()

calculator()
