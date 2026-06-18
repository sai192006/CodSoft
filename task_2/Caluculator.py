def calculator():
    print("***** SIMPLE CALCULATOR *****")
    
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Error: Invalid numeric input.")
        return

    print("Choose an operation:")
    print("+ : Addition")
    print("- : Subtraction")
    print("* : Multiplication")
    print("/ : Division")
    
    operation = input("Enter operation symbol (+, -, *, /): ").strip()
    
    print("Result:")
    if operation == '+':
        print(f"{num1} + {num2} = {num1 + num2}")
    elif operation == '-':
        print(f"{num1} - {num2} = {num1 - num2}")
    elif operation == '*':
        print(f"{num1} * {num2} = {num1 * num2}")
    elif operation == '/':
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            print(f"{num1} / {num2} = {num1 / num2}")
    else:
        print("Invalid operation choice.")

if __name__ == "__main__":
    calculator()