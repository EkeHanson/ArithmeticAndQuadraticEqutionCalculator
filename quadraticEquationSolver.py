import math

while True:
    try:
        a = float(input("Enter value for a, the coefficient of X\N{SUPERSCRIPT TWO}: "))
    except ValueError:
        print("Invalid input for 'a'. Please enter a valid number.")
        continue

    while True:
        try:
            b = float(input("Enter value for b, coefficient of X: "))
            break  # Break out of the inner loop if input is valid
        except ValueError:
            print("Invalid input for 'b'. Please enter a valid number.")

    while True:
        try:
            c = float(input("Enter value for c as the constant: "))
            break  # Break out of the inner loop if input is valid
        except ValueError:
            print("Invalid input for 'c'. Please enter a valid number.")

    try:
        discriminant = (b ** 2) - 4 * a * c
        if discriminant == 0:
            print(f'x\N{SUBSCRIPT ONE} = {-b/(2 * a)} and x\N{SUBSCRIPT TWO} = {-b/(2 * a)}')
        elif discriminant > 0:
            square_root_discriminant = math.sqrt(discriminant)
            root_1 = (-b + square_root_discriminant)/(2 * a)
            root_2 = (-b - square_root_discriminant)/(2 * a)
            print(f'x\N{SUBSCRIPT ONE} = {root_1} and x\N{SUBSCRIPT TWO} = {root_2}')
        else:
            absolute_discriminant = abs(discriminant)
            square_root_discriminant = math.sqrt(absolute_discriminant)
            real_part = -b/(2 * a)
            imaginary_part = square_root_discriminant / (2 * a)
            print(f'x\N{SUBSCRIPT ONE} = {real_part} + {round(imaginary_part, 3)}i and x\N{SUBSCRIPT TWO} = {real_part} - {round(imaginary_part, 3)}i')
    except ZeroDivisionError:
        print("Error: 'a' coefficient cannot be zero.")
    except Exception as e:
        print(f"An error occurred: {e}")

  

    
