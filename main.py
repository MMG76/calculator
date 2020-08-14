def calculator_sum(a, b):
    return a + b


def calculator_multiply(a, b):
    return a * b


def calculator_power(a, b):
    return a ** b


def calculator_factorial(a):
    if a <= 0:
        return 1
    return calculator_factorial(a - 1) * a


def calculator_mod(a, b):
    return a % b


def calculator_abs(a):
    if a <= 0:
        return a * -1
    return a


operator = input("Enter the operator you need: ")

if operator == "+" or operator == "-":
    number_one = float(input())
    number_two = float(input())
    if operator == "minus":
        number_two = number_two * -1
    result = calculator_sum(number_one, number_two)
    print("result of", operator, "is:", result)

if operator == "*" or operator == "/":
    temp = 0
    number_one = float(input())
    number_two = float(input())
    if operator == "divide":
        if number_two != 0:
            number_two = 1 / number_two
        else:
            temp = 1
            print("result of", operator, "is:", "Bad input")
    if temp == 0:
        result = calculator_multiply(number_one, number_two)
        print("result of", operator, "is:", result)

if operator == "^":
    number_one = float(input())
    number_two = float(input())
    result = calculator_power(number_one, number_two)
    print("result of", operator, "is:", result)

if operator == "!":
    number_one = float(input())
    result = calculator_factorial(number_one)
    print("result of", operator, "is:", result)

if operator == "||":
    number_one = float(input())
    result = calculator_abs(number_one)
    print("result of", operator, "is:", result)

if operator == "%":
    number_one = float(input())
    number_two = float(input())
    if number_two == 0:
        print("result of", operator, "is:", "Bad input")
    else:
        result = calculator_mod(number_one, number_two)
        print("result of", operator, "is:", result)