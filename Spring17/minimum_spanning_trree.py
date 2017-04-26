import queue
import collections
n ,m = input().split()
edges = collections.defaultdict(list)
for i in range(int(m)):
    a,b,c = input().split()
    edges[int(a)].append((int(c),int(b)))
    edges[int(b)].append((int(c),int(a)))
start = int(input())
total_weight = 0
pq = queue.PriorityQueue()
for i in edges[start]:
    pq.put(i)
found = set()
found.add(start)
while not pq.empty():
    temp = pq.get()
    if temp[1] not in found:
        found.add(temp[1])
        total_weight+=temp[0]
        for i in edges[temp[1]]:
            pq.put(i)
print(total_weight)

