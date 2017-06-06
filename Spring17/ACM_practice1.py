n,m = input().split()
l = [0 for i in range(int(n))]
ma = 0
for i in range(int(m)):
    a,b,c = input().split()
    for j in range(int(a)-1,int(b)):
        l[j]+=int(c)
        if ma<l[j]:
            ma = l[j]
print(ma)