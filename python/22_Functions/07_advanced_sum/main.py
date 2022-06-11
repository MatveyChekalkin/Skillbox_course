def sum(*args):
    summ = 0
    for i in args:
        if isinstance(i, int):
            summ += i
        else:
            summ +=sum(*i)
    return summ


print(sum([[1, 2, [3]], [1], 3]))

print(sum(1, 2, 3, 4, 5))