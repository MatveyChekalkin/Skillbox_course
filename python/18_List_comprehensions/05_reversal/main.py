a = input('Введите строку: ')
print(a[:a.index('h')]+a[a.rindex('h'):a.index('h'):-1] + a[a.rindex('h'):])

# b = a[::-1]
# if a.index('h') == 0 and - (1 + b.index('h')) == -1:
#     print(a[::-1])
# elif a.index('h') == 0:
#     print(a[- (1 + b.index('h')):: -1] + a[1 - (1 + b.index('h')):])
# elif - (1 + b.index('h')) == -1:
#     print(a[:a.index('h')] + a[- (1 + b.index('h')):a.index('h'): -1] + a[-1])
# else:
#     print(a[:a.index('h')] + a[- (1 + b.index('h')):a.index('h') - 1: -1] + a[1 - (1 + b.index('h')):])