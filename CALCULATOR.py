def calculator():
    print("Welcome to the Active Calculator!")
    print("Type 'exit' to quit.\n")
    
    while True:
        expression = input("Enter expression (e.g., 2 + 3 * 4): ")

        if expression.lower() == "exit":
            print("Goodbye!")
            break

        try:
            # Evaluate the expression and print the result
            result = eval(expression)
            print(f"Result: {result}\n")
        except Exception as e:
            print(f"Error: {e}\n")

calculator()
