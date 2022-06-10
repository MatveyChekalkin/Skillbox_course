# Надо отметить,что это задание тоже не очень понятное (непонятно из чего?пользователь вводит или уже есть готовая срукт данных???)
#  У словаря нет индексов это ассоциативная структура данных
# Весьма сомнителшьное задание
def checking_array(checking_list):
    return [i for i, v in enumerate(checking_list)if is_prime(i)]

def is_prime(i_num):
    k = 0
    for i in range(2, i_num // 2 + 1):
        if i_num % i == 0:
            k = k + 1
    if k <= 0:
        return True
    else:
        return False

s = list(input('Введите текст: '))

i_list = checking_array(s)
s1 = []
for i_index in i_list:
    s1.append(s[i_index])
print(s1)