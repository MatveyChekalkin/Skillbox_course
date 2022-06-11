nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]

def list_transformation(nice_list):
    new_list = []
    for i in nice_list:
        if isinstance(i,int):
            new_list.append(i)
        else:
            new_list.extend(list_transformation(i))
    return new_list

print('Ответ: {}'.format(list_transformation(nice_list)))