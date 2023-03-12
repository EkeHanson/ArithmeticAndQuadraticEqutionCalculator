operator = input("""Please select an operator:
                    A - for Addition
                    S - for Subtraction
                    D - for Division
                    M - for Multiplication
                    R - for Modulus Operation
                    P - for Square: 
                    H - for Help: 
                    """).title()
if operator == 'Help':
    print("Please select an operator:\n A - for Addition \n S - for Subtraction "
          "\n D - for Division \n M - for Multiplication \n R - for Modulus Operation \n P - for Square")
else:
    first_number = float(input("Please enter the first number: "))
    if operator == 'P':
        print(f"The square of {first_number} is {first_number * first_number}")
    else:
        second_number = float(input("Please enter the second number: "))
        if operator == 'A':
            print(f"The sum of {first_number} and {second_number} is {first_number + second_number}")
        elif operator == 'S':
            print(f"The difference between {first_number} and {second_number} is {first_number - second_number}")
        elif operator == 'D':
            print(f"The result of {first_number} divided by {second_number} is {first_number / second_number}")
        elif operator == 'M':
            print(f"The product of {first_number} and {second_number} is {first_number * second_number}")
        elif operator == 'R':
            print(f"The result of {first_number} modulus {second_number} is {first_number % second_number}")
        else:
            print(f"The operator \"{operator}\" is not recognized")

