n = int(input())
m = int(input())
matrix = [input().strip().split() for i in range(n)]
max_size = 0
visited = set()

def return_adjacents(j,k):
    adnodes = set()
    if j+1<n and k+1<m and matrix[j+1][k+1] == '1':
        adnodes.add((j+1,k+1))
    if j+1<n and k<m and matrix[j+1][k] == '1':
        adnodes.add((j+1,k))
    if j<n and k+1<m and matrix[j][k+1] == '1':
        adnodes.add((j,k+1))
    if j-1>=0 and k-1>=0 and matrix[j-1][k-1] == '1':
        adnodes.add((j-1,k-1))
    if j>=0 and k-1>=0 and matrix[j][k-1] == '1':
        adnodes.add((j,k-1))
    if j-1>=0 and k>=0 and matrix[j-1][k] == '1':
        adnodes.add((j-1,k))
    if j+1<n and k-1>=0 and matrix[j+1][k-1] == '1':
        adnodes.add((j+1,k-1))
    if j-1>=0 and k+1<m and matrix[j-1][k+1] == '1':
        adnodes.add((j-1,k+1))
    return adnodes

for j in range(n):
    for k in range(m):
        if (j,k) not in visited and matrix[j][k] == '1' :
            queue = set()
            queue.add((j,k))
            region_count = 1
            visited.add((j,k))
            while(len(queue)>0):
                new_queue = set()
                for node in queue:
                    for adjnode in return_adjacents(node[0],node[1]):
                        if adjnode not in visited:
                            region_count+=1
                            visited.add(adjnode)
                            new_queue.add(adjnode)
                queue = new_queue
            max_size = max(region_count,max_size)

print(max_size)

