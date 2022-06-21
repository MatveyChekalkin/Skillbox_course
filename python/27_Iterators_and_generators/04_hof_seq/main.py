def hofstadter_generator(s):
    a = s[:]
    while True:
        try:
            q = a[-a[-1]] + a[-a[-2]]
            a.append(q)
            yield q
        except IndexError:
            return


test = hofstadter_generator(10)
print(test)
