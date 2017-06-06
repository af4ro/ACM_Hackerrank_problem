import collections
import queue
q = int(input())
r = collections.defaultdict(list)
total_roads = 0
total_libs = 0
to_visit = queue.Queue()
visited = set()

def min_count():
    tot_r = 0
    tot_l = 0
    while not to_visit.empty():
        temp = to_visit.get()
        pq = queue.PriorityQueue()
        for i in r[temp]:
            pq.put(i)
        visited.add(temp)
        while not pq.empty():
            temp = to_visit.get()
            if temp not in visited:
                visited.add(temp[1])
                tot_r += 1
                for i in r[temp]:
                    pq.put(i)
        tot_l +=1

for i in range(q):
    total_roads = 0
    total_libs = 0
    cities,roads,costl,costr = input().split()
    if costr>=costl:
        print(costl*cities)
        continue
    for j in range(int(cities)):
        to_visit.put(j)
    visited = set()
    for j in range(int(roads)):
        a,b = input().split()
        r[a].append(b)
        r[b].append(a)
    min_count(costl,costr)
