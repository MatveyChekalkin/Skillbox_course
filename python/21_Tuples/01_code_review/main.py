students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


# def f(dict):
#     lst = []
#     string = ''
#     for i in dict:
#         lst += (dict[i]['interests'])
#         string += dict[i]['surname']
#     cnt = 0
#     for s in string:
#         cnt += 1
#     return lst, cnt
#
#
# pairs = []
# for i in students:
#     pairs += (i, students[i]['age'])
#
#
# my_lst = f(students)[0]
# l = f(students)[1]
# print(my_lst, l)

# Условия сформулированны плохо, точнее не логично

def list_len(dict):
    interests = list()
    string = ''
    for key, values in dict.items():
        interests.extend(values.get('interests'))
        string += values.get('surname')
    return interests, len(string)

# Вывести на экран список пар “айди студента - возраст” этого допустим в коде не было!!!оно нужно?
for key, values in students.items():
    print(f'id: {key}, age: {values.get("age")}')
# Или требовался список???
print([(i, g.get('age')) for i, g in students.items()])

my_lst,len = list_len(students)
print(f'\nСписок интересов: {my_lst} \nДлина фамилий: {len}'.format(my_lst = my_lst, len=len))

