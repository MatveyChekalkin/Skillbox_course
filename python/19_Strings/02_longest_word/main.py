text = input('Введите строку: ').split()
word_len = [len(word) for word in text]
print('Слово с максимальной длиной: {word} и состоит из {count_s} символов'.format(
    word=text[word_len.index(max(word_len))],
    count_s=max(word_len)
))
