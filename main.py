def calculator_sum(a, b):
    return a + b


def calculator_multiply(a, b):
    return a * b


operator = input("Enter the operator you need: ")

if operator == "sum":
    number_one = float(input())
    number_two = float(input())
    result = calculator_sum(number_one, number_two)
    print("result of", operator, "is:", result)

if operator == "multiply":
    number_one = float(input())
    number_two = float(input())
    result = calculator_multiply(number_one, number_two)
    print("result of", operator, "is:", result)


