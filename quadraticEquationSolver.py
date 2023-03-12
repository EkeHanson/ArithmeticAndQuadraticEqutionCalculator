import math
a = float(input("Please enter \"a\" the coefficient of X\N{SUPERSCRIPT TWO}: "))
b = float(input("Please enter \"b\" the coefficient of X: "))
c = float(input("Please enter \"c\" the constant term: "))
discriminant = b * b - 4 * a * c
if discriminant == 0:
    print(f'The roots of the equation are equal x\N{SUBSCRIPT ONE} = {-b/(2 * a)} and x\N{SUBSCRIPT TWO} = {-b/(2 * a)}')
elif discriminant > 0:
    square_root_of_discriminant = math.sqrt(discriminant)
    x1 = (-b + square_root_of_discriminant) / (2 * a)
    x2 = (-b - square_root_of_discriminant) / (2 * a)
    print(f'The roots of the equation are x\N{SUBSCRIPT ONE} = {x1} and x\N{SUBSCRIPT TWO} = {x2}')
elif discriminant < 0:
    absolute_discriminant = abs(discriminant)
    square_root_of_absolute_discriminant = math.sqrt(absolute_discriminant)
    first_component = -b / (2 * a)
    second_component1 = square_root_of_absolute_discriminant / (2 * a)
    print(f'The roots of the equation are'
          f' x\N{SUBSCRIPT ONE} = {first_component} + {second_component1}j '
          f'and x\N{SUBSCRIPT TWO} = {first_component} - {second_component1}j ')
else:
    print(f' Opps!!! The roots of the equation cannot be determined')
