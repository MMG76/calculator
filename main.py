def calculator_sum(a, b):
    return a + b


def calculator_minus(a, b):
    return a - b


def calculator_multiply(a, b):
    return a * b


def calculator_divide(a, b):
    return a / b


operator = input("Enter the operator you need: ")

if operator == "sum":
    number_one = float(input())
    number_two = float(input())
    result = calculator_sum(number_one, number_two)
    print("result of", operator, "is:", result)

if operator == "minus":
    number_one = float(input())
    number_two = float(input())
    result = calculator_minus(number_one, number_two)
    print("result of", operator, "is:", result)

if operator == "multiply":
    number_one = float(input())
    number_two = float(input())
    result = calculator_multiply(number_one, number_two)
    print("result of", operator, "is:", result)

if operator == "divide":
    number_one = float(input())
    number_two = float(input())
    if number_two != 0:
        result = calculator_divide(number_one, number_two)
        print("result of", operator, "is:", result)
    else:
        print("result of", operator, "is:", "Bad input")


