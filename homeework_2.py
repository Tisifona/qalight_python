number_1 = float(input("Enter first number: "))
number_2 = float(input("Enter second number: "))
symbol = input("Enter symbol: ")


def summarizing(number_1, number_2):
    print(f"Your sum = {number_1 + number_2}")


def subtraction(number_1, number_2):
    print(f"Your subtraction = {number_1 - number_2}")


def multiplication(number_1, number_2):
    print(f"Your multiplication = {number_1 * number_2}")


def division(number_1, number_2):
    if number_2 == 0:
        print("You cannot divide by 0")
    else:
        print(f"Your division = {number_1 / number_2}")


if symbol == '+':
    summarizing(number_1, number_2)
if symbol == '-':
    subtraction(number_1, number_2)
if symbol == '/':
    division(number_1, number_2)
