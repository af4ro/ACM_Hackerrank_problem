n,m = input().strip().split()
graph = []
ranks = []
sm = 0
for i in range(int(n)):
    temp = []
    temp1 = []
    for j in input().split():
        temp.append(int(j))
        sm+=int(j)
        temp1.append(0)
    graph.append(temp)
    ranks.append(temp1)

for i in range(int(n)):
    m = max(graph[i])
    t = [i for i, j in enumerate(graph[i]) if j == m]
    for k in t:
        ranks[i][k] = 1

tg = [list(i) for i in zip(*graph)]
tr = [list(i) for i in zip(*ranks)]
for i in range(int(n)):
    m = max(tg[i])
    t = [i for i, j in enumerate(tg[i]) if j == m]
    for k in t:
        tr[i][k] = 1
ranks = [list(i) for i in zip(*tr)]



print(ranks)
print(graph)
print(sm)
