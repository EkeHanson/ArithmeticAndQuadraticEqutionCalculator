num1 = float(input("Please enter the first Number: "))
num2 = float(input("Please enter the second Number: "))
num3 = float(input("Please enter the third Number: "))
if num2 < num1 > num3:
    print(f"The first number {num1} is the greatest")
elif num1 < num2 > num3:
    print(f"The second number {num2} is the greatest")
elif num1 < num3 > num2:
    print(f"The third number {num3} is the greatest")