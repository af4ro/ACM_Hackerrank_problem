import collections
outgoing = collections.defaultdict(list)
visited = []
for i in range(int(input ())):
    for j in range(int(input())):
        temp = input().strip().split()
        for k in range(len(temp)):
            for l in range(k + 1, len(temp)):
                outgoing[temp[k]].append(temp[l])
        if temp[0] not in visited:
            visited.append(temp[0])
    print(outgoing)
