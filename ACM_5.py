n = 7
ls = []
ls.append(1)
ls.append(2)
ls.append(4)
for i in range(3, n):
    ls.append(ls[i-1] + ls[i-2] + ls[i-3])

print(ls[n-1])