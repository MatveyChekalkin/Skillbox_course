def numbers(finish, start = 1):
    if finish + 1 != start:
        print(start, end=' ')   # костыль
        numbers(finish, start + 1) # рекурсия

numbers(int(input('Введите число: ')))

# def numbers(finish, start = 1):
#     print(*range(start, finish + 1))
#
# numbers(int(input('Введите число: ')))

