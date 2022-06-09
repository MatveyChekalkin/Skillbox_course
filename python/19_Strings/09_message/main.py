def swap(a, b):
    return b, a

def reverse_each_word(sentence):
    list_of_string = [i for i in sentence.split(" ")]
    Finalresult = ""
    for eachString in list_of_string:
        eachString = [x for x in eachString]
        r = len(eachString) - 1
        l = 0
        while l < r:
            if not (eachString[l].isalpha() or eachString[l].isdigit()):
                l += 1
            elif not (eachString[r].isalpha() or eachString[r].isdigit()):
                r -= 1
            else:
                eachString[l], eachString[r] = swap(eachString[l], eachString[r])
                l += 1 
                r -= 1
        result = "".join(eachString)
        Finalresult += (result+" ")
    return Finalresult

print(f"Новое сообщение: {reverse_each_word(input('Сообщение: '))}")