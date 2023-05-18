from art import logo

def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def multiply(n1 , n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": sub,
    "*": multiply,
    "/": divide       
}

def calculator():
    print(logo)
    
    num1 = float(input("What's the first number ? "))
    for symbol in operations:
        print(symbol)
    end_of_calculation = False
    
    while not end_of_calculation:
        operation_symbol = input("Pick an operation from the line above: ")
        num2 = float(input("What's the second number ? "))
        calculation_function = operations[operation_symbol] 
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")   
        if input(f"Type 'y' to continue calculating with {answer} or type 'n' to start again ") == "y":
            num1 = answer
        else:
            end_of_calculation = True
            calculator()
calculator()