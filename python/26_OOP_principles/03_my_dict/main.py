class MyDict(dict):

    def get(self, key, d=0):
        if key in self.keys():
            return self[key]
        else:
            return d


f = MyDict()
f[1]='первый'
f[2]='второй'
f[3]='третий'
print(f)

for i in range(1, 5 + 1):
    print(f.get(i))
