def new_zip(tupe_num, str_ob, start=0):
    finish = min(len(tupe_num), len(str_ob))
    if finish != start:
        new = (tupe_num[start], str_ob[start])
        print(new)
        new_zip(tupe_num, str_ob, start + 1)

tupe_num = (10, 20, 30, 40)
str_ob = 'abcd'
new_zip(tupe_num,str_ob)

# new_zip = ((str_ob[i], num) for i, num in enumerate(tupe_num))
# print(new_zip)
# for i in new_zip:
#     print(i)