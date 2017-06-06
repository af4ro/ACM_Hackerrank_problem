
n = int(input())
l = [int(i) for i in input().split()]
ind = 0
for i in range(n):
    if sum(l[0:i])>sum(l[i:]):
        ind = i
        break

l = l[ind:]+l[0:ind]
sm = 0
for i in range(n):
    sm+= l[i]*(i+1)
print(sm)
