import _collections
N,M = input().split()
l = _collections.defaultdict(set)
for i in range(int(M)):
    a,b = input().split()
    l[int(a)].add(int(b))
    l[int(b)].add(int(a))

def dfs(children,visited,result):
    if len(children) == 0 or children == None:
        return (1,result)
    mainodes = 0
    for i in children:
        visited.add(i)
        (nodes,r) = dfs(l[i]-visited,visited,0)
        mainodes+=nodes
        result+=r
    if mainodes%2 != 0:
        result+=1
        return (0,result)
    return (mainodes,result)

temp = set()
temp.add(1)
t = len(l[1])
# (t1,t2) = dfs(l[1],temp,0)
(t1,t2) = dfs(temp,set(),0)
print(t1,t2)
# if t1 == 0:
#     print(t2)
# elif t1%2 == 0:
#     print(t2+1)
# else:
#     print(t2)