def calculator():
    """
    A simple calculator with basic arithmetic operations.

    Prompt the user to input two numbers and an operation choice.
    Perform the calculation and display the result.
    """
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Choose an operation (+, -, *, /): ")

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error: Division by zero")
            return

    print(f"The result of {num1} {operation} {num2} is {result}")


# Call the calculator function to start the program
calculator()
