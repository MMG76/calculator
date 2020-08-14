def calculator_sum(a, b):
    return a + b


def calculator_multiply(a, b):
    return a * b


operator = input("Enter the operator you need: ")

if operator == "sum" or operator == "minus":
    number_one = float(input())
    number_two = float(input())
    if operator == "minus":
        number_two = number_two * -1
    result = calculator_sum(number_one, number_two)
    print("result of", operator, "is:", result)

if operator == "multiply":
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
