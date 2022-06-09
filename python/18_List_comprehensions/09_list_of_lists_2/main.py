nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],[[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

nice_list2 = [num for list_2 in nice_list for many_list in list_2 for num in many_list]
print(nice_list2)


# for i in range(0, len(nice_list)):
#     for n in range(2 + 1):
#         for z in range(2 + 1):
#              print(nice_list[i][n][z], end=' ')

# for l in nice_list:
#     for a in l:
#         for x in a:
#             print(x, end=' ')