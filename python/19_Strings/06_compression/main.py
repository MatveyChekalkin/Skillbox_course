# Уже решал
text = input('Введите строку: ')

first = text[0]
count = 0
answer =''
for n in range(int(len(text))):
  if first == text[n]:
    count += 1
  elif first != text[n]:
    answer += first + str(count)
    count = 1
    first = text[n]

print(answer+text[n] + str(count))