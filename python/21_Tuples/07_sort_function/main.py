def sorter(sumb):
    list_s = list(sumb)
    for i in list_s:
        if type(i) is not int:
            return sumb
    list_s.sort()
    return tuple(list_s)

sumb = (9, 3, 6, 1, 4)
print(sorter(sumb))
