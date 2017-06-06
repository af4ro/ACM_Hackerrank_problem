import _collections
queries = input()
graphs = []
to_start = []
nodes = []
for i in range(int(queries)):
    a,b = input().split()
    nodes.append(int(a))
    temp = _collections.defaultdict(list)
    for j in range(int(b)):
        c,d = input().split()
        temp[int(c)].append(int(d))
        temp[int(d)].append(int(c))
    to_start.append(int(input()))
    graphs.append(temp)

def path(mainDict ,start, to_find):
    toExplore = [start]
    found = set()
    # found.add(start)
    d = 0
    while(len(toExplore)!=0):
        newExplore = set()
        for node in toExplore:
            if node == to_find:
                return d
            elif node not in found:
                for newnode in mainDict[node]:
                    newExplore.add(newnode)
                    found.add(newnode)
        toExplore = list(newExplore)
        d += 6
    return -1

z = 0
for j in graphs:
    temp = ""
    for k in range(nodes[z]):
        if k!=to_start[z]:
            temp+= str(path(j,to_start[z],k)) +" "
    print(temp)
    z+=1
