n = int(input())
import collections
def operate(outgoing):
    for i in outgoing.keys():
        for j in outgoing[i]:
            if j in outgoing and i in outgoing[j]:
                print("ORDER VIOLATION")
                return
    print("ORDER EXISTS")

for i in range(n):
    outgoing = collections.defaultdict(list)
    m = int(input())
    for j in range(m):
        temp = input().strip().split(',')
        for k in range(len(temp)):
            for l in range(k+1,len(temp)):
                outgoing[temp[k]].append(temp[l])
    operate(outgoing)
