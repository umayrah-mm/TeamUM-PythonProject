def umayrah_calculator():
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        
        print("Addition:", a + b)
        print("Subtraction:", a - b)
        print("Multiplicaton:", a * b)
        print("Division:", a / b if b != 0 else "Cannot divide by zero.")

    except:
        print("Invalid input. Please enter numbers again.")