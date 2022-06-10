list_prob = list(range(10))
new_list =[tuple([i, i + 1]) for i in range(0, len(list_prob), 2)]
print('Оригинальный список: {} \nНовый список: {}'.format(list_prob, new_list))

# list_prob = list(range(10))
# new_list = []
# tup = 0
# start = 0
# step = 2
# while tup != 5:
#     new_list.append(tuple(list_prob[start:start+2]))
#     tup += 1
#     start +=step
# print('Оригинальный список: {} \nНовый список: {}'.format(list_prob, new_list))





