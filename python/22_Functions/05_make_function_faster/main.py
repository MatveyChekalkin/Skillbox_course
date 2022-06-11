# def calculating_math_func(data):
#     result = 1
#     for index in range(1, data + 1):
#         result *= index
#     result /= data ** 3
#     result = result ** 10
#     return result


def calculating_math_func(number):
    if number == 1:
        return 1
    res = number * calculating_math_func(number - 1)
    return res

number = int(input('Введите число: '))
print((calculating_math_func(number) / number ** 3) ** 10)

# import math
#
# def calculating_math_func(number):
#     return math.pow((math.factorial(number) / math.pow(number, 3)), 10)
#
# number = int(input('Введите число: '))
# print(calculating_math_func(number))