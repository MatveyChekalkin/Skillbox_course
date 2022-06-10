def tuple_form(tuple_put, sym):
    listt = list(tuple_put)
    if tuple_put.count(sym) == 0:
        return ()
    elif tuple_put.count(sym) == 1:
        return tuple(listt[listt.index(sym):])
    else:
        return tuple(listt[listt.index(sym):listt.index(sym, listt.index(sym) + 1) + 1])

tuple_put = tuple(input('Введите текст: ').lower())
sym = input('введите букву: ')
print(tuple_form(tuple_put, sym))
