while True:
    print("\n--- Simple Calculator Menu ---")
    print("Type 'exit' as the operation if you want to quit.")
    
    # Taking user inputs
    num1 = float(input("Enter 1st number: "))
    num2 = float(input("Enter 2nd number: "))
    op = input("Enter operation (+, -, *, /) or 'exit': ").strip().lower()

    # Checking for exit condition
    if op == "exit":
        print("Closing the calculator. Thank you!")
        break

    # Performing mathematical operations
    if op == "+":
        print("Result:", num1 + num2)
    elif op == "-":
        print("Result:", num1 - num2)
    elif op == "*":
        print("Result:", num1 * num2)
    elif op == "/":
        if num2 == 0:
            print("Error: Division by zero is not allowed!")
        else:
            print("Result:", num1 / num2)
    else:
        print("Error: Invalid operation requested!")
