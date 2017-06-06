import collections
import sys
sys.setrecursionlimit(1000000)
child = collections.defaultdict(list)
for i in range(int(input())-1):
    a, b = input().strip().split()
    child[int(a)].append(int(b))
root = int(input())
queries = [int(input()) for j in range(int(input()))]

def find_longest(node):
    if node not in child:
        return 0
    else:
        return max([find_longest(i) for i in child[node]]) + 1

def longest(node):
    temp1 = find_longest(node)
    tnode = node
    while True:
        if tnode not in child:
            break
        elif len(child[tnode]) == 1:
            tnode = child[node][0]
        else:
            break
    temp2 = sorted([find_longest(j) for j in child[tnode]])
    if len(temp2) == 0:
        temp2 = 0
    else:
        temp2 = sum(temp2[-2:])

    if temp1>temp2:
        return temp1
    else:
        return temp2


for k in queries:
    print(longest(k))